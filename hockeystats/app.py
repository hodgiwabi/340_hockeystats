from flask import Flask, render_template
from db_connector.db_connector import connect_to_database, execute_query

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("layouts/main.html",
                           body="<i>Are you looking for /teams, /games, /players, /penalties, or /infractions ?")


@app.route('/teams')
def teams():
    print("Querying the database for Teams")
    db_connection = connect_to_database()
    query = "SELECT team_name FROM teams;"
    result = execute_query(db_connection, query)
    return render_template("layouts/main.html",
                           body=render_template("teams.html", rows=result))


@app.route('/games')
def games():
    print("Querying database for Games")
    db_connection = connect_to_database()
    query = "SELECT home_id, away_id, game_date, game_time FROM games;"
    result = execute_query(db_connection, query)
    return render_template("layouts/main.html",
                           body=render_template("games.html", rows=result))


@app.route('/players')
def players():
    print("Querying database for Players")
    db_connection = connect_to_database()
    query = "SELECT fname, lname, number FROM players;"
    result = execute_query(db_connection, query)
    return render_template("layouts/main.html",
                           body=render_template("players.html", rows=result))


@app.route('/penalties')
def penalties():
    print("Querying database for Penalties")
    db_connection = connect_to_database()
    query = "SELECT type FROM penalties;"
    result = execute_query(db_connection, query)
    return render_template("layouts/main.html",
                           body=render_template("penalties.html", rows=result))


@app.route('/infractions')
def infractions():
    print("Querying database for Infractions")
    db_connection = connect_to_database()
    query = "SELECT player_id, penalty_id FROM infractions;"
    result = execute_query(db_connection, query)
    return render_template("layouts/main.html",
                           body=render_template("infractions.html", rows=result))
