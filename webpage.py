from flask import Flask, render_template, session, request
from flask import session

DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f355151353511f2b6176a'



@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/map')
def index():
    return render_template('player.html', json)