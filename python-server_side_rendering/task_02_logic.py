import json
from flask import Flask, render_template

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

if __name__ == '__main__':
   app.run(debug=True, port=5000)