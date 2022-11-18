from flask import Flask, render_template, request
import json

app = Flask(__name__)

@app.route("/")
def home():
    #template/home.html
    with open("app.json") as f:
        tasks = json.load(f)
    return render_template('home.html', tasks=tasks)

@app.route("/create", methods=["POST"])
def create():
    name = request.form['name']
    task = {
        "name" :  name,
        "finished": False
    }
    with open("app.json") as f:
        tasks = json.load(f)

    tasks.append(task)

    with open("app.json", 'w') as f:
        json.dump(tasks, f, indent = 2)
    
    return home()


app.run(debug = True)