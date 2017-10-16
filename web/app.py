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
        'start': {'row': 1, 'col': 4},
        'startDir': 'Down',
        'goals': [{'row': 1, 'col': 1}, {'row': 1, 'col': 7}, {'row': 7, 'col': 1}, {'row': 7, 'col': 7}],
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
"In programming, it is generally important to recognize patterns and to look for the \n\
most effective soutions, allowing you to keep your code short. \n\n\
As an example, the maze on the right could be solved by collecting the top right gear, \n\
then the bottom left one, then bottom right, then top left, but this would require a \n\
lot of steps. Instead, you can solve this maze with four simple loops. \n\n\
See if you can figure out how.",
        'startCode': '//Write your code here!'
    },

    'level7': {
        'name': 'Level 7',
        'skin': 'sand',
        'numRows': 8,
        'numCols': 9,
        'start': {'row': 8, 'col': 1},
        'startDir': 'Up',
        'goals': [{'row': 1, 'col': 9}],
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
this maze. (Hint: Pay attention to what you need to repeat, in this case it looks like \n\
you need to move up a certain number of times, then right, then down, then right again, \n\
and repeat this as many times as necessary until you reach the goal)",
        'startCode': '//Write your code here!'
    },

    'level8': {
        'name': 'Level 8',
        'skin': 'sand',
        'numRows': 15,
        'numCols': 15,
        'start': {'row': 1, 'col': 15},
        'startDir': 'Up',
        'goals': [{'row': 15, 'col': 1}],
        'grid': [
            ['_', 'L', '_', '_', '_', 'L', '_', '_', '_', 'L', '_', '_', '_', 'L', '_'],
            ['_', 'L', '_', 'L', '_', 'L', '_', 'L', '_', 'L', '_', 'L', '_', 'L', '_'],
            ['_', 'L', '_', 'L', '_', 'L', '_', 'L', '_', 'L', '_', 'L', '_', 'L', '_'],
            ['_', 'L', '_', 'L', '_', 'L', '_', 'L', '_', 'L', '_', 'L', '_', 'L', '_'],
            ['_', 'L', '_', 'L', '_', 'L', '_', 'L', '_', 'L', '_', 'L', '_', 'L', '_'],
            ['_', 'L', '_', 'L', '_', 'L', '_', 'L', '_', 'L', '_', 'L', '_', 'L', '_'],
            ['_', 'L', '_', 'L', '_', 'L', '_', 'L', '_', 'L', '_', 'L', '_', 'L', '_'],
            ['_', 'L', '_', 'L', '_', 'L', '_', 'L', '_', 'L', '_', 'L', '_', 'L', '_'],
            ['_', 'L', '_', 'L', '_', 'L', '_', 'L', '_', 'L', '_', 'L', '_', 'L', '_'],
            ['_', 'L', '_', 'L', '_', 'L', '_', 'L', '_', 'L', '_', 'L', '_', 'L', '_'],
            ['_', 'L', '_', 'L', '_', 'L', '_', 'L', '_', 'L', '_', 'L', '_', 'L', '_'],
            ['_', 'L', '_', 'L', '_', 'L', '_', 'L', '_', 'L', '_', 'L', '_', 'L', '_'],
            ['_', 'L', '_', 'L', '_', 'L', '_', 'L', '_', 'L', '_', 'L', '_', 'L', '_'],
            ['_', 'L', '_', 'L', '_', 'L', '_', 'L', '_', 'L', '_', 'L', '_', 'L', '_'],
            ['_', '_', '_', 'L', '_', '_', '_', 'L', '_', '_', '_', 'L', '_', '_', '_'],
        ],
        'instructions':
"Here's an example similar to the last one but longer, just to show you how important\n\
loops can be. Also be careful, the walls have been replaced with lava so codeBot will get\n\
hurt if you're not careful. (Hint: The grid is 15 by 15, so you will have to step up and \n\
down 15 times every time you moveUp or moveDown)",
        'startCode': '//Write your code here!'
    },


    'level9': {
        'name': 'Level 9',
        'skin': 'sand',
        'numRows': 9,
        'numCols': 9,
        'start': {'row': 9, 'col': 1},
        'startDir': 'Up',
        'goals': [{'row': 5, 'col': 5}],
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
"This is similar to the previous situation, but you have to figure the pattern out\n\
on your own this time! Note that it is ok for you to tell codeBot to move in a direction\n\
where there is a wall if it keeps your code short. For example, a useful loop might be to \n\
just get codeBot to move in sets up, right, down, and left 10 times each. He may awkwardly\n\
face the wall for a while, but eventually he'll turn and walk in the right direction.",
        'startCode': '//Write your code here!'
    },

    'level10': {
        'name': 'Level 10',
        'skin': 'sand',
        'numRows': 5,
        'numCols': 5,
        'start': {'row': 1, 'col': 1},
        'startDir': 'Down',
        'goals': [{'row': 1, 'col': 2}, {'row': 1, 'col': 3}, {'row': 1, 'col': 4}, {'row': 1, 'col': 5},
                  {'row': 2, 'col': 1}, {'row': 2, 'col': 2}, {'row': 2, 'col': 3}, {'row': 2, 'col': 4}, {'row': 2, 'col': 5},
                  {'row': 3, 'col': 1}, {'row': 3, 'col': 2}, {'row': 3, 'col': 3}, {'row': 3, 'col': 4}, {'row': 3, 'col': 5},
                  {'row': 4, 'col': 1}, {'row': 4, 'col': 2}, {'row': 4, 'col': 3}, {'row': 4, 'col': 4}, {'row': 4, 'col': 5},
                  {'row': 5, 'col': 1}, {'row': 5, 'col': 2}, {'row': 5, 'col': 3}, {'row': 5, 'col': 4}, {'row': 5, 'col': 5}],
        'grid': [
            ['_', '_', '_', '_', '_', '_'],
            ['_', '_', '_', '_', '_', '_'],
            ['_', '_', '_', '_', '_', '_'],
            ['_', '_', '_', '_', '_', '_'],
            ['_', '_', '_', '_', '_', '_'],
            ['_', '_', '_', '_', '_', '_']
        ],
        'instructions':
"In computer science, everyone likes money, so go collect as much of it as possible!",
        'startCode': '//Write your code here!'
    },

    'level11': {
        'name': 'Level 11',
        'skin': 'sand',
        'numRows': 25,
        'numCols': 16,
        'start': {'row': 1, 'col': 16},
        'startDir': 'Up',
        'goals': [{'row': 10, 'col': 3}],
        'grid': [
            ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
            ['_', 'W', 'W', '_', 'W', '_', 'W', 'W', '_', 'W', '_', 'W', '_', '_', '_', '_'],
            ['_', 'W', '_', '_', '_', '_', 'W', '_', '_', 'W', 'W', '_', '_', '_', '_', '_'],
            ['_', 'W', 'W', '_', 'W', '_', 'W', '_', '_', 'W', '_', '_', '_', '_', '_', '_'],
            ['_', '_', 'W', '_', 'W', '_', 'W', '_', '_', 'W', 'W', '_', '_', '_', '_', '_'],
            ['_', 'W', 'W', '_', 'W', '_', 'W', 'W', '_', 'W', '_', 'W', '_', '_', '_', '_'],
            ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
            ['_', 'W', 'W', 'W', '_', 'W', 'W', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
            ['_', 'W', '_', 'W', '_', 'W', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
            ['_', 'W', '_', 'W', '_', 'W', 'W', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
            ['_', 'W', '_', 'W', '_', 'W', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
            ['_', 'W', 'W', 'W', '_', 'W', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
            ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
            ['_', 'W', 'W', 'W', '_', 'W', '_', 'W', '_', 'W', '_', 'W', 'W', '_', '_', '_'],
            ['_', '_', 'W', '_', '_', 'W', '_', 'W', '_', '_', '_', 'W', '_', '_', '_', '_'],
            ['_', '_', 'W', '_', '_', 'W', 'W', 'W', '_', 'W', '_', 'W', 'W', '_', '_', '_'],
            ['_', '_', 'W', '_', '_', 'W', '_', 'W', '_', 'W', '_', '_', 'W', '_', '_', '_'],
            ['_', '_', 'W', '_', '_', 'W', '_', 'W', '_', 'W', '_', 'W', 'W', '_', '_', '_'],
            ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
            ['_', 'W', 'W', '_', 'W', '_', '_', '_', 'W', '_', '_', 'W', 'W', '_', 'W', 'W'],
            ['_', 'W', '_', '_', 'W', '_', '_', 'W', '_', 'W', '_', 'W', '_', '_', 'W', '_'],
            ['_', 'W', '_', '_', 'W', '_', '_', 'W', 'W', 'W', '_', 'W', 'W', '_', 'W', 'W'],
            ['_', 'W', '_', '_', 'W', '_', '_', 'W', '_', 'W', '_', '_', 'W', '_', '_', 'W'],
            ['_', 'W', 'W', '_', 'W', 'W', '_', 'W', '_', 'W', '_', 'W', 'W', '_', 'W', 'W'],
            ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_']
        ],
        'instructions':
"",
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
