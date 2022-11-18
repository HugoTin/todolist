from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    #template/home.html
    return render_template('home.html')

@app.route("/test")
def test():
    #template/home.html
    return render_template('test.html')

@app.route("/bye")
def bye():
    return 'Bye'

app.run(debug = True)