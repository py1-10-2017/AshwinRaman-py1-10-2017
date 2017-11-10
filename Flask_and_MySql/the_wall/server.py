
from flask import Flask, request, render_template, redirect, session, flash
from mysqlconnection import MySQLConnector
import re
from flask_bcrypt import Bcrypt


app = Flask(__name__)
app.secret_key = "secreeettt"
mysql = MySQLConnector(app, 'wall')
bcrypt = Bcrypt(app)

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')


@app.route('/')
def index():
    get_all_query = "SELECT * FROM users"
    users = mysql.query_db(get_all_query)
    return render_template('index.html', users=users)


@app.route('/register', methods=['POST'])
def register():
    errors = []

    if len(request.form['first_name']) < 2:
        errors.append('First name must be at least 2 characters long')
    elif not request.form['first_name'].isalpha():
        errors.append('First name must contain only letters')

    if len(request.form['last_name']) < 2:
        errors.append('Last name must be at least 2 characters long')
    elif not request.form['last_name'].isalpha():
        errors.append('Last name must contain only letters')

    if not EMAIL_REGEX.match(request.form['email']):
        errors.append('Email must be valid')

    if not len(request.form['password']) >= 8:
        errors.append('Password must be at least 8 characters')
    elif not request.form['confirm_password'] == request.form['password']:
        errors.append('Password and confirm password must match exactly')

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
        register_query = """INSERT INTO users
        (first_name, last_name, email, password, created_at, updated_at)
        VALUES
        (:first_name, :last_name, :email, :password, NOW(), NOW())
        """
        new_user_id = mysql.query_db(register_query, user_data)
        if new_user_id is not 0:
            session['id'] = new_user_id
        else:
            flash('Failed to create user')
        return redirect('/wall')

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']

    if not re.match(EMAIL_REGEX,email):
        flash('Email is not valid')

    if not len(password) > 7:
        flash("Password is not valid")

    if not '_flashes' in session:
        try:
            login_query = 'SELECT * FROM users WHERE email = :email'
            login_data = {'email': email}
            user = mysql.query_db(login_query, login_data)[0]
            hashed = user['password']
            it_worked = bcrypt.check_password_hash(hashed, password)
        except:
            flash('Invalid username or password')
            it_worked = False

        if it_worked:
            session['id'] = user['id']
            flash("Welcome {}".format(user['first_name']), category="success")
            return redirect('/wall')

    return redirect('/')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

@app.route('/wall')
def wall():
    get_messages_query = "SELECT messages.message, messages.id, first_name, last_name, messages.created_at FROM messages\
                          JOIN users ON messages.id=user_id"
    messages = mysql.query_db(get_messages_query)

    get_comments_query = "SELECT comments.comment, message_id, comments.created_at, first_name, last_name FROM comments\
                          JOIN messages ON messages.id=comments.message_id\
                          JOIN users ON users.id=comments.user_id"
    comments = mysql.query_db(get_comments_query)
    print comments
    if 'id' not in session:
        return redirect('/')
    return render_template('wall.html', messages=messages, comments=comments)

@app.route('/post_message', methods=['POST'])
def create_message():
    new_message_query = "INSERT INTO messages (user_id, message, created_at, updated_at)\
                         VALUES (:user_id, :message, NOW(), NOW())"
    new_message_data = {
        "user_id": int(session['id']),
        "message": request.form['message']
    }
    mysql.query_db(new_message_query, new_message_data)
    return redirect('/wall')

@app.route('/post_comment/<message_id>', methods=['POST'])
def create_comment(message_id):
    new_comment_query = "INSERT INTO comments (user_id, message_id, comment, created_at, updated_at)\
                         VALUES (:user_id, :message_id, :comment, NOW(), NOW())"
    new_comment_data = {
        "user_id": session['id'],
        "message_id": message_id,
        "comment": request.form["comment"]
    }
    mysql.query_db(new_comment_query, new_comment_data)
    return redirect('/wall')


app.run(debug=True)
