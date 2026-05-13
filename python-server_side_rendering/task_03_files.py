from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

@app.route('/products')
def products():
    source = request.args.get('source')
    prod_id = request.args.get('id')
    
    if source not in ['json', 'csv']:
        return render_template('product_display.html', error="Wrong source")
    
    products_list = []
    if source == 'json':
        try:
            with open('products.json', 'r') as f:
                products_list = json.load(f)
        except Exception:
            products_list = []
    elif source == 'csv':
        try:
            with open('products.csv', 'r') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    row['id'] = int(row['id'])
                    row['price'] = float(row['price'])
                    products_list.append(row)
        except Exception:
            products_list = []
            
    if prod_id is not None:
        try:
            prod_id = int(prod_id)
            products_list = [p for p in products_list if p['id'] == prod_id]
            if not products_list:
                return render_template('product_display.html', error="Product not found")
        except ValueError:
            return render_template('product_display.html', error="Product not found")

    return render_template('product_display.html', products=products_list)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
