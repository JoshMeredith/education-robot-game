from flask import render_template, redirect, url_for

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
        # TODO(junkbot): Check if user already exists.
        # form.username.errors.append('Username already exists!')
        user = User(username=form.username.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        # TODO(junkbot): Flash a confirmation message.
        return redirect(url_for('home'))

    return render_template('signup.html', form=form)

@app.route('/signin', methods=["GET", "POST"])
def signin():
    form = UsernamePasswordForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first_or_404()
        if user.is_correct_password(form.password.data):
            login_user(user)
            return redirect(url_for('home'))
        else:
            # TODO(junkbot): Display errors?
            return redirect(url_for('signin'))

    return render_template('signin.html', form=form)

@app.route('/signout')
def signout():
    logout_user()
    return redirect(url_for('home'))
