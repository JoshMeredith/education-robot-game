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
    },

    'level6': {
        'name': 'Level 6',
        'skin': 'sand',
        'numRows': 7,
        'numCols': 7,
        'start': {'row': 0, 'col': 3},
        'startDir': 'Up',
        'goals': [{'row': 0, 'col': 0}, {'row': 6, 'col': 6}],
        'grid': [
            ['_', '_', '_', '_', '_', '_', '_'],
            ['_', '_', '_', '_', '_', '_', '_'],
            ['_', '_', '_', '_', '_', '_', '_'],
            ['_', '_', '_', '_', '_', '_', '_'],
            ['_', '_', '_', '_', '_', '_', '_'],
            ['_', '_', '_', '_', '_', '_', '_'],
            ['_', '_', '_', '_', '_', '_', '_']
        ],
        'instructions':
"In programming, it is generally important to recognize patterns and to look for \n\
most effective soution, allowing you to keep your code short. As an example, the \n\
maze on the right could be solved by collecting the top right gear, then the bottom \n\
left one, then bottom right, then top left, but this would require a lot of steps.\n\
Instead, you can solve this maze with four simple loops. See if you can figure out how.",
        'startCode': '//Write your code here!'
    },

    'level7': {
        'name': 'Level 7',
        'skin': 'sand',
        'numRows': 8,
        'numCols': 9,
        'start': {'row': 7, 'col': 0},
        'startDir': 'Up',
        'goals': {'row': 0, 'col': 9},
        'grid': [
            ['_', '_', '_', 'W', '_', '_', '_', 'W', '_'],
            ['_', 'W', '_', 'W', '_', 'W', '_', 'W', '_'],
            ['_', 'W', '_', 'W', '_', 'W', '_', 'W', '_'],
            ['_', 'W', '_', 'W', '_', 'W', '_', 'W', '_'],
            ['_', 'W', '_', 'W', '_', 'W', '_', 'W', '_'],
            ['_', 'W', '_', 'W', '_', 'W', '_', 'W', '_'],
            ['_', 'W', '_', 'W', '_', 'W', '_', 'W', '_'],
            ['_', 'W', '_', '_', '_', 'W', '_', '_', '_']
        ],
        'instructions':
"A useful thing you can do is 'nest' loops inside each other. \n\
Here is an example:\n\
times (3) {\n\
    times(2) {\n\
        moveUp;\n\
    }\n\
    times(3) {\n\
        moveRight;\n\
    }\n\
}\n\
The outer loop will run three times, each time, it will make codeBot moveUp twice,\n\
then make him move right three times before repeating. Use something similar to solve\n\
this maze.",
        'startCode': '//Write your code here!'
    },

    'level8': {
        'name': 'Level 8',
        'skin': 'sand',
        'numRows': 9,
        'numCols': 9,
        'start': {'row': 0, 'col': 0},
        'startDir': 'Up',
        'goals': {'row': 5, 'col': 5},
        'grid': [
            ['_', '_', '_', '_', '_', '_', '_', '_', '_'],
            ['_', 'W', 'W', 'W', 'W', 'W', 'W', 'W', '_'],
            ['_', 'W', '_', '_', '_', '_', '_', 'W', '_'],
            ['_', 'W', '_', 'W', 'W', 'W', '_', 'W', '_'],
            ['_', 'W', '_', 'W', '_', 'W', '_', 'W', '_'],
            ['_', 'W', '_', 'W', '_', 'W', '_', 'W', '_'],
            ['_', 'W', '_', 'W', '_', '_', '_', 'W', '_'],
            ['_', 'W', '_', 'W', 'W', 'W', 'W', 'W', '_'],
            ['_', 'W', '_', '_', '_', '_', '_', '_', '_']
        ],
        'instructions':
"Try ",
        'startCode': '//Write your code here!'
    },

    'level9': {
        'name': 'Level 9',
        'skin': 'sand',
        'numRows': 12,
        'numCols': 12,
        'start': {'row': 0, 'col': 3},
        'startDir': 'Up',
        'goals': [{'row': 0, 'col': 0}, {'row': 6, 'col': 6}],
        'grid': [
            ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
            ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
            ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
            ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
            ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
            ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
            ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
            ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
            ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
            ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
            ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
            ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_']
        ],
        'instructions':
"A final example.",
        'startCode': '//Write your code here!'
    },
}

@app.route('/<level>')
def hello_world(level):
    return render_template('index.html', grid=WORLDS[level])

@app.route('/levels')
@app.route('/')
def hello_world_2():
    return render_template('challenges.html',
                           levels=[{'tag': k, 'name': WORLDS[k]["name"]} for k in sorted(list(WORLDS.keys()))])
