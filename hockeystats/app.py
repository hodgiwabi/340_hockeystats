from flask import Flask, render_template
from db_connector.db_connector import connect_to_database, execute_query

app = Flask(__name__)

@app.route('/')
def index():
    return "<i>Are you looking for /teams, /games, /players, /penalties ?</i>"

@app.route('/teams')
def teams():
    print("Querying the database for Teams")
    db_connection = connect_to_database()
    query = "SELECT teamName FROM teams;"
    result = execute_query(db_connection, query)
    return render_template("layouts/main.html",
                           navbar=render_template("layouts/navbar.html"),
                           body=render_template("teams.html", rows=result))

@app.route('/games')
def games():
    print("Querying database for Games")
    db_connection = connect_to_database()
    query = "SELECT homeTeamID, awayTeamID, gameDate, gameTime FROM games;"
    result = execute_query(db_connection, query)
    return render_template("layouts/main.html",
                           navbar=render_template("layouts/navbar.html"),
                           body=render_template("games.html", rows=result))

@app.route('/players')
def players():
    print("Querying database for Players")
    db_connection = connect_to_database()
    query = "SELECT playerFName, playerLName, playerNumber FROM players;"
    result = execute_query(db_connection, query)
    return render_template("layouts/main.html",
                           navbar=render_template("layouts/navbar.html"),
                           body=render_template("players.html", rows=result))

@app.route('/penalties')
def penalties():
    print("Querying database for Penalties")
    db_connection = connect_to_database()
    query = "SELECT penaltyType FROM penalties;"
    result = execute_query(db_connection, query)
    return render_template("layouts/main.html",
                           navbar=render_template("layouts/navbar.html"),
                           body=render_template("penalties.html", rows=result))
