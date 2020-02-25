from flask import Flask, render_template
from flask import request, redirect
from db_connector.db_connector import connect_to_database, execute_query

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("layouts/main.html",
                           body="<i>Are you looking for /teams, /games, /players, /penalties, or /infractions ?</i>")


@app.route('/teams', methods=['POST', 'GET'])
def teams():
    print("Querying the database for Teams")
    db_connection = connect_to_database()

    if request.method == 'GET':
        query = "SELECT team_id, team_name FROM teams;"
        result = execute_query(db_connection, query)
        return render_template("layouts/main.html",
                               body=render_template("teams.html", rows=result))
    elif request.method == 'POST':
        print("Adding some new team!")
        query = "SELECT team_id, team_name FROM teams;"
        result = execute_query(db_connection, query)
        return render_template("layouts/main.html",
                               body=render_template("teams.html", rows=result))


@app.route('/games', methods=['POST', 'GET'])
def games():
    print("Querying database for Games")
    db_connection = connect_to_database()

    if request.method == 'GET':
        query = "SELECT game_id, home_id, away_id, game_date, game_time FROM games;"
        result = execute_query(db_connection, query)
        return render_template("layouts/main.html",
                               body=render_template("games.html", rows=result))
    elif request.method == 'POST':
        print("Adding some new game!")
        query = "SELECT game_id, home_id, away_id, game_date, game_time FROM games;"
        result = execute_query(db_connection, query)
        return render_template("layouts/main.html",
                               body=render_template("games.html", rows=result))


@app.route('/players', methods=['POST', 'GET'])
def players():
    print("Querying database for Players")
    db_connection = connect_to_database()

    if request.method == 'GET':
        query = "SELECT player_id, fname, lname, number FROM players;"
        result = execute_query(db_connection, query)
        return render_template("layouts/main.html",
                               body=render_template("players.html", rows=result))
    elif request.method == 'POST':
        print("Adding some new player!")
        query = "SELECT player_id, fname, lname, number FROM players;"
        result = execute_query(db_connection, query)
        return render_template("layouts/main.html",
                               body=render_template("players.html", rows=result))


@app.route('/penalties', methods=['POST', 'GET'])
def penalties():
    print("Querying database for Penalties")
    db_connection = connect_to_database()

    if request.method == 'GET':
        query = "SELECT penalty_id, type FROM penalties;"
        result = execute_query(db_connection, query)
        return render_template("layouts/main.html",
                               body=render_template("penalties.html", rows=result))
    elif request.method == 'POST':
        print("Adding some new penalty!")
        query = "SELECT penalty_id, type FROM penalties;"
        result = execute_query(db_connection, query)
        return render_template("layouts/main.html",
                               body=render_template("penalties.html", rows=result))


@app.route('/infractions', methods=['POST', 'GET'])
def infractions():
    print("Querying database for Infractions")
    db_connection = connect_to_database()

    if request.method == 'GET':
        query = "SELECT infraction_id, player_id, penalty_id FROM infractions;"
        result = execute_query(db_connection, query)
        return render_template("layouts/main.html",
                               body=render_template("infractions.html", rows=result))
    elif request.method == 'POST':
        print("Adding some new infraction!")
        query = "SELECT infraction_id, player_id, penalty_id FROM infractions;"
        result = execute_query(db_connection, query)
        return render_template("layouts/main.html",
                               body=render_template("infractions.html", rows=result))
