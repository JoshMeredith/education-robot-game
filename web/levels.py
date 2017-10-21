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
        'badge_thresholds': {
            'code_score': 1,
            'execution_score': 2,
        },
        'instructions':
<p>Welcome to the first level of Codebot!</p>

<p>
In each level, you will see Codebot on a grid. He loves collecting gears and
would like to move around and pick all of them up. He's not very clever and so
he'd like you to help him! He wants you to tell him how to move around, by
writing some instructions (which we sometimes call <i>code</i>) in his codebox
below.  Code is usually laid out in <i>lines</i>.
</p>

<p>
Each level will start with some comments in the codebox. A comment is a line of
code that starts with a hash (<tt>#</tt>). Codebot will ignore all the code that
comes after a hash on a line, for example:
</p>

<p>
<pre>
# This is a comment
</pre>
</p>

<p>
Try following the instructions in the comments below to help Codebot find his
first gear!
</p>
""",
        'startCode':
"""# Codebot knows how to move to the right!
# Uncomment the last line by removing the hash, then click Run!
# to help him collect his first gear!
#
# You can also click reset at any time to reset the grid and
# Codebot to where they were before.
#
# moveRight;""",
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
        'badge_thresholds': {
            'code_score': 4,
            'execution_score': 6,
        },
        'instructions':
"""
<p>
In the previous level you might have noticed that the line of code had a
semicolon (<tt>;</tt>) on the end. This lets Codebot know that you have finished
giving him an instruction - kind of like how a full stop lets you know when a
sentence is finished.
</p>

<p>
Semicolons become important when you have many instructions to
give to Codebot. 
</p>
""",
        'startCode':
"""# Codebot also knows how to move up, down, left and right.
# Uncomment all the lines below and click Run! to see Codebot
# move about! After that, try changing these lines (possibly
# removing a few) to guide Codebot to the gear.
#
# moveUp;
# moveDown;
# moveLeft;
# moveRight;
# moveUp;
# moveDown;
# moveLeft;
# moveRight;"""
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
        'badge_thresholds': {
            'code_score': 2,
            'execution_score': 11,
        },
        'instructions':
"""
<p>
Sometimes we'll want Codebot to perform the same sequence of actions over and
over again, some number of times. Instead of writing the same thing out each
time, we can use the special <tt>times</tt> command to ask Codebot to follow a
set of instructions any number of times. We call this a <i>loop</i>. The
following code will tell Codebot to <tt>dance</tt> and <tt>moveRight</tt> ten
times, in alternation.
</p>

<p>
<pre>
# We call this a "times" loop.
times (10) {
    # We often shift (indent) the code inside a loop
    # so we can easily read and see which instructions
    # are being repeated;
    dance;
    # Everything between the { and the } (the curly
    # braces) will be repeated 10 times, in order!
    moveRight;
}
</pre>
</p>

<p>
Unfortunately Codebot hasn't learnt how to <tt>dance</tt> yet.  However, he does
know how to <tt>moveRight</tt> though! Use your newfound knowledge of loops to
help Codebot reach the gear.
</p>""",
        'startCode': '# Write your code here!'
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
        'badge_thresholds': {
            'code_score': 6,
            'execution_score': 11,
        },
        'instructions':
"""
<p>
Now we know how to move Codebot around using the <tt>moveUp</tt>,
<tt>moveDown</tt>, <tt>moveLeft</tt> and <tt>moveRight</tt> instructions. We also know
how to use loops to make our code shorter. 
</p>

<p>
Try using these tools to help Codebot reach the goal. What happens if Codebot
tries walking into a wall? How short can you make your code?
</p>

<p>
If your code is short enough, you'll receive a blue badge for this level! You
can always go back and re-do previous levels to earn more badges by using the
level selector.
</p>""",
        'startCode': '# Write your code here!'
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
        'badge_thresholds': {
            'code_score': 20,
            'execution_score': 84,
        },
        'instructions':
"""
<p>
Oh no, Codebot is really lost now!
</p>

<p>
Give him some instructions to help him navigate through the grid and pick up
both gears.
</p>

<p>
<i>Pssst</i>, let me let you in on a little secret! Codebot hates walking and
likes finding gears quickly, so he'll give you a special red badge for this
level if you help him finish it fast enough! Just like with the blue badge, you
can always go back to previous levels to earn any badges you've missed.
</p>
""",
        'startCode': '# Write your code here!'
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
        'badge_thresholds': {
            'code_score': 8,
            'execution_score': 25,
        },
        'instructions':
"""
<p>
Codebot has become very ambitious. He's heard that there are many more gears to
be found in the desert than the grassy fields around his home... and he's
dragged his new best friend (ahem, <i>you</i>) to help him find them.
</p>

<p>
The same commands work here as before, so start by helping him pick up the four
gears in the corners of this grid.
</p>
""",
        'startCode': '# Write your code here!'
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
        'badge_thresholds': {
            'code_score': 7,
            'execution_score': 51,
        },
        'instructions':
"""
<p>
Walking on sand is quite repetitive and so Codebot would like to give you a tip to
help write concise code for him.
</p>

<p>
He suggests that a cool thing you can do is 'nest' loops inside each other. 
Here is an example:

<p>
<pre>
# Putting loops inside other loops is called "nesting".
#
# We call this the "outer" loop.
times (3) {
    # This is an "inner" loop.
    times(2) {
        moveUp;
    }
    # This is another "inner" loop.
    times(3) {
        moveRight;
    }
}
</pre>
</p>

<p>
Codebot will run the outer loop three times. Each time, he will <tt>moveUp</tt>
twice, then <tt>moveRight</tt> three times before repeating it all again. He'd
like you to use something similar to help him find the gear in this grid.
</p>

<p>
<i>Hint</i>: Think about what pattern you can repeat here, then think about how you can
use loops to construct that pattern!
</p>""",
        'startCode': '# Write your code here!'
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
        'badge_thresholds': {
            'code_score': 9,
            'execution_score': 127,
        },
        'instructions':
"""
<p>
Here's an example similar to the last one but a little longer, just to show you
how important loops can be. But be careful of the poisonous cacti! Codebot will
get hurt if he walks into one!
</p>

<p>
<i>Hint</i>: The grid is 15 by 15, so you will have to step up and down 14 times
every time you <tt>moveUp</tt> or <tt>moveDown</tt> from one end of the grid to
the other.
</p>""",
        'startCode': '# Write your code here!'
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
        'badge_thresholds': {
            'code_score': 7,
            'execution_score': 261,
        },
        'instructions':
"""
<p>
Codebot's in a dizzy spiral! Help him reach the gear with some short code!
</p>

<p>
<i>Hint</i>: remember what happens when you ask Codebot to walk into a wall? How
might you use that to earn yourself a blue badge?
</p>
""",
        'startCode': '# Write your code here!'
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
        'badge_thresholds': {
            'code_score': 7,
            'execution_score': 32,
        },
        'instructions':
"""
<p>
Codebot is in his happy place - he's completely surrounded by gears! Help him
pick them all up.
</p>
""",
        'startCode': '# Write your code here!'
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
        'badge_thresholds': {
            'code_score': 5,
            'execution_score': 7,
        },
        'instructions':
"""
<p>
Codebot was enjoying himself walking around the desert when he didn't see where
he was going (although he blames his assistant, i.e. <i>you</i>!) and fell into
a cave! He hit his head so hard that he forgot all his instructions: he
no longer knows how to <tt>moveLeft</tt>, <tt>moveUp</tt>, <tt>moveDown</tt> or
even <tt>moveRight</tt>!
</p>

<p>
After dusting off his rusty arms, he slowly learned to move around once more,
but this time with some new instructions: you can now use the <tt>turnLeft</tt>
and <tt>turnRight</tt> instructions to get him to turn on the spot, and the
<tt>walkForward</tt> instruction to get him to move one square in the direction
he is facing.
</p>

Give it a go and help him pick up these two gears.""",
        'startCode': 
"""# You can uncomment the instructions below to see what Codebot
# does with each of these instructions!
#
# turnLeft;
# turnRight;
# walkForward;
#
# Now, comment or delete those lines, and write your code below,
# using only these three types of instructions!
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
        'badge_thresholds': {
            'code_score': 5,
            'execution_score': 18,
        },
        'instructions':
"""
<p>
Oops! Codebot fell down again and has temporarily forgotten how to
<tt>turnRight</tt> (just for this level!).
</p>

<p>
Help him find the two gears using only the <tt>turnLeft</tt> and
<tt>walkForward</tt> instructions.
</p>
""",
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
        'badge_thresholds': {
            'code_score': 4,
            'execution_score': 10,
        },
        'instructions':
"""
<p>
Codebot's learned a new skill! He can now detect if walking forwards is safe.
For instance, if you type

<p>
<pre>
if (clearInFront?) {
    # Some commands here!
}
</pre>
</p>

<p>
those commands will only be run if Codebot can safely take a step forwards,
right now.  Otherwise, nothing will happen.  Instead, if you typed
</p>

<p>
<pre>
if (clearInFront?) {
    # Some commands here!
} else {
    # More commands here!
}
</pre>
</p>

<p>
Codebot will do "Some commands" if walking forwards is safe (right now), or
otherwise he will do "More commands" instead. We call this idea <i>branching</i>.
</p>

<p>
By combining branching with a <tt>times</tt> loop, we can write some neat,
concise code for Codebot. Try uncommenting the code below to see what Codebot
does! Can you explain why?
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
        'badge_thresholds': {
            'code_score': 9,
            'execution_score': 35,
        },
        'instructions':
"""
<p>
Oh no! Codebot has found himself very far away from the gear, surrounded by
walls and treacherous lava (if he walks in, he'll melt! Aaaaaaarrrrh).
Help him get to gear and avoid the fiery staircase.
</p>

<p>
<i>Hint</i>: try and combine nested loops with branching to see if you can
devise a short and clever solution. By the way, Codebot thinks those badges look
great on you!
</p>""",
        'startCode':
"""# Write some code below to help Codebot find his missing gear!""",
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
        'badge_thresholds': {
            'code_score': 15,
            'execution_score': 831,
        },
        'instructions':
"""
<p>
Codebot wandered deep into a cave and found many gears stashed away in every
corner! Help him collect each gear. But watch out! Make sure you keep
him away from that lava.
</p>

<p>
<i>Pssst</i>. I didn't tell you this but... he's getting a little <i>rusty</i>
(if you know what I mean) and his memory isn't what it used to be. Sooo he'd
really like it if you could keep your code short and concise so he has less to
remember.  <i>I'll</i> give you a badge if you write some short code and don't
tell him anything. <i>"Tell him what?"</i> you ask? Exaaaactly.
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
