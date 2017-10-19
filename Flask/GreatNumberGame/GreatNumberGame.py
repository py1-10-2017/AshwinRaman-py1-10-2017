from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = "thisissecret"

@app.route('/')
def index():
    if 'target' not in session:
        session['target'] = random.randint(1,100)
    return render_template('index.html')

@app.route('/guess', methods=["POST"])
def guess():
    if session['target'] == int(request.form['guess']):
        session['result'] = 'correct'

    elif session['target'] < int(request.form['guess']):
        session['result'] = 'high'

    else:
        session['result'] = 'low'

    return redirect('/')

@app.route('/reset')
def reset():
    session.pop('target')
    session.pop('result')
    return redirect('/')

app.run(debug=True)
