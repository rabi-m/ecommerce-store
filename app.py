from flask import Flask, render_template, request

app = Flask(__name__)

# قاعدة بيانات محدثة تحتوي على صور المنتجات
PRODUCTS = [
    {"id": 1, "name": "Laptop", "price": 1000, "description": "High-performance laptop", "image": "laptop.jpg"},
    {"id": 2, "name": "Phone", "price": 500, "description": "Latest smartphone", "image": "phone.jpg"},
    {"id": 3, "name": "Headphones", "price": 100, "description": "Noise-cancelling headphones", "image": "headphones.jpg"},
]

@app.route('/')
def home():
    # عرض الصفحة الرئيسية مع المنتجات
    return render_template('index.html', products=PRODUCTS)

@app.route('/product/<int:product_id>')
def product_detail(product_id):
    # العثور على المنتج بناءً على ID
    product = next((p for p in PRODUCTS if p['id'] == product_id), None)
    if not product:
        return render_template('404.html'), 404
    return render_template('product.html', product=product)

@app.route('/about')
def about():
    # صفحة "من نحن"
    return render_template('about.html')

@app.errorhandler(404)
def page_not_found(e):
    # صفحة الخطأ 404
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000)

