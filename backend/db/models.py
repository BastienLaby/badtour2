from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Player(db.Models):
    """
    """
    id = db.Column(db.Integer(), primary_key=True)
    license = db.Column(db.String(64), unique=True)
    firstname = db.Column(db.String(64))
    lastname = db.Column(db.String(64))
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f"<Player {self.firstname}.{self.lastname}#{license}>"


class Genre(db.Models):
    """
    male / female
    """
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(64))


class Tournement(db.Models):
    """
    """
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(64))
    start_day = db.Column(db.Date())
    end_day = db.Column(db.Date())


class Category(db.Models):
    """
    SH, DH, SD, DD, DX
    """
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(64))
    single = db.Column(db.Boolean())


class Subscription(db.Models):
    """
    """
    id = db.Column(db.Integer(), primary_key=True)
    tournement_id = db.Column(db.Integer())  # Tournement.id
    player_id = db.Column(db.Integer())  # Player.id
    category_id = db.Column(db.Integer())  # Category.id
    state = db.Column(db.String(64))  # wip, sent, accepted, etc.
    mate_id = db.Column(db.Integer(), nullable=True)  # Player.id

