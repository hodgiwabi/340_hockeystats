from flask import Flask, render_template
from jinja2 import Environment, PackageLoader, select_autoescape
from db_connector.db_connector import connect_to_database, execute_query

app = Flask(name)

env = Environment(
    loader=PackageLoader('340_hockeystats', 'templates'),
    autoescape=select_autoescape(['html', 'xml'])
)

# main = env.get_template("index.html")

#the route is what you will type in browser
@app.route('/hello')
#the name of this function is just a cosmetic thing
def hello():
    #this is the output returned to browser
    return "Hello world!"

@app.route('/')
def index():
    return "<i>Are you looking for /db-test or /hello ?</i>"

#@app.route('/db-test')
#def test_database_connection():
#    print("Executing a sample query on the database using the credentials from db_credentials.py")
#    db_connection = connect_to_database()
#    query = "SELECT * from bsg_people;"
#    result = execute_query(db_connection, query)
#    return render_template('db_test.html', rows=result)
