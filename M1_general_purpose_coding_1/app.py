from flask import Flask, render_template
import csv

# ensure file is called app.py

app = Flask(__name__)

@app.route("/hello")
def hello_world():
    return "Hello World"

@app.route("/films/list")
def film_list():
    films = []
    with open("film_stars.csv", "r+") as film_ratings:
        film = csv.DictReader(film_ratings, delimiter=',')
        for row in film:
            films.append(row)
    return render_template('film_list.html', films=films)