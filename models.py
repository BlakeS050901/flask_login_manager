from extensions import db


class User(db.Model):
    __tablename__ = 'user'

    email = db.Column(db.String(120), unique=True, nullable=False, primary_key=True)
    password = db.Column(db.String(60), nullable=False)







