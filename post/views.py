from flask import redirect, render_template, url_for, flash
from .forms import *#RegistrationForm, LoginForm
from .models import *#RegistrationForm, LoginForm

from post import app, bcrypt
from flask_login import login_user, current_user, logout_user, login_required



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
    if current_user.is_authenticated:
        return redirect(url_for('home'))
        
    form = RegistrationForm()
    if form.validate_on_submit():
        pw_hash = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user=User(username=form.username.data, email=form.email.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        login_user(user)
        
        
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()    
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):    
            login_user(user)
            flash(f'Login for {form.username.data}!', 'successful')
            return redirect(url_for('home'))
        
    return render_template('login.html', title='login', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))
