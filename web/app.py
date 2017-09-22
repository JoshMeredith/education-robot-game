from flask import Flask
from flask import render_template

app = Flask(__name__, static_url_path='/static')

# FIXME: Hardcoded worlds.
WORLDS = {
    'level0': {
        'numRows': 8,
        'numCols': 8,
        'start': {'x': 2, 'y': 3},
        'startDir': 'Down',
        'goal': {'x': 6, 'y': 1},
    },
}

@app.route('/<level>')
def hello_world(level):
    return render_template('js-test.html', grid=WORLDS[level])
