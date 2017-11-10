# import dependencies
from flask import Flask, request, render_template, redirect, session, flash
from mysqlconnection import MySQLConnector
import re
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.secret_key = "secreeeet"
mysql = MySQLConnector(app, 'login_registration')
bcrypt = Bcrypt(app)

EMAIL_REGEX = re.compile(r'^[a-zA-Z-_+.]+@[a-zA-Z-_]+\.[a-zA-Z]+$')

# begin routes
@app.route('/')
def index():
    get_all_query = "SELECT * FROM users"
    users = mysql.query_db(get_all_query)
    print "index method: found", len(users), "users in the db"
    return render_template('index.html', users=users)

@app.route('/success')
def success():
    if 'id' not in session:
        return redirect('/')
    userdata = {'id': session['id']}
    users = mysql.query_db('SELECT * FROM users WHERE id = :id', userdata)
    current_user = users[0]
    return render_template('success.html', user=current_user)

@app.route('/register', methods=['POST'])
def register():
    print request.form
    errors = []

    if len(request.form['first_name']) < 2:
        errors.append('first name must be at least 2 characters long')
    elif not request.form['first_name'].isalpha():
        errors.append('first name must contain only letters')

    if len(request.form['last_name']) < 2:
        errors.append('last name must be at least 2 characters long')
    elif not request.form['last_name'].isalpha():
        errors.append('last name must contain only letters')

    if not EMAIL_REGEX.match(request.form['email']):
        errors.append('email must be valid')

    if not len(request.form['password']) >= 8:
        errors.append('password must be at least 8 characters')
    elif not request.form['confirm_password'] == request.form['password']:
        errors.append('password and confirm password must match exactly')

    if errors:
        for error in errors:
            flash(error)
        return redirect('/')
    else:
        hashed_pw = bcrypt.generate_password_hash(
            request.form['password']
        )
        user_data = {
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'email': request.form['email'],
            'password': hashed_pw
        }
        print user_data
        register_query = """INSERT INTO users
        (first_name, last_name, email, password, created_at, updated_at)
        VALUES
        (:first_name, :last_name, :email, :password, NOW(), NOW())
        """
        new_user_id = mysql.query_db(register_query, user_data)
        print new_user_id
        if new_user_id is not 0:
            session['id'] = new_user_id
        else:
            flash('user creation failed')
        return redirect('/success')

@app.route('/login', methods=['POST'])
def login():
    print request.form
    email = request.form['email']
    password = request.form['password']

    if not EMAIL_REGEX.match(email):
        flash('email is not valid')

    if not len(password) > 7:
        flash("password isn't valid")

    if not '_flashes' in session:
        try:
            login_query = 'SELECT * FROM users WHERE email = :email'
            login_data = {'email': email}
            user = mysql.query_db(login_query, login_data)
            hashed = user[0]['password']

            print "<<< about to test password vs hash >>>", hashed, password
            it_worked = bcrypt.check_password_hash(hashed, password)
            print "login success:", it_worked
        except:
            flash('invalid username or password')
            it_worked = False

        if it_worked:
            session['id'] = user[0]['id']
            return redirect('/success')

    return redirect('/')

app.run(debug=True)
