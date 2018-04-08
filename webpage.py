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
    # dic = all_frames()
    #
    dic = {'slide_0.png': 0.0, 'slide_3.png': 308.0, 'slide_1.png': 68.0, 'slide_2.png': 248.0}
    l = [list(dic.keys()), dic, len(dic.keys())]
    return render_template('player.html', result=l)


if __name__ == "__main__":
    app.run()
