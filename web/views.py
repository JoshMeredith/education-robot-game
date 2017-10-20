from flask import render_template, redirect, url_for, flash

from flask_login import login_user, logout_user

from web import app, db
from web.levels import LEVELS, WORLDS
from web.forms import UsernamePasswordForm
from web.models import User

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/level/<level>')
@app.route('/level/<level>/')
def serve_level(level):
    return render_template('level.html', level=LEVELS[level])

@app.route('/levels')
@app.route('/levels/')
def level_selector():
    world_levels = [
        [ {'tag': k, 'name': LEVELS[k]["name"], 'skin': LEVELS[k]["skin"]}
            for k in v ]
            for _, v in sorted(list(WORLDS.items())) ]
    return render_template('level_selector.html', worlds=world_levels)

@app.route('/signup', methods=["GET", "POST"])
def signup():
    form = UsernamePasswordForm()
    if form.validate_on_submit():
        exists = db.session.query(User.id).filter_by(username=form.username.data).scalar()
        if exists:
            form.username.errors.append('That username is already taken!')
            return render_template('signup.html', form=form)

        user = User(username=form.username.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()

        flash('Successfully created an account! You can login now.')
        return redirect(url_for('login'))

    return render_template('signup.html', form=form)

@app.route('/login', methods=["GET", "POST"])
def login():
    form = UsernamePasswordForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.is_correct_password(form.password.data):
            login_user(user)
            # TODO: redirect to profile page?

            flash('Welcome to Codebot!')
            return redirect(url_for('home'))
        else:
            flash('Invalid username / password', 'error')
            return redirect(url_for('login'))

    return render_template('login.html', form=form)

@app.route('/logout')
def logout():
    logout_user()
    flash('Successfully logged you out.')
    return redirect(url_for('home'))
