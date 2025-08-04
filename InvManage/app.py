from flask import Flask, render_template, request, redirect, url_for, flash
from db_config import get_connection

app = Flask(__name__)
app.secret_key = 'abc123xyz@securekey'

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Replace with actual DB check (hardcoded for now)
        if username == "admin" and password == "admin123":
            return redirect(url_for('dashboard'))
        else:
            flash("Invalid credentials", "danger")
            return redirect(url_for('login'))
    
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT COUNT(*) AS total FROM products")
    total = cursor.fetchone()['total']
    cursor.close()
    conn.close()
    return render_template('dashboard.html', total=total)


@app.route('/add', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']
        qty = request.form['quantity']
        
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO products (name, price, quantity) VALUES (%s, %s, %s)", (name, price, qty))
        conn.commit()
        cursor.close()
        conn.close()
        flash("Product Added Successfully!", "success")
        return redirect(url_for('view_products'))

    return render_template('add_product.html')

@app.route('/products')
def view_products():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM products")
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('view_products.html', products=data)

if __name__ == '__main__':
    app.run(debug=True)
