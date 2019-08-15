"""Project Website."""

from jinja2 import StrictUndefined

from flask import Flask, render_template, redirect, request, flash, session
from flask_debugtoolbar import DebugToolbarExtension

from model import connect_to_db, db, User, Inquiry, Response

app = Flask(__name__)

app.jinja_env.undefined = StrictUndefined

app.secret_key = "ABC"

#Routes

@app.route("/")
def homepage():
    """Returns Homepage with login."""
    
    return render_template("homepage.html")


@app.route("/login", methods=["POST"])
def process_login():
    """Gets user's email and password."""

    #get email and password that the user submitted
    email = request.form["email"]
    password = request.form["password"]

    user = User.query.filter_by(email=email).first()

    if not user:
        flash("No such user")
        return redirect("/")

    if user.password != password:
        flash("Incorrect password")
        return redirect("/")

    session["user_id"] = user.user_id
    print("HIII")
    flash("Logged In")
    print("HERE")
    
    return redirect(f"/user/{user.user_id}")


@app.route("/user/<int:user_id>")
def user_detail(user_id):
    """User's Information."""
    
    user = User.query.get(user_id)
   
    return render_template("user.html", user=user)

@app.route("/inquiry/<int:inquiry_id>")
def report_detail(inquiry_id):
    """Report details."""

    inquiry = Inquiry.query.get(inquiry_id)

    return render_template("view_report.html", inquiry=inquiry)



@app.route("/logout")
def logout():
    """Log out."""

    del session["user_id"]
    flash("Logged Out.")
    return redirect("/")

@app.route("/register")
def register():
    """Show new user registration form."""
    

    return render_template("register.html")

@app.route("/register", methods=["POST"])
def process_registration():
    """Process new user registration form."""

    first_name = request.form["fname"] #get this from html where name=""
    last_name = request.form["lname"]
    email = request.form["email"]
    password = request.form["password"]

    new_user = User(first_name=first_name, last_name=last_name, email=email, password=password)
    
    db.session.add(new_user)
    db.session.commit()

    flash(f"User {first_name} {last_name} added.")

    return redirect("/")



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


    

if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True
    connect_to_db(app)
    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")