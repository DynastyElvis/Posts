from flask import redirect, render_template, url_for, flash
from .forms import *#RegistrationForm, LoginForm
from post import app#, db, bcrypt

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


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html', title='Register', form=form)
