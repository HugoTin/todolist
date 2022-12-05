from flask import Flask, render_template, request, redirect
import json

app = Flask(__name__)

@app.route("/", methods=["POST","GET"])
def home():
    #template/home.html
    with open("app.json", "r") as f:
        tasks = json.load(f)
    return render_template('home.html', tasks=tasks)



@app.route("/create", methods=["POST"])
def create():
    name = request.form['name'].upper()
    status = request.form['status']

    try:
        if request.form['platinum'] == "on":
            platinum = True
    except:
        platinum = False

    task = {
        "name" :  name,
        "platinum": platinum,
        "status": status
    }

    with open("app.json") as f:
        tasks = json.load(f)

    tasks.append(task)

    with open("app.json", 'w') as f:
        json.dump(tasks, f, indent = 2)
    
    return redirect('/')

@app.route("/excluir", methods=["POST"])
def excluir():
    name = request.form['task'].upper()
    with open("app.json") as f:
        tasks = json.load(f)

    for x, task in enumerate(tasks):
        if task["name"] == name:
            tasks.pop(x)

    with open("app.json", 'w') as f:
        json.dump(tasks, f, indent = 2)
    
    return redirect('/')

@app.route("/add", methods=["POST"])
def add():
    with open("app.json") as f:
        tasks = json.load(f)
    return render_template('addgame.html')

app.run(debug=True)