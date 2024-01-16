from flask import Flask, render_template, request, redirect, url_for
import random, hashlib

app = Flask(__name__)

@app.route("/") 
def index():
    return render_template("index.html")

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['input_name']
    return redirect(url_for('results', name=name))
    

@app.route('/results')
def results():
    #Hardcoded my name because obviously I'm a fan of the commanders
    names = ['Greg', 'Greg Mihokovich']
    teams = ['Arizona Cardinals', 'Baltimore Ravens', 'Atlanta Falcons', 'Buffalo Bills', 'Carolina Panthers', 'Cincinatti Bengals', 'Chicago Bears', 'Cleveland Browns', 'Dallas Cowgirls', 'Denver Broncos', 'Detroit Lions', 'Houston Texans', 'Greenbay Packers', 'Indianapolis Colts', 'Los Angeles Rams', 'Jacksonville Jaguars', 'Minnesota Vikings', 'Kansas City Chiefs', 'New Orleans Saints', 'Las Vegas Raiders', 'New York Giants', 'Los Angeles Chargers', 'Filthadelphia Eagles', 'Miami Dolphins', 'San Francisco 49ers', 'New England Patriots', 'Seattle Seahawks', 'New York Jets', 'Tampa Bay Buccaneers', 'Pittsburgh Steelers', 'Washington Commanders', 'Tennessee Titans']
    name = request.args.get('name')
    md5_hash = hashlib.md5(name.encode()).hexdigest()
    team_index = int(md5_hash, 16) % 32
    team = teams[team_index]
    if name in names:
        return render_template('results.html', name=name, team='Washington Commanders')
    else:
        return render_template('results.html', name=name, team=team)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
