import csv
import json
import sqlite3
from flask import Flask, render_template, request
from pathlib import Path

app = Flask(__name__)

@app.route('/')
def home():
   return render_template('index.html')

@app.route('/about')
def about():
   return render_template('about.html')

@app.route('/contact')
def contact():
   return render_template('contact.html')

@app.route('/items')
def items():
    items_list = []

    with open("items.json", 'r') as f:
        rows = json.load(f)
    for k, v in rows.items():
        items_list = v

    return render_template('items.html', items=items_list)

@app.route('/products')
def products():
    source = request.args.get('source')
    id = request.args.get('id')

    data = []
    if source == "json":
        data = load_json_data("products.json", id)
    elif source == "csv":
        data = load_csv_data("products.csv", id)
    elif source == "sql":
        data = load_sql_data("products.db", id)

    return render_template('product_display.html', data=data, source=source, id=id)

def load_json_data(filename, desired_id = None):
    data = []

    if not Path(filename).is_file():
        raise FileNotFoundError("Data file '{}' missing".format(filename))

    try:
        with open(filename, 'r') as f:
            rows = json.load(f)

        for row in rows:
            id = str(row['id'])

            if (desired_id is not None and id == desired_id) or (desired_id is None):
                product = {}
                for k,v in row.items():
                    product[k] = v
                data.append(product)

    except ValueError:
        raise ValueError("Unable to load data from file '{}'".format(filename))

    return data

def load_csv_data(filename, desired_id = None):
    data = []

    if not Path(filename).is_file():
        raise FileNotFoundError("Data file '{}' missing".format(filename))

    try:
        with open(filename, 'r') as f:
            for row in csv.DictReader(f):
                if (desired_id is not None and row['id'] == desired_id) or (desired_id is None):
                    data.append(row)
    except ValueError:
        raise ValueError("Unable to load data from file '{}'".format(filename))
    
    print("final data = ", data)
    return data

def load_sql_data(filename, desired_id = None):
    if not Path("products.db").is_file():
        create_database()

    data = []

    if desired_id is not None:
        desired_id = " WHERE id = " + desired_id
    else:
        desired_id = ""

    con = sqlite3.connect(filename)
    cur = con.cursor()
    res = cur.execute("SELECT * FROM products " + desired_id)
    rows = res.fetchall()

    keys = []
    colnames = cur.description
    for desc in colnames:
        keys.append(desc[0])
    
    for row_tuple in rows:
        item = {}
        i = 0
        for v in row_tuple:
            item[keys[i]] = v
            i = i + 1
        data.append(item)

    return data

def create_database():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS Products (
                   id INTEGER PRIMARY KEY,
                   name TEXT NOT NULL,
                   category TEXT NOT NULL,
                   price REAL NOT NULL
                   )
                   ''')
    cursor.execute('''
                   INSERT INTO Products (id, name, category, price)
                   VALUES
                   (1, 'Laptop', 'Electronics', 799.99),
                   (2, 'Coffee Mug', 'Home Goods', 15.99)
                   ''')
    conn.commit()
    conn.close()

if __name__ == '__main__':
   app.run(debug=True, port=5000)