"""Project Website."""

from jinja2 import StrictUndefined
from flask import Flask, render_template, redirect, request, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from model import User, Inquiry, Response

app = Flask(__name__)

app.jinja_env.undefined = StrictUndefined
app.jinja_env.auto_reload = True

app.secret_key = "ABC"

#Routes

# @app.route("/")
# def homepage():
#     """Returns Homepage."""
    
#     return render_template("homepage.html")

# @app.route("/welcome")
# def welcome():
#     """User's personal page after logging in."""
  
#     return render_template("welcome.html")

# @app.route("/about")
# def about():
#     """Describes what this web app does."""

#     return render_template("about.html")


@app.route("/create-report")
def create_report():
    """Form for generating report."""

    return render_template("create_report.html")

    

@app.route("/handle-report", methods=["POST"])
def handle_report():
    """Get information from report user created"""
    
    todays_date = request.form.get("todays_date")
    incident_date = request.form.get("incident_date")
    location = request.form.get("location")
    witness = request.form.get("witness")
    inquiry_text = request.form.get("inquiry_text")
    anonymous = request.form.get("anonymous")

    return render_template("view_report.html",
                    todays_date=todays_date,
                    incident_date=incident_date,
                    location=location,
                    witness=witness,
                    inquiry_text=inquiry_text,
                    anonymous=anonymous)


# @app.route("/view-all-reports")
# def view_all_reports():
#     """List of users reports"""

#     return render_template("/view_all_reports.html")
    

if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")