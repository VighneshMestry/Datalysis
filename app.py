import sqlite3
from flask import Flask, Response, redirect, render_template, jsonify, request
from streamlit.web.server import server
from openpyxl import load_workbook

app = Flask(__name__)

@app.route('/') 
def hello():
    return render_template('login.html')
def HomePage():
    return redirect('http://localhost:8501')

if __name__ == '__main__':
    # app.run(debug = True)
    app.debug = True
    app.run(host = '0.0.0.0', port=5000)

@app.route('/join', methods = ['GET', 'POST'])
def hoJa():
    email = request.form['email']
    password = request.form['password']
    print("python__________ ", email)
    print(password)
    if request.method == 'POST':
        connection = sqlite3.connect('userdata.db')
        cursor = connection.cursor()
        email = request.form['email']
        password = request.form['password']
        print(email, password)

        query = "SELECT email, password FROM userdata WHERE email = ? and password = ?"
        cursor.execute(query, (email, password))
        results = cursor.fetchall()
        connection.commit()
        connection.close()
        print('results' , results)
        if len(results) == 0:
            print('Sorry worng credentials')
            print("final checking ", email, password)
            return redirect('https://www.elegantthemes.com/blog/wp-content/uploads/2019/12/401-error-wordpress-featured-image.jpg')
        else:
            return HomePage()

@app.route('/sign', methods = ['GET', 'POST'])
def hoJaWaps():
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    print(username)
    print("python__________ ", email)
    print(password)
    connection = sqlite3.connect('userdata.db')
    cur = connection.cursor()
    queryChecking = "SELECT username, email FROM userdata where username = '"+username+"' and email = '"+email+"'"

    cur.execute(queryChecking)
    results = cur.fetchall()
    print('results' , results)

    if len(results) == 0:
         if any(char.isdigit() for char in password):
            if len(password)>=8:
                cur.execute("INSERT INTO userdata (username, email, password) VALUES (?, ?, ?)", (username, email, password))
                # cur.execute(queryUpdating)
                print("signup ", username, password)
                connection.commit()
                return render_template('login.html')

    else:
        connection.commit()
        print('failed')
        return redirect('https://www.elegantthemes.com/blog/wp-content/uploads/2019/12/401-error-wordpress-featured-image.jpg')

@app.route('/product_to_db', methods = ['GET', 'POST'])
def ProductToDb():
    place = request.form['place']
    customer_type = request.form['customer_type']
    product_line = request.form['product_line']
    unit_price = request.form['unit_price']
    total = request.form['total']
    payment = request.form['payment']
    gross_income = request.form['gross_income']
    print(place, customer_type, product_line, unit_price, total, payment, gross_income)

    wb = load_workbook('supermarket_sales.xlsx')
    ws = wb.active
    ws.append(['', '123-45-6789', 'A', place, customer_type, 'Male', product_line, unit_price, '10', '18.00', total, '########', '12:00', payment, '500.00', '4.761904762', gross_income, '10.0']) 

    wb.save('supermarket_sales.xlsx')

    connection = sqlite3.connect('productdata.db')
    cur = connection.cursor()
    cur.execute("INSERT INTO productdata (place, customer_type, product_line, unit_price, total, payment, gross_income) VALUES (?, ?, ?, ?, ?, ?, ?)", (place, customer_type, product_line, unit_price, total, payment, gross_income))
    connection.commit()
    return redirect('http://localhost:8501')

@app.route('/signup_page')
def DisplaySignUp():
    return render_template('signup.html')

@app.route('/login_page')
def DisplayLogIn():
    return render_template('login.html')

@app.route('/add_product_page')
def DisplayAddProductPage():
    return render_template('addProduct.html')