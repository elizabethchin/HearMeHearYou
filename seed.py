"""Utility file to seed ratings database from MovieLens data in seed_data/"""

from sqlalchemy import func
from model import User
from model import Inquiry # remember to import so class can be accessed
from model import Response


from model import connect_to_db, db
from server import app
from datetime import datetime


def load_users():
    """Load users from u.user into database."""

    print("Users")

    # Delete all rows in table, so if we need to run this a second time,
    # we won't be trying to add duplicate users
    User.query.delete()

    # Read u.user file and insert data
    for row in open("seed_data/u.user"):

        row = row.rstrip().split(",")
        user_id, first_name, last_name, email, password = row

        user = User(user_id=user_id,
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    password=password)

        db.session.add(user)

    db.session.commit()


def load_inquiries():
    """Load movies from u.inquiry into database."""
    print("Inquiries")

    Inquiry.query.delete()

    #Read u.item file and insert data
    for row in open("seed_data/u.inquiry"):
        row = row.rstrip().split(",")
        print(row)
        inquiry_id, user_id, todays_date, incident_date, location, witness, inquiry_text, anonymous = row

        inquiry = Inquiry(inquiry_id=inquiry_id,
                    user_id=user_id,
                    todays_date=todays_date,
                    incident_date=incident_date,
                    location=location,
                    witness=witness,
                    inquiry_text=inquiry_text,
                    anonymous=anonymous)

        db.session.add(inquiry)

    db.session.commit()


def load_responses():
    """Load responses from u.response into database."""
    print("Responses")

    Response.query.delete()

    for row in open("seed_data/u.response"):
        row = row.rstrip().split(",")
        response_id, inquiry_id, user_id, response_date, responding_to, response_text = row

        response = Response(response_id=response_id,
                            inquiry_id=inquiry_id,
                            user_id=user_id,
                            response_date=response_date,
                            responding_to=responding_to,
                            response_text=response_text)

        db.session.add(response)

    db.session.commit(response)


if __name__ == "__main__":
    connect_to_db(app)

    # In case tables haven't been created, create them
    db.create_all()

    # Import different types of data
    load_users()
    load_inquiries()
    load_responses()
    set_val_user_id()
