from flask import Flask, render_template, session, request
from flask import session
# from VideoFrames import all_frames
# import sim
# import PDF_Image


DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f355151353511f2b6176a'



@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/map')
def map():
    # dic = all_frames

    dic = {'slide_3.png': 69300, 'slide_1.png': 15300, 'slide_0.png': 0, 'slide_2.png': 55800}
    l = [list(dic.keys()),dic]
    return render_template('player.html', result=l)


if __name__ == "__main__":
    app.run()
