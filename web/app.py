from flask import Flask
from flask import render_template

app = Flask(__name__, static_url_path='/static')

# FIXME: Hardcoded worlds.
WORLDS = {
    'level1': {
        'name': 'Level 1',
        'numRows': 1,
        'numCols': 2,
        'start': {'row': 0, 'col': 0},
        'startDir': 'Down',
        'goal': {'row': 0, 'col': 1},
        'grid': [
            ['_', '_']
        ]
    },
    'level2': {
        'name': 'Level 2',
        'numRows': 5,
        'numCols': 5,
        'start': {'row': 3, 'col': 1},
        'startDir': 'Down',
        'goal': {'row': 1, 'col': 3},
        'grid': [
            ['_', '_', '_', '_', '_'],
            ['_', '_', '_', '_', '_'],
            ['_', '_', '_', '_', '_'],
            ['_', '_', '_', '_', '_'],
            ['_', '_', '_', '_', '_']
        ]
    },
    'level3': {
        'name': 'Level 3',
        'numRows': 1,
        'numCols': 11,
        'start': {'row': 0, 'col': 0},
        'startDir': 'Down',
        'goal': {'row': 0, 'col': 10},
        'grid': [
            ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_']
        ]
    },
    'level4': {
        'name': 'Level 4',
        'numRows': 5,
        'numCols': 5,
        'start': {'row': 2, 'col': 1},
        'startDir': 'Down',
        'goal': {'row': 2, 'col': 3},
        'grid': [
            ['_', '_', '_' , '_', '_'],
            ['_', '_', 'TL', 'H', '_'],
            ['_', '_', 'V' , '_', '_'],
            ['_', '_', 'BL', 'H', '_'],
            ['_', '_', '_' , '_', '_']
        ]
    },
    'level5': {
        'name': 'Level 5',
        'numRows': 15,
        'numCols': 14,
        'start': {'row': 2, 'col': 9},
        'startDir': 'Up',
        'goal': {'row': 12, 'col': 3},
        'grid': [
            ['_', '_', '_', '_', '_', '_', 'V', '_', '_', '_', '_', '_', '_', '_'],
            ['_', '_', '_', 'H', '_', '_', 'V', '_', '_', 'H', '_', '_', '_', '_'],
            ['_', '_', '_', '_', 'V', '_', '_', '_', 'V', '_', '_', 'H', 'H', '_'],
            ['_', 'V', '_', '_', 'V', '_', '_', '_', 'BL', 'H', 'H', '_', '_', '_'],
            ['_', 'V', '_', 'H', '_', 'H', '_', 'H', '_', '_', '_', '_', 'H', '_'],
            ['_', 'V', '_', '_', 'H', '_', 'H', '_', '_', '_', '_', 'H', '_', '_'],
            ['H', '_', 'V', '_', '_', '_', '_', 'H', '_', '_', 'H', '_', '_', 'H'],
            ['_', '_', 'V', '_', 'H', '_', 'H', '_', '_', 'H', '_', '_', '_', '_'],
            ['_', 'H', '_', 'H', '_', '_', '_', 'V', '_', '_', 'H', 'H', '_', '_'],
            ['_', '_', 'H', '_', '_', '_', '_', 'V', '_', '_', '_', '_', 'V', '_'],
            ['_', '_', '_', 'V', '_', '_', '_', '_', 'H', '_', 'V', '_', 'V', '_'],
            ['_', 'V', '_', 'V', '_', 'H', 'H', 'H', '_', '_', 'V', '_', 'V', '_'],
            ['_', 'V', '_', '_', 'H', '_', '_', '_', '_', '_', 'BL', 'H', '_', '_'],
            ['_', '_', 'H', 'H', '_', 'H', 'H', 'H', 'H', 'H', '_', '_', '_', '_'],
            ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', 'H', '_', '_']
        ]
    }
}

@app.route('/<level>')
def hello_world(level):
    return render_template('index.html', grid=WORLDS[level])

@app.route('/levels')
@app.route('/')
def hello_world_2():
    return render_template('challenges.html',
                           levels=[{'tag': k, 'name': WORLDS[k]["name"]} for k in WORLDS.keys()])
