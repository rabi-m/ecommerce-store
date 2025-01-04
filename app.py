from flask import Flask, render_template, request

app = Flask(__name__)

# قاعدة بيانات مؤقتة (للأمثلة فقط)
PRODUCTS = [
    {"id": 1, "name": "Laptop", "price": 1000},
    {"id": 2, "name": "Phone", "price": 500},
    {"id": 3, "name": "Headphones", "price": 100},
]

@app.route('/')
def home():
    return render_template('index.html', products=PRODUCTS)

@app.route('/product/<int:product_id>')
def product_detail(product_id):
    product = next((p for p in PRODUCTS if p['id'] == product_id), None)
    return render_template('product.html', product=product)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
