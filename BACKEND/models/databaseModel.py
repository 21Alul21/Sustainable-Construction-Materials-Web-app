from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Users(db.Model):
    """Class for modeling user information"""

    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(10), nullable=False)
    first_name = db.Column(db.String(10), nullable=False)
    last_name = db.Column(db.String(10), nullable=False)
    discipline = db.Column(db.String(100))
    interest = db.Column(db.Text, nullable=False)
    email = db.Column(db.String(20), nullable=False, unique=True)
    is_active = db.Column(db.Boolean)
    posts = db.relationship('Posts', backref='users', lazy=True)
    comments = db.relationship('Comments', backref='users', lazy=True)
 

class Posts(db.Model):
    """Class for modeling posts made by users"""

    id = db.Column(db.Integer, primary_key=True)
    post_field = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    comment = db.relationship('Comments', backref='post', lazy=True)

    def __repr__(self):
        return f'post - {self.post_field}, user id - {self.user_id}'


class Comments(db.Model):
    """Class for modelling comments made on posts"""
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'), nullable=False)
   
    

class Reactions(db.Model):
    """Class for modeling reactions made on posts"""
    id = db.Column(db.Integer, primary_key=True)
    reaction_count = db.Column(db.Integer)
    post_id = db.Column(db.Integer, nullable=False)