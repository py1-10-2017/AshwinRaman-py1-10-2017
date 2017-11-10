from flask import Flask, render_template, request, redirect
from mySQLConnector import MySQLConnection


app = Flask(__name__)
mysql = MySQLConnection(app, 'flask_friends')

@app.route('/')
def index():
    query = 'SELECT * FROM friends'
    friends = mysql.query_db(query)
    return render_template('index.html', friends = friends)

@app.route('/addfriend', methods=['POST'])
def add():
    query = "INSERT INTO friends(first_name, last_name, email, created_at, updated_at) VALUES(:first_name, :last_name, :email, NOW(), NOW())"
    data = {'first_name' : request.form['first_name'], 'last_name':request.form['last_name'], 'email' : request.form['email']}
    mysql.query_db(query, data)
    return redirect('/')


app.run(debug=True)
