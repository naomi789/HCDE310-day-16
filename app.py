import time
from flask import Flask, session
# Secret string for "signing" session data, stored separately
from projectsecrets import app_secret

app = Flask(__name__)
app.secret_key = app_secret

@app.route("/")
def index():
   login_time = time.ctime()
   session["firstvisit"] = login_time
   print(f"Another user just logged in at `{login_time}`!! Here's their key to their session: `{app_secret}`")
   return "<a href='/otherpage'>Click me</a> to go to the other page"


@app.route("/otherpage")
def otherpage():
   return "You started visiting this site at " + session["firstvisit"] 



