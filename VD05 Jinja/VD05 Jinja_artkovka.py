from flask import Flask, render_template

app = Flask(__name__)




@app.route('/')
def home():
    return render_template('home.html', link = "Узнать подробнее")




@app.route('/base/')
def nothome():
    context = {
        "caption": "Шаблон",

    }
    return render_template('base.html', **context)



@app.route('/about/')
def about():
    context = {
        "caption": "кованые перила"

    }
    return render_template('about.html', **context)

@app.route('/perila/')
def perila():
    context = {
        "caption": "Кованые перила"
    }
    return render_template('perila.html', **context)

if __name__ == '__main__':
    app.run(debug=True)
