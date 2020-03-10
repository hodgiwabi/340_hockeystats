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
        if "searchTeam" in request.args:
            team_name = request.args['searchTeam']
            data = [team_name]
            query = "SELECT team_name FROM teams WHERE team_name = %s;"
            result = execute_query(db_connection, query, data)
        else:
            query = "SELECT team_id, team_name FROM teams;"
            result = execute_query(db_connection, query)

        return render_template("layouts/main.html",
            body=render_template("teams.html", rows=result))
    elif request.method == 'POST':
        req = request.form["action"]
        if req == "add":
            teamName = request.form['teamName']
            data = [teamName]
            query = 'INSERT INTO teams (team_name) VALUES (%s);'
            execute_query(db_connection, query, data)
            return render_template("layouts/main.html",
                                   body=render_template("posts/team_post.html", teamName=teamName))
        elif req == "update":
            tn = request.form["teamUpdateName"]
            tid = request.form["teamID"]

            query = "UPDATE team SET team_name= %s WHERE team_id= %s;"
            data = [tn, tid]
            execute_query(db_connection, query, data)
            msg = "Successfully updated Team: {0}. New Name: {1}".format(tn, tid)
        elif req == "remove":
            tid = request.form["teamID"]
            query = "DELETE FROM team WHERE team_id= %s"
            data = [tid]
            execute_query(db_connection, query, data)
            msg = "Successfully removed Team: {0}".format(tid)
        else:
            msg = "Invalid call (missing add/update/remove)"

        return render_template("layouts/main.html",
                               body=render_template("posts/post_message.html", message=msg))


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
        req = request.form["action"]
        if req == "add":
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
        elif req == "update":
            gid = request.form["gameID"]
            tid1 = request.form["teamUpdate1"]
            tid2 = request.form["teamUpdate2"]

            query = "UPDATE games SET home_id= %s, away_id= %s WHERE game_id= %s"
            data = [tid1, tid2, gid]
            execute_query(db_connection, query, data)
            msg = "Successfully updated Game: {0}. New Teams: {1} vs {2}".format(gid, tid1, tid2)
        elif req == "remove":
            gid = request.form["gameID"]
            query = "DELETE FROM teams WHERE team_id= %s"
            data = [gid]
            execute_query(db_connection, query, data)
            msg = "Successfully removed Game: {0}".format(gid)
        else:
            msg = "Invalid call (missing add/update/remove)"

        return render_template("layouts/main.html",
                               body=render_template("posts/post_message.html", message=msg))


@app.route('/players', methods=['POST', 'GET'])
def players():
    print("Querying database for Players")
    db_connection = connect_to_database()

    if request.method == 'GET':
        if "searchPlayer" in request.args:
            number = request.args["searchPlayer"]
            query = "SELECT player_id, fname, lname, number FROM players WHERE number = %s;"
            data = [number]
            result = execute_query(db_connection, query, data)
        else:
            query = "SELECT player_id, fname, lname, number FROM players;"
            result = execute_query(db_connection, query)
        
        return render_template("layouts/main.html",
                                body=render_template("players.html", rows=result))
    elif request.method == 'POST':
        req = request.form["action"]
        if req == "add":
            fname = request.form['playerFirstName']
            lname = request.form['playerLastName']
            number = request.form['playerNumber']
            team_id = request.form['playerTeam']

            query = "INSERT INTO players (fname, lname, number, team_id) VALUES (%s, %s, %s, %s);"
            data = [fname, lname, number, team_id]
            execute_query(db_connection, query, data)
            msg = "Successfully Added: {0} {1}, #{2} on Team {3}".format(fname, lname, number, team_id)
        elif req == "update":
            pid = request.form["playerID"]
            tid = request.form["playerUpdateTeamID"]

            query = "UPDATE players SET team_id= %s WHERE player_id= %s;"
            data = [tid, pid]
            execute_query(db_connection, query, data)
            msg = "Successfully updated Player: {0}. New Team: {1}".format(pid, tid)
        elif req == "remove":
            pid = request.form["playerID"]
            query = "DELETE FROM players WHERE player_id= %s"
            data = [pid]
            execute_query(db_connection, query, data)
            msg = "Successfully removed Player: {0}".format(pid)
        else:
            msg = "Invalid call (missing add/update/remove)"

        return render_template("layouts/main.html",
                               body=render_template("posts/post_message.html", message=msg))


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

    elif request.method == 'POST':
        req = request.form["action"]
        if req == "add":
            fname = request.form['playerFirstName']
            lname = request.form['playerLastName']
            number = request.form['playerNumber']
            team_id = request.form['playerTeam']

            query = "INSERT INTO players (fname, lname, number, team_id) VALUES (%s, %s, %s, %s);"
            data = [fname, lname, number, team_id]
            execute_query(db_connection, query, data)
            msg = "Successfully Added: {0} {1}, #{2} on Team {3}".format(fname, lname, number, team_id)
        elif req == "update":
            pid = request.form["playerID"]
            tid = request.form["playerUpdateTeamID"]

            query = "UPDATE players SET team_id= %s WHERE player_id= %s;"
            data = [tid, pid]
            execute_query(db_connection, query, data)
            msg = "Successfully updated Player: {0}. New Team: {1}".format(pid, tid)
        elif req == "remove":
            pid = request.form["playerID"]
            query = "DELETE FROM players WHERE player_id= %s"
            data = [pid]
            execute_query(db_connection, query, data)
            msg = "Successfully removed Player: {0}".format(pid)
        else:
            msg = "Invalid call (missing add/update/remove)"

        return render_template("layouts/main.html",
                               body=render_template("posts/post_message.html", message=msg))


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
        req = request.form["action"]
        if req == "add":
            player_id = request.form['infractionPlayerID']
            penalty_id = request.form['infractionPenaltyIDs']
            data = [player_id, penalty_id]
            query = "INSERT INTO infractions (player_id, penalty_id) VALUES (%s, %s);"
            execute_query(db_connection, query, data)
            msg = "Successfully Added Infraction. Player {0} contains penality {1}".format(player_id, penality_id)
        elif req == "update":
            inf_id = request.form["infractionID"]
            pen_id = request.form["infractionUpdatePenalty"]

            query = "UPDATE infractions SET penalty_id = %s WHERE infraction_id = %s;"
            data = [inf_id, pen_id]
            execute_query(db_connection, query, data)
            msg = "Successfully updated Player: {0}. New Team: {1}".format(pid, tid)
        elif req == "remove":
            pid = request.form["playerID"]
            query = "DELETE FROM players WHERE player_id= %s"
            data = [pid]
            execute_query(db_connection, query, data)
            msg = "Successfully removed Player: {0}".format(pid)
        else:
            msg = "Invalid call (missing add/update/remove)"

        return render_template("layouts/main.html",
                               body=render_template("posts/post_message.html", message=msg))