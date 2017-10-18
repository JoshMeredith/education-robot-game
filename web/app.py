from flask import Flask
from flask import render_template

from levels import LEVELS, WORLDS

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/<level>')
@app.route('/<level>/')
def serve_level(level):
    return render_template('level.html', level=LEVELS[level])

@app.route('/challenges')
@app.route('/challenges/')
def level_selector():
    world_levels = [
        [ {'tag': k, 'name': LEVELS[k]["name"], 'skin': LEVELS[k]["skin"]}
            for k in v ]
            for _, v in sorted(list(WORLDS.items())) ]
    return render_template('challenges.html', worlds=world_levels)
