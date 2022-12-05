@app.route('/create', methods=['POST'])
def create():
    name = request.form['name']
    musica = {'name' : name, 'finished': False}


    with ("app.json", "r") as f:
        musicas = json.load(f)

    musicas.append(musica)

    with ("app.json", "w") as f:
        json.dump(musicas, f, indent = 2)

    return redirect(url_for('home'))