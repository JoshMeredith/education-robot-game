from flask import render_template, redirect, url_for, flash, jsonify, request

from flask_login import login_user, logout_user, current_user, login_required

from web import app, db
from web.levels import LEVELS, WORLDS, update_levels
from web.forms import UsernamePasswordForm
from web.models import User, Level, Progress

@app.before_first_request
def startup():
    # This should probably be done on load, rather than the first request. This
    # is easier to implement.
    update_levels(db)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/level/<level>')
@app.route('/level/<level>/')
def serve_level(level):
    level_data = dict(LEVELS[level])
    level_data['codename'] = level
    return render_template('level.html', level=level_data)

@app.route('/levels')
@app.route('/levels/')
def level_selector():
    level_ids = {level.codename: level.id for level in Level.query.all()}

    # Extract info for world levels.
    world_levels = [
            [ {'id': level_ids[k],
                'tag': k,
                'name': LEVELS[k]["name"],
                'skin': LEVELS[k]["skin"]} for k in v ]
            for _, v in sorted(list(WORLDS.items())) ]

    # Find the user's progress for each level, if logged in.
    level_progress = {}

    if current_user.is_authenticated:
        all_progress = Progress.query.filter_by(user_id=current_user.id).all()
        for progress in all_progress:
            level_progress[progress.level_id] = (progress.code_score,
                    progress.execution_score)

    return render_template('level_selector.html', worlds=world_levels,
            level_progress=level_progress)

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

@app.route('/update_score', methods=["POST"])
def update_score():
    if not current_user.is_authenticated:
        return jsonify({'success': False })

    request_json = request.get_json(silent=True)
    if not request_json:
        # HTTP Error code 415.
        return "Unsupported media type", 415

    codename = request_json['codename']

    # Check that level exists.
    level = Level.query.filter_by(codename=codename).first_or_404()

    INFINITY = (1 << 30)
    try:
        code_score = int(request_json['code_score'])
        if code_score <= 0:
            raise ValueError
    except (ValueError, KeyError) as e:
        code_score = INFINITY

    try:
        execution_score = int(request_json['execution_score'])
        if execution_score <= 0:
            raise ValueError
    except (ValueError, KeyError) as e:
        execution_score = INFINITY

    # Check if a Progress entry exists.
    cur_score = Progress.query.filter_by(user_id=current_user.id,
            level_id=level.id).first()
    if not cur_score:
        cur_score = Progress(user_id=current_user.id,
                level_id=level.id,
                code_score=code_score,
                execution_score=execution_score)
        db.session.add(cur_score)
    else:
        # Update the progress, if necessary.
        cur_score.code_score = min(cur_score.code_score, code_score)
        cur_score.execution_score = min(cur_score.execution_score, execution_score)
    db.session.commit()

    return jsonify({
        'success': True,
        'level': codename,
        'level_id': level.id,
        'code_score': cur_score.code_score,
        'execution_score': cur_score.execution_score
    })
