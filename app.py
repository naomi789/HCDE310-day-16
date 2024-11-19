import time
from flask import Flask, session

from projectsecrets import app_secret # Secret string for "signing" session data, stored separately similar to API keys

app = Flask(__name__)
app.secret_key = app_secret


@app.route("/")
def index():
   session["firstvisit"] = time.ctime()
   return "<a href='/otherpage'>Click me</a> to go to the other page"


@app.route("/otherpage")
def otherpage():
   return "You started visiting this site at " + session["firstvisit"] 
