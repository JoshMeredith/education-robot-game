from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('js-test.html', dat={'apple': 'correct!'})
