"""Utility file to seed ratings database from MovieLens data in seed_data/"""

from sqlalchemy import func
from model import User, Inquiry, Response # remember to import so class can be accessed

from model import connect_to_db, db
from server import app
from datetime import datetime

def load_users():
    """Load users from u.user into database."""

    print("Users")

    # Read u.user file and insert data
    for row in open("seed_data/u.user"):

        row = row.rstrip().split("|")
        first_name, last_name, email, password = row

        user = User(first_name=first_name,
                    last_name=last_name,
                    email=email,
                    password=password)

        db.session.add(user)

    db.session.commit()


def load_inquiries():
    """Load movies from u.inquiry into database."""
    print("Inquiries")


    #Read u.item file and insert data
    for row in open("seed_data/u.inquiry"):
        row = row.rstrip().split("|")
        print(row)
        user_id, todays_date, incident_date, location, witness, inquiry_text, anonymous = row
        
        if todays_date == "none":
       		t_date = None
        else:
            t_date = datetime.strptime(todays_date, "%d-%b-%Y")
       
        if incident_date == "none":
            i_date = None
        else:
            i_date = datetime.strptime(incident_date, "%d-%b-%Y")

        inquiry = Inquiry(user_id=int(user_id),
                    todays_date=t_date,
                    incident_date=i_date,
                    location=location,
                    witness=witness,
                    inquiry_text=inquiry_text,
                    anonymous=bool(anonymous))

        print(inquiry)
        db.session.add(inquiry)

    db.session.commit()


def load_responses():
    """Load responses from u.response into database."""
    print("Responses")


    for row in open("seed_data/u.response"):
        row = row.rstrip().split("|")
        response_id, inquiry_id, user_id, response_date, responding_to, response_text = row

        if response_date == "none":
            r_date = None
        else:
            r_date = datetime.strptime(incident_date, "%Y-%m-%d")

        response = Response(response_id=int(response_id),
                            inquiry_id=int(inquiry_id),
                            user_id=int(user_id),
                            response_date=r_date,
                            responding_to=int(responding_to),
                            response_text=response_text)

        db.session.add(response)

    db.session.commit()


if __name__ == "__main__":
    connect_to_db(app)

    # In case tables haven't been created, create them
    db.create_all()

    # Import different types of data
    load_users()
    load_inquiries()
    load_responses()
  
