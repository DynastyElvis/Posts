from flask import redirect, render_template, url_for, flash
from .forms import *#RegistrationForm, LoginForm
from .models import *#RegistrationForm, LoginForm

from post import app, bcrypt
from flask_login import login_user, current_user, logout_user, login_required



@app.route("/")
@app.route("/home")

def home():
    posts = Post.query.all()
    return render_template('index.html', posts=posts)


@app.route("/profile", methods=['GET', 'POST'])
def profile():
    form = UpdateProfileForm
    if form.validate_on_submit():
        if form.avator.data:
            pass
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Account has been updated successfully!', 'success')
        return redirect(url_for('profile'))
    return render_template('profile.html', title='User Profile', form=form)

@app.route("/new/post", methods=['GET', 'POST'])
def create():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data, author=current_user )
        db.session.add(post)
        db.session.commit()
        
        flash('Your pitch has been created Successfully', 'success')
        return redirect(url_for('home'))

    return render_template('create.html', title="New Post", form=form)


@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        pw_hash = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=pw_hash)
        db.session.add(user)
        db.session.commit()
        login_user(user)
        
        
        flash('Account created', 'success')
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
            flash('Login successful')
            return redirect(url_for('home'))
        
    return render_template('login.html', title='login', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))
