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


    return render_template('about.html', )

@app.route('/perila/')
def perila():

    return render_template('perila.html')

if __name__ == '__main__':
    app.run(debug=True)
