from web.models import Level

WORLDS = {
    'World 1': [
        'level1',
        'level2',
        'level3',
        'level4',
        'level5',
    ],
    'World 2': [
        'level6',
        'level7',
        'level8',
        'level9',
        'level10',
    ],
    'World 3': [
        'level11',
        'level12',
        'level13',
        'level14',
        'level15',
    ],
}

LEVELS = {
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
"""A comment is a line of code that codebot will ignore.
To write a comment we use <tt> # </tt>and then write some text.

<pre>
#this is a comment
</pre>

Comments have 2 main uses that you will see over and over
during your time spent programming.
<ol>
<li>Describing what your code does</li>
<li>Toggling code on and off</li>
</ol>""",
        'startCode':
"""#The next line moves the robot to the goal, uncomment it and hit RUN
#moveRight;"""
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
"""In the last level you might have noticed that the line of
code had a semicolon (;) at the end.
This lets codebot know that you have finished giving an
instruction - kind of like how a full stop lets you know
when a sentence is finished.
This becomes important when you have many instructions to
give to codeBot. To complete this level uncomment the
instructions that will lead codebot to the goal.""",
        'startCode':
"""#moveUp;
#moveDown;
#moveLeft;
#moveRight;
#moveUp;
#moveDown;
#moveLeft;
#moveRight;"""
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
"""It can get pretty tiresome repeatedly typing out the same
instructions for codebot over and over again. That's why we
have the times loop!
By using the times loop we can tell codebot to follow a set
of instructions any number of times. The following code will
tell codebot to dance 10 times:
<pre>
times(10){
    dance;
}
</pre>
Unfortunately codebot hasn't learnt how to dance yet.
He has learnt how to move right though! Use your newfound
knowledge of loops to help codebot reach the goal.""",
        'startCode': '#Write your code here!'
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
"""Now we know how to move Codebot around using the <tt>moveUp</tt>,
<tt>moveDown</tt>, <tt>moveLeft</tt> and <tt>moveRight</tt> instructions. We also know
how to use loops to make our code shorter. 
Use these tools to help codebot reach the goal.""",
        'startCode': '#Write your code here!'
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
"""Oh no, codebot is really lost now!
Give him some instructions to help him navigate the maze
and reach his goal.""",
        'startCode': '#Write your code here!'
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
"""In programming, it is generally important to recognize patterns and to look for the 
most effective soutions, allowing you to keep your code short. 
As an example, the maze on the right could be solved by collecting the top right gear, 
then the bottom left one, then bottom right, then top left, but this would require a 
lot of steps. Instead, you can solve this maze with four simple loops. 
See if you can figure out how.""",
        'startCode': '#Write your code here!'
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
"""A useful thing you can do is 'nest' loops inside each other. 
Here is an example:
<pre>times (3) {
    times(2) {
        moveUp;
    }
    times(3) {
        moveRight;
    }
}
</pre>
The outer loop will run three times, each time, it will make Codebot <tt>moveUp</tt> twice,
then make him move right three times before repeating. Use something similar to solve
this maze.

<p>
Hint: Pay attention to what you need to repeat, in this case it looks like 
you need to move up a certain number of times, then right, then down, then right again, 
and repeat this as many times as necessary until you reach the goal
</p>""",
        'startCode': '#Write your code here!'
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
"""Here's an example similar to the last one but longer, just to show you how important
loops can be. Also be careful, the walls have been replaced with cactuses so Codebot will get
hurt if you're not careful.

<p>
Hint: The grid is 15 by 15, so you will have to step up and 
down 14 times every time you moveUp or moveDown
</p>""",
        'startCode': '#Write your code here!'
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
"""This is similar to the previous situation, but you have to figure the pattern out
on your own this time!

<p>
Note that it is OK for you to tell Codebot to move in a direction where there
is a wall if it keeps your code short. For example, a useful loop might get
codeBot to move up, right, down, and left 10 times each. He may awkwardly face
the wall for a while, but eventually he'll turn and walk in the right
direction.""",
        'startCode': '#Write your code here!'
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
"""In computer science, everyone likes money, so go collect as much of it as possible!""",
        'startCode': '#Write your code here!'
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

Codebot no longer knows how to <tt>moveLeft</tt>, <tt>moveUp</tt>, <tt>moveDown</tt> or <tt>moveRight</tt>!
Instead, you can use the <tt>turnLeft</tt> and <tt>turnRight</tt> instructions to get him to turn
on the spot, and the <tt>walkForward</tt> instruction to get him to move one square in
the direction he is facing.

Give it a go!""",
        'startCode': 
"""# You can uncomment the instructions below to see what Codebot does with each
# of these instructions!
#
# turnLeft;
# turnRight;
# walkForward;
#
# Now, comment or delete those lines, and write your code below, using only
# these three instructions!
#
# Your code here!""",
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
<tt>turnRight</tt> (just for this level!).

Help him find his lost gears only using the <tt>turnLeft</tt> and <tt>walkForward</tt>
instructions.""",
        'startCode': """# Your code here!""",
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

<pre>
if (clearInFront?) {
    # Some commands here!
}
</pre>

those commands will only be run if Codebot can safely take a step forwards,
right now.  Otherwise, nothing will happen.  Instead, if you typed

<pre>
if (clearInFront?) {
    # Some commands here!
} else {
    # More commands here!
}
</pre>

Codebot will do "Some commands" if walking forwards is safe (right now), or
otherwise he will do "More commands" instead. We call this idea <i>branching</i>.

<p>
By combining branching with a times loop, we can write some neat, concise code
for Codebot. Try uncommenting the code below to see what Codebot does! Can you
explain why?
</p>
""",
        'startCode': 
"""# Codebot has learned how to check if it's safe to walk forwards!
# Try this code!
# times (10) {
#     if (clearInFront?) {
#         walkForward;
#     } else {
#         turnLeft;
#     }
# }""",
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

<p>
Hint: try and combine nested loops with branching to see if you can devise a
short and clever solution.
</p>""",
        'startCode':
"""# Codebot needs your help!
# Write some code below to help him find his missing gear!""",
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

<p>
Psst. He's in a panic, so he'd really like it if you could keep your code
concise so he has less to remember ;).
</p>""",
        'startCode': '# Your goes code here!',
    },
}

def update_levels(db):
    to_create = []
    for codename, level in LEVELS.items():
        db_level = db.session.query(Level.id).filter_by(codename=codename).scalar()
        if not db_level:
            to_create.append(Level(codename=codename, title=level['name']))

    for l in to_create:
        db.session.add(l)
    db.session.commit()
    all_levels = Level.query.all()
