from flask import Flask, render_template
from flask import request
from db_connector.db_connector import connect_to_database, execute_query
from MySQLdb import DatabaseError, Error, IntegrityError, InternalError, MySQLError

app = Flask(__name__)


def run_query(query, data, q=True, sel="", msg="", html_path=""):
    try:
        db_connection = connect_to_database()
        result = execute_query(db_connection, query, data)
        if q:
            if sel:
                select = execute_query(db_connection, sel, [])
                return render_template("layouts/main.html",
                                   body=render_template(html_path, rows=result, data=select))

            return render_template("layouts/main.html",
                                   body=render_template(html_path, rows=result))
    except (DatabaseError, Error, IntegrityError, InternalError, MySQLError) as err:
        msg = err

    return render_template("layouts/main.html",
                           body=render_template("posts/post_message.html", message=msg))


@app.route('/')
def index():
    return render_template("layouts/main.html",
                           body="<i>Are you looking for /teams, /games, /players, /penalties, or /infractions ?</i>")


@app.route('/teams', methods=['POST', 'GET'])
def teams():
    print("Querying the database for Teams")

    if request.method == 'GET':
        if "searchTeam" in request.args:
            team_name = request.args['searchTeam']
            data = [team_name]
            query = "SELECT team_name FROM teams WHERE team_name = %s;"
        else:
            query = "SELECT team_id, team_name FROM teams;"
            data = []
        
        return run_query(query, data, html_path="teams.html")

    elif request.method == 'POST':
        req = request.form["action"]
        if req == "add":
            team_name = request.form['teamName']
            data = [team_name]
            query = 'INSERT INTO teams (team_name) VALUES (%s);'
            msg = "Successfully added Team: {0}".format(team_name)
        elif req == "update":
            tn = request.form["teamUpdateName"]
            tid = request.form["teamID"]

            query = "UPDATE teams SET team_name= %s WHERE team_id= %s;"
            data = [tn, tid]
            msg = "Successfully updated Team: {0}. New Name: {1}".format(tid, tn)
        elif req == "remove":
            tid = request.form["teamID"]
            query = "DELETE FROM teams WHERE team_id= %s;"
            data = [tid]
            msg = "Successfully removed Team: {0}".format(tid)
        else:
            query = ""
            data = []
            msg = "Invalid call (missing add/update/remove)"

        return run_query(query, data, q=False, msg=msg)


@app.route('/games', methods=['POST', 'GET'])
def games():
    print("Querying database for Games")

    if request.method == 'GET':
        query = """
SELECT home.game_id, home.team_name, away.team_name, home.game_date, home.game_time FROM
    (
        SELECT game_id, t.team_name, game_date, game_time  FROM games
        JOIN teams t on games.home_id = t.team_id
    ) AS home
    JOIN
    (
        SELECT game_id, t.team_name FROM games
        JOIN teams t on games.away_id = t.team_id
    ) AS away
    WHERE home.game_id = away.game_id;"""

        select = "SELECT team_id, team_name FROM teams;"
  
        return run_query(query, [], sel=select, html_path="games.html")

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
            msg = "Successfully added Game: {0} vs {1} at {2} on {3}".format(home_id, away_id, game_time, game_date)
        elif req == "update":
            gid = request.form["gameID"]
            tid1 = request.form["teamUpdate1"]
            tid2 = request.form["teamUpdate2"]

            query = "UPDATE games SET home_id= %s, away_id= %s WHERE game_id= %s"
            data = [tid1, tid2, gid]
            msg = "Successfully updated Game: {0}. New Teams: {1} vs {2}".format(gid, tid1, tid2)
        elif req == "remove":
            gid = request.form["gameID"]
            query = "DELETE FROM games WHERE game_id= %s"
            data = [gid]
            msg = "Successfully removed Game: {0}".format(gid)
        else:
            query = ""
            data = []
            msg = "Invalid call (missing add/update/remove)"

        return run_query(query, data, q=False, msg=msg)


@app.route('/players', methods=['POST', 'GET'])
def players():
    print("Querying database for Players")

    if request.method == 'GET':
        if "searchPlayer" in request.args:
            number = request.args["searchPlayer"]
            query = "SELECT player_id, fname, lname, number FROM players WHERE number = %s;"
            data = [number]
        else:
            query = "SELECT player_id, fname, lname, number FROM players;"
            data = []
        
        return run_query(query, data, html_path="players.html")

    elif request.method == 'POST':
        req = request.form["action"]
        if req == "add":
            fname = request.form['playerFirstName']
            lname = request.form['playerLastName']
            number = request.form['playerNumber']
            team_id = request.form['playerTeam']

            query = "INSERT INTO players (fname, lname, number, team_id) VALUES (%s, %s, %s, %s);"
            data = [fname, lname, number, team_id]
            msg = "Successfully Added: {0} {1}, #{2} on Team {3}".format(fname, lname, number, team_id)
        elif req == "update":
            pid = request.form["playerID"]
            tid = request.form["playerUpdateTeamID"]

            query = "UPDATE players SET team_id= %s WHERE player_id= %s;"
            data = [tid, pid]
            msg = "Successfully updated Player: {0}. New Team: {1}".format(pid, tid)
        elif req == "remove":
            pid = request.form["playerID"]
            query = "DELETE FROM players WHERE player_id= %s"
            data = [pid]
            msg = "Successfully removed Player: {0}".format(pid)
        else:
            query = ""
            data = []
            msg = "Invalid call (missing add/update/remove)"

        return run_query(query, data, q=False, msg=msg)


@app.route('/penalties', methods=['POST', 'GET'])
def penalties():
    print("Querying database for Penalties")

    if request.method == 'GET':
        query = "SELECT penalty_id, type FROM penalties;"

        return run_query(query, [], html_path="penalties.html")

    elif request.method == 'POST':
        req = request.form["action"]
        if req == "add":
            ptype = request.form['penaltyType']
            data = [ptype]
            query = "INSERT INTO penalties (type) VALUES (%s);"
            msg = "Successfully Added Penalty: {0}".format(ptype)
        elif req == "update":
            pen_id = request.form["penaltyID"]
            pen_type = request.form["penaltyUpdateType"]

            query = "UPDATE penalties SET type = %s WHERE penalty_id = %s;"
            data = [pen_type, pen_id]
            msg = "Successfully updated Penalty: {0}. New Type: {1}".format(pen_id, pen_type)
        elif req == "remove":
            pid = request.form["penaltyID"]
            query = "DELETE FROM penalties WHERE penalty_id = %s;"
            data = [pid]
            msg = "Successfully removed Penalty: {0}".format(pid)
        else:
            query = ""
            data = []
            msg = "Invalid call (missing add/update/remove)"

        return run_query(query, data, q=False, msg=msg)


@app.route('/infractions', methods=['POST', 'GET'])
def infractions():
    print("Querying database for Infractions")

    if request.method == 'GET':
        query = "SELECT infraction_id, player_id, penalty_id FROM infractions;"

        return run_query(query, [], html_path="infractions.html")

    elif request.method == 'POST':
        req = request.form["action"]
        if req == "add":
            player_id = request.form['infractionPlayerID']
            penalty_id = request.form['infractionPenaltyIDs']
            data = [player_id, penalty_id]
            query = "INSERT INTO infractions (player_id, penalty_id) VALUES (%s, %s);"
            msg = "Successfully Added Infraction. Player {0} contains penality {1}".format(player_id, penalty_id)
        elif req == "update":
            inf_id = request.form["infractionID"]
            pen_id = request.form["infractionUpdatePenalty"]

            query = "UPDATE infractions SET penalty_id = %s WHERE infraction_id = %s;"
            data = [pen_id, inf_id]
            msg = "Successfully updated Infraction: {0}. New Penalty: {1}".format(inf_id, pen_id)
        elif req == "remove":
            inf_id = request.form["infractionID"]
            query = "DELETE FROM infractions WHERE infraction_id = %s"
            data = [inf_id]
            msg = "Successfully removed Infraction: {0}".format(inf_id)
        else:
            query = ""
            data = []
            msg = "Invalid call (missing add/update/remove)"

        return run_query(query, data, q=False, msg=msg)
