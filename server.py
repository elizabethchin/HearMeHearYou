"""Project Website."""

from jinja2 import StrictUndefined
from flask import Flask, render_template, redirect, request, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from model import User, Inquiry, Response

app = Flask(__name__)

app.jinja_env.undefined = StrictUndefined
app.jinja_env.auto_reload = True

#Routes

@app.route("/")
def homepage():
    """Returns Homepage."""
    
    return render_template("homepage.html")

@app.route("/welcome")
def welcome():
    """User's personal page after logging in."""
  
    return render_template("welcome.html")

@app.route("/view-all-reports")
def get_name():
    """List of users reports"""

    return render_template("/view-all-reports")
    

if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")