from flask import Flask
from flask import render_template

from levels import LEVELS, WORLDS

app = Flask(__name__, static_url_path='/static')

@app.route('/<level>')
def serve_level(level):
    return render_template('index.html', grid=LEVELS[level])

@app.route('/levels')
@app.route('/')
def level_selector():
    world_levels = [
        [ {'tag': k, 'name': LEVELS[k]["name"], 'skin': LEVELS[k]["skin"]}
            for k in v ]
            for _, v in sorted(list(WORLDS.items())) ]
    return render_template('challenges.html', worlds=world_levels)
