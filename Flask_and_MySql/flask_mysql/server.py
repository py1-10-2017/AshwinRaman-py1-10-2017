import mysqlconnection
from flask import Flask, render_template, redirect, session, request
app = Flask(__name__)
app.secret_key = "my secret sesssssion keey"
connection = mysqlconnection.MySQLConnector(app, "facebook")
print connection.query_db("SELECT * FROM users")
app.run(debug=True)



# an example of running a query
#print mysql.query_db("SELECT * FROM users")
