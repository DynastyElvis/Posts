from datetime import datetime
from post import db#, login_manager


class User (db.Model): # User class
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    avator = db.Column(db.String(20), nullable=False, default='default.png')
    email = db.Column(db.String(60), nullable=False)
    post = db.relationship('Post', backref='author', lazy=True)
    
    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.avator}')"
    
class Post(db.Model):# Post class
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    content = db.Column(db.String(300), unique=True, nullable=False)
    #image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    date = db.Column(db.String(60), nullable=False,  default=datetime.utcnow) 
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)    
    
    
    
    def __repr__(self):
        return f"User('{self.title}', '{self.date}', '{self.author}')"

