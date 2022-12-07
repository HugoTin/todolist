from flask import Flask, render_template, request, redirect
import json

app = Flask(__name__)

@app.route("/", methods=["POST","GET"])
def home():
    with open("app.json", "r") as f:
        games = json.load(f)
    return render_template('home.html', games=games)

@app.route("/edit", methods=["POST","GET"])
def edit():
    game_id = int(request.form['id'])
    with open("app.json", "r") as f:
        games = json.load(f)
    for x, game in enumerate(games):
        if game["id"] == game_id:
            games = game
    return render_template('edit.html', games=games)

@app.route("/editar", methods=["POST","GET"])
def editar():
    name = request.form['name'].upper()
    status = request.form['status']

    try:
        if request.form['platinum'] == "on":
            platinum = True
    except:
        platinum = False

    game_id = int(request.form['id'])

    with open("app.json", "r") as f:
        games = json.load(f)
    for x, game in enumerate(games):
        if game["id"] == game_id:
            list_id = x

    games[list_id] = {
        "id": int(game_id),
        "name" :  name,
        "platinum": platinum,
        "status": status
    }

    with open("app.json", 'w') as f:
        json.dump(games, f, indent = 2)
    
    return redirect('/')

    return redirect('/')    

@app.route("/create", methods=["POST"])
def create():
    name = request.form['name'].upper()
    status = request.form['status']

    try:
        if request.form['platinum'] == "on":
            platinum = True
    except:
        platinum = False

    

    with open("app.json") as f:
        games = json.load(f)

    game_id = int(games[-1]["id"]) + 1

    game = {
        "id": int(game_id),
        "name" :  name,
        "platinum": platinum,
        "status": status
    }
    games.append(game)

    with open("app.json", 'w') as f:
        json.dump(games, f, indent = 2)
    
    return redirect('/')

@app.route("/excluir", methods=["POST"])
def excluir():
    game_id = int(request.form['id'])
    with open("app.json") as f:
        games = json.load(f)

    for x, game in enumerate(games):
        if game["id"] == game_id:
            games.pop(x)

    with open("app.json", 'w') as f:
        json.dump(games, f, indent = 2)
    
    return redirect('/')

@app.route("/add", methods=["POST"])
def add():
    with open("app.json") as f:
        tasks = json.load(f)
    return render_template('addgame.html')

app.run(debug=True)