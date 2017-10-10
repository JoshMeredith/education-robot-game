from flask import Flask
from flask import render_template

app = Flask(__name__, static_url_path='/static')

# FIXME: Hardcoded worlds.
WORLDS = {
    'level1': {
        'numRows': 1,
        'numCols': 2,
        'start': {'x': 0, 'y': 0},
        'startDir': 'Down',
        'goal': {'x': 0, 'y': 1},
        'grid': [
            ['_', '_']
        ]
    },
    'level2': {
        'numRows': 5,
        'numCols': 5,
        'start': {'x': 3, 'y': 1},
        'startDir': 'Down',
        'goal': {'x': 1, 'y': 3},
        'grid': [
            ['_', '_', '_', '_', '_'],
            ['_', '_', '_', '_', '_'],
            ['_', '_', '_', '_', '_'],
            ['_', '_', '_', '_', '_'],
            ['_', '_', '_', '_', '_']
        ]
    },
    'level3': {
        'numRows': 1,
        'numCols': 11,
        'start': {'x': 0, 'y': 0},
        'startDir': 'Down',
        'goal': {'x': 0, 'y': 10},
        'grid': [
            ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_']
        ]
    },
    'level4': {
        'numRows': 5,
        'numCols': 5,
        'start': {'x': 2, 'y': 1},
        'startDir': 'Down',
        'goal': {'x': 2, 'y': 3},
        'grid': [
            ['_', '_', '_' , '_', '_'],
            ['_', '_', 'TL', 'H', '_'],
            ['_', '_', 'V' , '_', '_'],
            ['_', '_', 'BL', 'H', '_'],
            ['_', '_', '_' , '_', '_']
        ]
    }
}

@app.route('/<level>')
def hello_world(level):
    return render_template('index.html', grid=WORLDS[level])
