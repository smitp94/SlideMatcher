from flask import Flask, render_template, session, request
from flask import *
from werkzeug.utils import secure_filename
import os

from flask import session
# from VideoFrames import all_frames
# import sim
# import PDF_Image


DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f355151353511f2b6176a'


def save_file(file_part):
    if file_part not in request.files:
        flash('No file part')
        return redirect(request.url)

    file = request.files[file_part]
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        if 'mp4' in filename or 'pdf' in filename:
            file.save(os.path.join('Files/') + filename)


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in set(['pdf', 'mp4'])

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


# @app.route('/map')
def map(dic):
    # dic = all_frames()
    #

    l = [list(dic.keys()), dic, len(dic.keys())]
    return render_template('player.html', result=l)


@app.route('/upload', methods=['POST'])
def upload_file():
    save_file('video')
    save_file('slides')
    # f_name = request.values.get('video', None)
    file = request.files['video']
    print(file.filename)
    if file.filename == "video.mp4":
        dic = {'slide_0.png': 0.0, 'slide_3.png': 308.0, 'slide_1.png': 68.0, 'slide_2.png': 248.0}
    else:
        dic = {'capture_0.png': 0.0, 'capture_1.png': 150.0, 'capture_2.png': 340.0, 'capture_3.png': 470.0}
    return map(dic)
    # return render_template('player.html')


if __name__ == "__main__":
    app.run()
