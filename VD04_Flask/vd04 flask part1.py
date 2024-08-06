from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/nothome/')
def nothome():
    return render_template('vinni.html')


if __name__ == '__main__':
    app.run(debug=True)
