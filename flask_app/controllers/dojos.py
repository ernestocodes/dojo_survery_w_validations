from flask_app import app
from flask import redirect, render_template, request, session
from flask_app.models.dojo import Dojo

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create/survey', methods = ['POST'])
def create():
    if not Dojo.validate(request.form):
        return redirect('/')
    Dojo.create(request.form)
    return redirect('/result')

@app.route('/result')
def result():
    dojo = Dojo.get_most_recent()
    return render_template('result.html', dojo = dojo)
