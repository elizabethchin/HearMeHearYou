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


        # We need to add to the session or it won't ever be stored
        db.session.add(user)

    # Once we're done, we should commit our work
    db.session.commit()


def load_inquiries():
    """Load movies from u.inquiry into database."""
    print("Inquiries")

    Movie.query.delete()

    #Read u.item file and insert data
    for row in open("seed_data/u.inquiry"):
        row = row.rstrip().split("|")
        print(row)
        movie_id, title, released_str, empty, imdb_url = row[:5]

        title = title[:-7]

        if released_str:
            released_at = datetime.strptime(released_str, "%d-%b-%Y")
        else:
            released_at = None

        movie = Movie(movie_id=movie_id,
                    title=title,
                    released_at=released_at,
                    imdb_url=imdb_url)

        db.session.add(movie)

    db.session.commit()


def load_responses():
    """Load responses from u.response into database."""
    print("Responses")

    Rating.query.delete()

    for row in open("seed_data/u.response"):
        row = row.rstrip().split("\t")
        user_id, movie_id, score, extra = row

        user_id = int(user_id)
        movie_id = int(movie_id)
        score = int(score)

        rating = Rating(user_id=user_id,
                        movie_id=movie_id,
                        score=score)
        db.session.add(rating)

    db.session.commit()


if __name__ == "__main__":
    connect_to_db(app)

    # In case tables haven't been created, create them
    db.create_all()

    # Import different types of data
    load_users()
    load_movies()
    load_ratings()
    set_val_user_id()
