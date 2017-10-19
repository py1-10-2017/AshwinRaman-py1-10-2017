from flask import Flask, render_template, request, flash
app = Flask(__name__)

app.secret_key = 'KeepItSecretKeepItSafe'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=["POST"])
def result():
    name = request.form['name']
    location = request.form['location']
    language = request.form['language']
    comment = request.form['comment']

    if len(request.form['name']) < 1:
        flash("Name cannot be empty!")
    else:
        flash("Success! Your name is {}".format(request.form['name']))

    if len(request.form['comment']) < 1:
        flash("Comment field cannot be empty!")
    elif len(request.form['comment']) > 120:
        flash("Comment field cannot contain more than 120 characters!")
    else:
        flash("Success! Thanks for your comment!")


    return render_template('result.html', name=name, location=location, language=language, comment=comment)

app.run(debug=True)
