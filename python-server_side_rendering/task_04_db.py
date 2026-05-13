from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

@app.route('/products')
def products():
    source = request.args.get('source')
    prod_id = request.args.get('id')
    
    if source not in ['json', 'csv', 'sql']:
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
    elif source == 'sql':
        try:
            conn = sqlite3.connect('products.db')
            cursor = conn.cursor()
            if prod_id is not None:
                cursor.execute("SELECT id, name, category, price FROM Products WHERE id=?", (prod_id,))
            else:
                cursor.execute("SELECT id, name, category, price FROM Products")
            
            rows = cursor.fetchall()
            for row in rows:
                products_list.append({'id': row[0], 'name': row[1], 'category': row[2], 'price': row[3]})
            conn.close()
        except Exception as e:
            return render_template('product_display.html', error="Database error")

    if prod_id is not None and source != 'sql':
        try:
            prod_id = int(prod_id)
            products_list = [p for p in products_list if p['id'] == prod_id]
            if not products_list:
                return render_template('product_display.html', error="Product not found")
        except ValueError:
            return render_template('product_display.html', error="Product not found")
    elif prod_id is not None and source == 'sql' and not products_list:
        return render_template('product_display.html', error="Product not found")

    return render_template('product_display.html', products=products_list)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
