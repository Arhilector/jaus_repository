from flask import render_template, request
from . import app

@app.route('/', methods=['GET', 'POST'])
def index():
    user_data = None
    if request.method == 'POST':
        user_data = {
            'name': request.form['name'],
            'city': request.form['city'],
            'hobby': request.form['hobby'],
            'age': request.form['age']
        }
    return render_template('index.html', user_data=user_data)