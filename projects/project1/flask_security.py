import os
from flask import Flask, url_for, request, render_template, redirect, Response
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
import io

UPLOAD_FOLDER = './files'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:*******@localhost/postgres'
db = SQLAlchemy(app)

variable = 'a'
image = None

# app.debug = True

class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(80), unique=True)

    def __init__(self,username):
        self.username = username

    def __repr__(self):
        return '<user %s>'%self.username



def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/about')
def about():

    return render_template('about.html')


@app.route('/')
def index():
    user = User.query.all()
    return render_template('home.html', myuser=user)

@app.route('/userlogin/')
def userlogin():

    return render_template('add_user.html')

@app.route('/toggle/')
def toggle():
    global variable
    variable = 'b'
    return render_template('result.html')

@app.route('/checkstatus/', methods=['GET'])
def checkstatus():
    global variable
    return variable

@app.route('/postdata/', methods= ['POST'])
def postdata():
    if request.method == 'POST':
        # check if the post request has the file part
        data = request.files['file']
        image = io.BytesIO(data)
    return "done"

@app.route('/video_feed')
def video_feed():
    global image
    result= image
    return Response(result,
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/userprofile/<username>')
def userprofile(username):

    user = User.query.filter_by(username=username).first()
    if user is not None:
        return render_template('profile.html',user=user)
    else:
        return redirect(url_for('userlogin'))

@app.route('/post_user', methods = ['POST'])
def post_user():
    user = User(request.form['username'])
    db.session.add(user)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:

            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':

            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('upload',
                                    filename=filename))
    return render_template('upload.html')




if __name__== "__main__":
    app.run() #host='0.0.0.0', debug=True
