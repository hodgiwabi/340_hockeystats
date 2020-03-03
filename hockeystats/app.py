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
        # req = request.form["submit"]
        # if req and req == "search":
        #     team_name = request.form['searchTeam']
        #     data = [team_name]
        #     query = "SELECT team_name FROM teams WHERE team_name = '%s';"
        #     result = execute_query(db_connection, query, data)
        #     return render_template("layouts/main.html",
        #                            body=render_template("teams.html", rows=result))
        # else:
        teamName = request.form['teamName']
        data = [teamName]
        query = 'INSERT INTO teams (team_name) VALUES (%s);'
        execute_query(db_connection, query, data)
        return render_template("layouts/main.html", 
                            body=render_template("posts/team_post.html", teamName=teamName))


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
        home_id = request.form['teamAdd1']
        away_id = request.form['teamAdd2']
        game_date = request.form['addDate']
        date = game_date.split('T')
        game_date = date[0]
        game_time = date[1]
        query = "INSERT INTO games (home_id, away_id, game_date, game_time) VALUES (%s, %s, %s, %s);"
        data = [home_id, away_id, game_date, game_time]
        execute_query(db_connection, query, data)
        return render_template("layouts/main.html",
                               body=render_template("posts/game_post.html", data=data))


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
        print(request.form)
        req = request.form["search"]
        print(req)
        if req and req == "search":
            print("we got here")
            number = request.form["searchPlayer"]
            query = "SELECT player_id, fname, lname, number FROM players WHERE number = %s;"
            data = [number]
            result = execute_query(db_connection, query, data)
            return render_template("layouts/main.html",
                                body=render_template("players.html", rows=result))
        elif req == "add":
            fname = request.form['playerFirstName']
            lname = request.form['playerLastName']
            number = request.form['playerNumber']
            team_id = request.form['playerTeam']

            query = "INSERT INTO players (fname, lname, number, team_id) VALUES (%s, %s, %s, %s);"
            data = [fname, lname, number, team_id]
            execute_query(db_connection, query, data)
            return render_template("layouts/main.html",
                                body=render_template("posts/player_post.html", data=data))


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
        ptype = request.form['penaltyType']
        data = [ptype]
        query = "INSERT INTO penalties (type) VALUES (%s);"
        execute_query(db_connection, query, data)
        return render_template("layouts/main.html",
                               body=render_template("posts/penalty_post.html", data=data))


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
        player_id = request.form['infractionPlayerID']
        penalty_id = request.form['infractionPenaltyIDs']
        data = [player_id, penalty_id]
        query = "INSERT INTO infractions (player_id, penalty_id) VALUES (%s, %s);"
        execute_query(db_connection, query, data)
        return render_template("layouts/main.html",
                               body=render_template("posts/infraction_post.html", data=data))
