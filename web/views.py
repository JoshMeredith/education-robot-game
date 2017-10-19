from flask import render_template

from web import app
from web.levels import LEVELS, WORLDS

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
