from email.policy import default
from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime





app = Flask(__name__)

db = SQLAlchemy(app)
migrate = Migrate(app, db)


app.config['SECRET_KEY'] = '123456789'
app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

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



post = [
    {
        'author': 'Elvis',
        'title': 'Flask',
        'content': 'Flask is a microframework for Python based on Werkzeug, Jinja2 and good intentions.',
        'date_posted': 'January 21, 2019'
        
    },
    {
        'author': 'Lornah',
        'title': 'Flask',
        'content': 'Flask is a microframework for Python based on Werkzeug, Jinja2 and good intentions.',
        'date_posted': 'January 21, 2019'
        
    },
    {
        'author': 'Hope',
        'title': 'Flask',
        'content': 'Flask is a microframework for Python based on Werkzeug, Jinja2 and good intentions.',
        'date_posted': 'January 21, 2019'
        
    }
]


@app.route("/")
@app.route("/home")

def home():
    return render_template('index.html', posts=post)


@app.route("/profile")
def profile():
    return render_template('profile.html', title='User Profile')


@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Register', form=form)



if __name__ == "__main__":
    app.run(debug=True)

