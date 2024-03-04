from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime

db = SQLAlchemy()


class Users(db.Model, UserMixin):
    """Class for modeling user information"""

    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(10), nullable=False)
    email = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(20), nullable=False)
    posts = db.relationship('Posts', backref='users', lazy=True)
    comments = db.relationship('Comments', backref='author', lazy=True)
    
    

class Posts(db.Model):
    """Class for modeling posts made by users"""

    id = db.Column(db.Integer, primary_key=True)
    post_field = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    comment = db.relationship('Comments', backref='post', lazy=True)
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)

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