from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'very secret'


@app.route('/')
def counter():
    try:
        session['counter'] += 1
    except:
        session['counter'] = 1
    print counter
    return render_template('index.html')

@app.route('/add2', methods=['POST'])
def increment2():
    session['counter'] += 1
    print session['counter']
    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    session['counter'] = 0
    return redirect('/')

app.run(debug=True)
