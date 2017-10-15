from flask import Flask
from flask import render_template

app = Flask(__name__, static_url_path='/static')

# FIXME: Hardcoded worlds.
WORLDS = {
    'level1': {
        'name': 'Level 1',
        'skin': 'grass',
        'numRows': 1,
        'numCols': 2,
        'start': {'row': 1, 'col': 1},
        'startDir': 'Down',
        'goals': [{'row': 1, 'col': 2}],
        'grid': [
            ['_', '_']
        ],
        'instructions': 
'A comment is a line of code that codebot will ignore.\n\
To write a comment we use // and then write some text.\n\
\n\
//this is a comment\n\
\n\
Comments have 2 main uses that you will see over and over\n\
during your time spent programming.\n\
1. Describing what your code does\n\
2. Toggling code on and off\n\
        ',
        'startCode': 
'//The next line moves the robot to the goal, uncomment it and hit RUN\n\
//moveRight;\
        '
    },
    'level2': {
        'name': 'Level 2',
        'skin': 'grass',
        'numRows': 5,
        'numCols': 5,
        'start': {'row': 4, 'col': 2},
        'startDir': 'Down',
        'goals': [{'row': 2, 'col': 4}],
        'grid': [
            ['_', '_', '_', '_', '_'],
            ['_', '_', '_', '_', '_'],
            ['_', '_', '_', '_', '_'],
            ['_', '_', '_', '_', '_'],
            ['_', '_', '_', '_', '_']
        ],
        'instructions': 
'In the last level you might have noticed that the line of\n\
code had a semicolon (;) at the end.\n\n\
This lets codebot know that you have finished giving an\n\
instruction - kind of like how a full stop lets you know\n\
when a sentence is finished.\n\n\
This becomes important when you have many instructions to\n\
give to codeBot. To complete this level uncomment the\n\
instructions that will lead codebot to the goal.\
        ',
        'startCode': 
'//moveUp;\n\
//moveDown;\n\
//moveLeft;\n\
//moveRight;\n\
//moveUp;\n\
//moveDown;\n\
//moveLeft;\n\
//moveRight;\
        '
    },
    'level3': {
        'name': 'Level 3',
        'skin': 'grass',
        'numRows': 1,
        'numCols': 11,
        'start': {'row': 1, 'col': 1},
        'startDir': 'Down',
        'goals': [{'row': 1, 'col': 11}],
        'grid': [
            ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_']
        ],
        'instructions': 
"It can get pretty tiresome repeatedly typing out the same\n\
instructions for codebot over and over again. That\'s why we\n\
have the times loop!\n\n\
By using the times loop we can tell codebot to follow a set\n\
of instructions any number of times. The following code will\n\
tell codebot to dance 10 times:\n\
times(10){\n\
    dance;\n\
}\n\n\
Unfortunately codebot hasn\'t learnt how to dance yet.\n\
He has learnt how to move right though! Use your newfound\n\
knowledge of loops to help codebot reach the goal.\
",
        'startCode': '//Write your code here!'
    },

    'level4': {
        'name': 'Level 4',
        'skin': 'grass',
        'numRows': 5,
        'numCols': 5,
        'start': {'row': 3, 'col': 2},
        'startDir': 'Down',
        'goals': [{'row': 3, 'col': 4}],
        'grid': [
            ['_', '_', '_', '_', '_'],
            ['_', '_', 'W', 'W', '_'],
            ['_', '_', 'W', '_', '_'],
            ['_', '_', 'W', 'W', '_'],
            ['_', '_', '_', '_', '_']
        ],
        'instructions': 
"Now we know how to move codebot around using the moveUp,\n\
moveDown, moveLeft and moveRight instructions. We also know\n\
how to use loops to make our code shorter. \n\n\
Use these tools to help codebot reach the goal.",
        'startCode': '//Write your code here!'
    },

    'level5': {
        'name': 'Level 5',
        'skin': 'grass',
        'numRows': 15,
        'numCols': 14,
        'start': {'row': 3, 'col': 10},
        'startDir': 'Up',
        'goals': [{'row': 13, 'col': 4}, {'row': 3, 'col': 11}],
        'grid': [
            ['_', '_', '_', '_', '_', '_', 'W', '_', '_', '_', '_', '_', '_', '_'],
            ['_', '_', '_', 'W', '_', '_', 'W', '_', '_', 'W', '_', '_', '_', '_'],
            ['_', '_', '_', '_', 'W', '_', '_', '_', 'W', '_', '_', 'W', 'W', '_'],
            ['_', 'W', '_', '_', 'W', '_', '_', '_', 'W', 'W', 'W', '_', '_', '_'],
            ['_', 'W', '_', 'W', '_', 'W', '_', 'W', '_', '_', '_', '_', 'W', '_'],
            ['_', 'W', '_', '_', 'W', '_', 'W', '_', '_', '_', '_', 'W', '_', '_'],
            ['W', '_', 'W', '_', '_', '_', '_', 'W', '_', '_', 'W', '_', '_', 'W'],
            ['_', '_', 'W', '_', 'W', '_', 'W', '_', '_', 'W', '_', '_', '_', '_'],
            ['_', 'W', '_', 'W', '_', '_', '_', 'W', '_', '_', 'W', 'W', '_', '_'],
            ['_', '_', 'W', '_', '_', '_', '_', 'W', '_', '_', '_', '_', 'W', '_'],
            ['_', '_', '_', 'W', '_', '_', '_', '_', 'W', '_', 'W', '_', 'W', '_'],
            ['_', 'W', '_', 'W', '_', 'W', 'W', 'W', '_', '_', 'W', '_', 'W', '_'],
            ['_', 'W', '_', '_', 'W', '_', '_', '_', '_', '_', 'W', 'W', '_', '_'],
            ['_', '_', 'W', 'W', '_', 'W', 'W', 'W', 'W', 'W', '_', '_', '_', '_'],
            ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', 'W', '_', '_']
        ],
        'instructions': 
"Oh no, codebot is really lost now!\n\n\
Give him some instructions to help him navigate the maze\n\
and reach his goal.",
        'startCode': '//Write your code here!'
    }
}

@app.route('/<level>')
def hello_world(level):
    return render_template('index.html', grid=WORLDS[level])

@app.route('/levels')
@app.route('/')
def hello_world_2():
    return render_template('challenges.html',
                           levels=[{'tag': k, 'name': WORLDS[k]["name"]} for k in sorted(list(WORLDS.keys()))])
