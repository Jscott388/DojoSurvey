from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key = '\xb8?\xff\xd4\x1a\xdf\x11\xeaiP2[\x8cs\x1d\x17\x9d\xc5\xcf\x7f\xbb\xf0P\xd3'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create', methods=['POST'])
def create_user():
    if len(request.form['name']) < 1:
        flash("Name cannot be empty!")
        return redirect('/')
    if len(request.form['comment']) > 120:
        flash("Your comment is too long! Must be under 120 characters")
        return redirect('/')
    if len(request.form['comment']) < 1:
        flash("Please enter a comment!")
        return redirect('/')
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    return redirect('/show')

@app.route('/show')
def show_user():
    return render_template('results.html')

app.run(debug=True)
