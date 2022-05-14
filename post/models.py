from datetime import datetime
from post import db#, login_manager


class User (db.Model): # User class
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    #image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    email = db.Column(db.String(60), nullable=False)
    
    
class Post(db.Model):# Post class
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    content = db.Column(db.String(300), unique=True, nullable=False)
    #image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    date = db.Column(db.String(60), nullable=False,  default=datetime.utcnow)     
    
    
    
    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

