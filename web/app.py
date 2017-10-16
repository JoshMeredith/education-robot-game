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
        'skin': 'stone',
        'numRows': 5,
        'numCols': 3,
        'start': {'row': 5, 'col': 1},
        'startDir': 'Up',
        'goals': [{'row': 4, 'col': 1}, {'row': 2, 'col': 3}],
        'grid': [
            ['_', '_', '_'],
            ['_', 'W', '_'],
            ['_', '_', '_'],
            ['_', 'W', '_'],
            ['_', '_', '_'],
        ],
        'instructions':
"""Codebot is growing up and has upgraded his instructions!

Codebot no longer knows how to moveLeft, moveUp, moveDown or moveRight!
Instead, you can use the turnLeft and turnRight instructions to get him to turn
on the spot, and the walkForward instruction to get him to move one square in
the direction he is facing.

Give it a go!""",
        'startCode': 
"""// You can uncomment the instructions below to see what Codebot does with each
// of these instructions!
//
// turnLeft;
// turnRight;
// walkForward;
//
// Now, comment or delete those lines, and write your code below, using only
// these three instructions!
//
// Your code here!""",
    },

    'level12': {
        'name': 'Level 12',
        'skin': 'stone',
        'numRows': 7,
        'numCols': 5,
        'start': {'row': 1, 'col': 1},
        'startDir': 'Down',
        'goals': [{'row': 1, 'col': 5}, {'row': 7, 'col': 1}],
        'grid': [
            ['_', '_', '_', '_', '_'],
            ['_', 'W', 'W', 'W', 'W'],
            ['_', 'W', 'W', 'W', 'W'],
            ['_', 'W', 'W', 'W', 'W'],
            ['_', 'W', 'W', 'W', 'W'],
            ['_', 'W', 'W', 'W', 'W'],
            ['_', 'W', 'W', 'W', 'W'],
        ],
        'instructions':
"""Oops! Codebot is a slow learner and has temporarily forgotten how to
turnRight (just for this level!).

Help him find his lost gears only using the turnLeft and walkForward
instructions.""",
        'startCode': """// Your code here!""",
    },

    'level13': {
        'name': 'Level 13',
        'skin': 'stone',
        'numRows': 4,
        'numCols': 5,
        'start': {'row': 4, 'col': 4},
        'startDir': 'Down',
        'goals': [{'row': 4, 'col': 2}, {'row': 2, 'col': 2},
            {'row': 2, 'col': 3}],
        'grid': [
            ['_', '_', '_', 'W', 'W'],
            ['L', '_', '_', '_', '_'],
            ['W', '_', '_', '_', '_'],
            ['_', '_', 'L', '_', 'L'],
        ],
        'instructions':
"""Codebot has also learned to detect if walking forwards is safe. If you type

if (clearInFront?) {
    // Some commands here!
}

those commands will only be run if Codebot can safely take a step forwards,
right now.  Otherwise, nothing will happen.  Instead, if you typed

if (clearInFront?) {
    // Some commands here!
} else {
    // More commands here!
}

Codebot will do "Some commands" if walking forwards is safe (right now), or
otherwise he will do "More commands" instead. We call this idea 'branching'.

By combining branching with a times loop, we can write some neat, concise code
for Codebot. Try uncommenting the code below to see what Codebot does! Can you
explain why?
""",
        'startCode': 
"""// Codebot has learned how to check if it's safe to walk forwards!
// Try this code!
// times (10) {
//     if (clearInFront?) {
//         walkForward;
//     } else {
//         turnLeft;
//     }
// }""",
    },

    'level14': {
        'name': 'Level 14',
        'skin': 'stone',
        'numRows': 15,
        'numCols': 15,
        'start': {'row': 15, 'col': 1},
        'startDir': 'Right',
        'goals': [{'row': 1, 'col': 15}],
        'grid': [
            ['L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', '_', '_', '_', '_', '_'],
            ['L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', '_', '_', '_', '_', '_', '_', '_'],
            ['L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', '_', '_', '_', '_', 'L', 'L', 'L'],
            ['L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', '_', '_', 'L', 'L', 'L', 'L', 'L'],
            ['L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', '_', 'L', 'L', 'L', 'L', 'L', 'L'],
            ['L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', '_', 'L', 'L', 'L', 'L', 'L', 'L'],
            ['L', 'L', 'L', 'L', 'L', 'L', '_', '_', '_', 'L', 'L', 'L', 'L', 'L', 'L'],
            ['L', 'L', 'L', 'L', 'L', 'L', '_', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L'],
            ['L', 'L', 'L', 'L', 'L', '_', '_', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L'],
            ['L', 'L', 'L', 'L', 'L', '_', '_', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L'],
            ['L', 'L', 'L', '_', '_', '_', '_', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L'],
            ['L', 'L', 'L', '_', '_', '_', '_', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L'],
            ['L', 'L', 'L', '_', '_', '_', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L'],
            ['_', '_', '_', '_', '_', '_', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L'],
            ['_', '_', '_', '_', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L'],
        ],
        'instructions':
"""Oh no! Codebot has found himself very far away from his gear, surrounded by
walls and treacherous lava. Help him recover his gear.

Hint: try and combine nested loops with branching to see if you can devise a
short and clever solution.""",
        'startCode':
"""// Codebot needs your help!
// Write some code below to help him find his missing gear!""",
    },
    
    'level15': {
        'name': 'Level 15',
        'skin': 'stone',
        'numRows': 15,
        'numCols': 15,
        'start': {'row': 10, 'col': 9},
        'startDir': 'Down',
        'goals': [{'col': 4, 'row': 1}, {'col': 1, 'row': 12}, {'col': 5, 'row': 9}, {'col': 8, 'row': 12}, {'col': 8, 'row': 15}, {'col': 13, 'row': 7}, {'col': 12, 'row': 15}, {'col': 14, 'row': 4}, {'col': 2, 'row': 13}, {'col': 6, 'row': 10}, {'col': 1, 'row': 6}, {'col': 7, 'row': 3}, {'col': 10, 'row': 12}, {'col': 1, 'row': 14}, {'col': 6, 'row': 15}, {'col': 3, 'row': 6}, {'col': 11, 'row': 2}, {'col': 15, 'row': 15}, {'col': 9, 'row': 13}, {'col': 13, 'row': 3}, {'col': 4, 'row': 7}, {'col': 11, 'row': 9}, {'col': 13, 'row': 13}, {'col': 11, 'row': 7}, {'col': 10, 'row': 4}, {'col': 1, 'row': 10}, {'col': 3, 'row': 4}, {'col': 8, 'row': 1}, {'col': 4, 'row': 5}, {'col': 10, 'row': 10}, {'col': 9, 'row': 2}, {'col': 15, 'row': 6}, {'col': 15, 'row': 9}, {'col': 8, 'row': 7}, {'col': 5, 'row': 11}, {'col': 14, 'row': 10}, {'col': 2, 'row': 1}, {'col': 10, 'row': 15}, {'col': 2, 'row': 5}, {'col': 15, 'row': 13}, {'col': 4, 'row': 10}, {'col': 9, 'row': 11}, {'col': 1, 'row': 8}, {'col': 10, 'row': 8}, {'col': 15, 'row': 3}, {'col': 1, 'row': 4}, {'col': 5, 'row': 6}],
        'grid': [
            ['L', '_', 'L', '_', 'L', '_', '_', '_', 'L', 'L', 'L', '_', '_', '_', '_'],
            ['_', '_', '_', '_', '_', '_', 'L', 'L', '_', 'L', '_', '_', 'L', 'L', '_'],
            ['_', 'L', 'L', 'L', '_', 'L', '_', '_', '_', 'L', 'L', '_', '_', 'L', '_'],
            ['_', 'L', '_', '_', '_', '_', 'L', '_', 'L', '_', 'L', '_', 'L', '_', 'L'],
            ['L', '_', 'L', '_', 'L', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
            ['_', '_', '_', 'L', '_', '_', 'L', 'L', 'L', 'L', '_', 'L', 'L', 'L', '_'],
            ['L', '_', 'L', '_', 'L', '_', 'L', '_', '_', 'L', '_', 'L', '_', 'L', 'L'],
            ['_', '_', 'L', '_', '_', '_', '_', 'L', '_', '_', 'L', 'L', '_', '_', '_'],
            ['L', '_', '_', 'L', '_', 'L', '_', 'L', '_', 'L', '_', '_', '_', 'L', '_'],
            ['_', 'L', '_', '_', 'L', '_', '_', '_', '_', '_', 'L', '_', 'L', '_', 'L'],
            ['_', '_', '_', 'L', '_', 'L', '_', 'L', '_', 'L', '_', '_', '_', '_', '_'],
            ['_', 'L', '_', 'L', '_', '_', '_', '_', 'L', '_', '_', 'L', 'L', 'L', '_'],
            ['L', '_', '_', 'L', 'L', '_', 'L', 'L', '_', 'L', '_', 'L', '_', 'L', '_'],
            ['_', 'L', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', 'L'],
            ['_', '_', '_', 'L', 'L', '_', 'L', '_', 'L', '_', 'L', '_', 'L', '_', '_'],
        ],
        'instructions':
"""Codebot went for a walk in the woods and accidentally left many gears behind!
Help him retrace his steps and recover each gear. Watch out! Make sure you keep
him away from that lava.

Psst. He's in a panic, so he'd really like it if you could keep your code
concise so he has less to remember ;).""",
        'startCode': '// Your goes code here!',
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
