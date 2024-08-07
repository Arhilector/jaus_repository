from flask import render_template, request, redirect, url_for

from . import app

posts= []

@app.route('/', methods=['GET', 'POST']) #декоратор для обработки GET-запросов

def index():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        posts.append({'title': title, 'content': content})
        return redirect(url_for('index'))
    return render_template('Index.html', posts=posts)

