"""Project Website."""

from jinja2 import StrictUndefined

from flask import Flask, render_template, redirect, request, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from secret import keys 
from model import connect_to_db, db, User, Inquiry, Response

app = Flask(__name__)

app.jinja_env.undefined = StrictUndefined

app.secret_key = "ABC"

#Routes

@app.route("/")
def landing_page():
    """Returns landing page."""
  
    return render_template("landing_page.html")

@app.route("/login_page")
def login_page():
    """Renders login page."""

    return render_template("login_page.html")

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
    
    flash("Logged In")

    if user.user_id == 6:
        return redirect("/user_list")
    
    else:
        return redirect(f"/user/{user.user_id}")


@app.route("/user/<int:user_id>")
def user_detail(user_id):
    """User's Information."""
    
    user = User.query.get(user_id)
   
    return render_template("user.html", user=user)

@app.route("/inquiry/<int:inquiry_id>")
def report_detail(inquiry_id):
    """Report details."""
    user_id = session["user_id"]

    inquiry = Inquiry.query.get(inquiry_id)
    responses = Response.query.options(db.joinedload('user')).filter(Response.inquiry_id == inquiry_id).all()
    
    
    return render_template("view_report.html", inquiry=inquiry, 
        user_id=user_id, responses=responses)

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
    """Submit report to HearMe."""
    
    todays_date = request.form.get("todays_date")
    incident_date = request.form.get("incident_date")
    subject = request.form.get("subject")
    inquiry_text = request.form.get("inquiry_text")
    anonymous = request.form.get("anonymous")
    user_id = session["user_id"]
    archive = False

    print("HEREEEEEE")
    print(anonymous)
    anonymous = anonymous == "True"
    print(anonymous)



    new_inquiry = Inquiry(user_id=user_id, todays_date=todays_date, subject=subject, 
    incident_date=incident_date,inquiry_text=inquiry_text, anonymous=bool(anonymous), archive=archive)
    
    db.session.add(new_inquiry)
    db.session.commit()

    flash("New Inquiry added")

    return redirect(f"/user/{user_id}")


@app.route("/save-report", methods=["POST"])
def save_report():
    """Save report to archive."""
    
    todays_date = request.form.get("todays_date")
    incident_date = request.form.get("incident_date")
    subject = request.form.get("subject")
    inquiry_text = request.form.get("inquiry_text")
    anonymous = request.form.get("anonymous")
    user_id = session["user_id"]
    archive = True
    print("HEREEEEEE")
    print(anonymous)
    anonymous = anonymous == "True"
    print(anonymous)


    new_inquiry = Inquiry(user_id=user_id, todays_date=todays_date, subject=subject, 
    incident_date=incident_date, inquiry_text=inquiry_text, anonymous=bool(anonymous), archive=archive)
    
    db.session.add(new_inquiry)
    db.session.commit()

    flash("Saved Inquiry")

    return redirect(f"/user/{user_id}")

@app.route("/user_list")
def list_users():

    if session["user_id"] == 6:

        inquiries = Inquiry.query.filter_by(anonymous=True).all()
        users = User.query.all()
        return render_template("user_list.html", users=users, inquiries=inquiries)
    
    else:
        return redirect("/")


@app.route("/reply-form", methods=["POST"])
def reply_form():
    """Submit Reply form."""

    inquiry_id = request.form.get("inquiry_id")
    user_id = request.form.get("user_id")
    
    response_date = request.form.get("todays_date")
    responding_to = request.form.get("inquiry_id")
    response_text = request.form.get("response_text")

    response_date= response_date[:11]

    print("HEREEEEEEEEEE")
    print(response_date)

    new_response = Response(inquiry_id=inquiry_id, user_id=user_id, response_date=response_date,
        responding_to=responding_to, response_text=response_text)

    db.session.add(new_response)
    db.session.commit()

    return redirect(f"/inquiry/{inquiry_id}")

@app.route("/contact")
def contact():
    """My contact information with google map api."""

    return render_template("contact.html", google_map_api=keys['google_map_api'])




if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True
    connect_to_db(app)
    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")