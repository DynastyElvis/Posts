from datetime import datetime
from post import db, login_manager
#from email.policy import default
from flask_login import UserMixin



@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))




# class  User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(20), unique=True, nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)
#     avator = db.Column(db.String(20), nullable=False, default='default.jpg')
#     password = db.Column(db.String(60), nullable=False)
#     posts = db.relationship('post', backref='author', lazy=True)

#     def __repr__(self):
#         return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class User (db.Model, UserMixin): # User class
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    email = db.Column(db.String(130), unique=True, nullable=False)
    avator = db.Column(db.String(130), nullable=False, default='default.png')
    password = db.Column(db.String(130), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)
    
    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.avator}')"
    
class Post(db.Model):# Post class
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    content = db.Column(db.String(300), unique=True, nullable=False)
    #image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    date = db.Column(db.DateTime, nullable=False,  default=datetime.utcnow) 
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)    
    
    
    
    def __repr__(self):
        return f"Post('{self.title}', '{self.date}')"

