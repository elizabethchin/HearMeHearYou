"""Models and database functions for final project."""

from flask_sqlalchemy import SQLAlchemy

# This is the connection to the PostgreSQL database; we're getting this through
# the Flask-SQLAlchemy helper library. On this, we can find the `session`
# object, where we do most of our interactions (like committing, etc.)

db = SQLAlchemy()


##############################################################################
# Model definitions

class User(db.Model):
    """List of users."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(50), nullable=False)

    reports = db.relationship('Report')

    def __repr__(self):
        """Provide helpful representation when printed."""
        
        return ("<User user_id={} first_name={} last_name={} email={}>"
            .format(self.user_id, self.first_name, self.last_name, self.email))

class Report(db.Model):
    """List of reports."""

    __tablename__ = "reports"

    report_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Intiger, db.ForeignKey('users.user_id'), nullable=False)
    date_time = db.Column(db.TIMESTAMPTZ, nullable=False)
    location = db.Column(db.String(100), nullable=True)
    witness = db.Column(db.String(100), nullable=True)
    anonymous = db.Column(db.Boolean, default=True)
    incident_descrip = db.Column(db.String(1000000), nullable=False)

    user = db.relationship('User')

    def __repr__(self):
        """Provide helpful representation when printed."""
        return """<Report ID report_id={} user_id={} date_time={} location={}
                witness={} anonymous={} incident_descrip={}>""".format(self.report_id, self.user_id, self.date_time, 
                self.location, self.witness, self.anonymous, self.incident_descrip)

##############################################################################
# Helper functions

def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our PstgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///project'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # app.config['SQLALCHEMY_ECHO'] = True
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.

    from server import app
    connect_to_db(app)
    print("Connected to DB.")
