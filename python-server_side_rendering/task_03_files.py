import csv
import json
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

    return data

if __name__ == '__main__':
   app.run(debug=True, port=5000)