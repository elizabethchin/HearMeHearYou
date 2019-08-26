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

    inquiries = db.relationship('Inquiry')
    responses = db.relationship("Response")

    def __repr__(self):
        """Provide helpful representation when printed."""
        
        return ("<User information: user_id={} first_name={} last_name={} email={} password={}>"
            .format(self.user_id, self.first_name, self.last_name, self.email, self.password))

class Inquiry(db.Model):
    """List of inquiries."""

    __tablename__ = "inquiries"

    inquiry_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    todays_date = db.Column(db.TIMESTAMP(timezone=True), nullable=False)
    incident_date = db.Column(db.TIMESTAMP(timezone=True), nullable=True)
    location = db.Column(db.String(100), nullable=True)
    witness = db.Column(db.String(100), nullable=True)
    inquiry_text = db.Column(db.String(1000000), nullable=False)
    anonymous = db.Column(db.Boolean, default=True)
    archive = db.Column(db.Boolean)

    user = db.relationship('User')
    responses = db.relationship("Response")

    def __repr__(self):
        """Provide helpful representation when printed."""
        return """<Inquiry: inquiry_id={} user_id={} todays_date={} incident_date={}
                location={} witness={} incident_text={} anonymous={}>""".format(self.inquiry_id, self.user_id, self.todays_date, 
                self.incident_date, self.location, self.witness, self.inquiry_text, self.anonymous, self.archive)

class Response(db.Model):
    """List of responses to inquiries."""

    __tablename__ = "responses"

    response_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    inquiry_id = db.Column(db.Integer, db.ForeignKey('inquiries.inquiry_id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False) #change this to person replying
    response_date = db.Column(db.TIMESTAMP(timezone=True), nullable=False)
    responding_to = db.Column(db.Integer, nullable=False)
    response_text = db.Column(db.String(1000000), nullable=False)

    user = db.relationship('User')
    inquiries = db.relationship('Inquiry')

    def __repr__(self):
        """Provide helpful representation when printed."""
        return """<Response: response_id={} inquiry_id={} user_id={} response_date={}
                responding_to={} response_text={}>""".format(self.response_id, self.inquiry_id, self.user_id, self.response_date, 
                self.responding_to, self.response_text)


##############################################################################
# Helper functions

def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our PstgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///project'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_ECHO'] = True
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.
    from server import app

    connect_to_db(app)
    print("Connected to DB.")
