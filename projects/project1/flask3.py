import os
from flask import Flask, url_for, request, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = './files'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:********@localhost/postgres'
db = SQLAlchemy(app)


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
    ab = "Team Unicom Solutions is one of the 9 teams in the world to be selected to pitch for the final of enable makeathon 2.0"
    return ab

# @app.route('/user/<username>')
# def show_user_profile(username):
#     # show the user profile for that user
#     if username.lower()=="rahul":
#         profile = "Image processing Expert"
#     elif username.lower() == "ankit":
#         profile = "Machine Learning and Data Analytics Expert"
#     elif username.lower() == "sahaja":
#         profile = "NLP Expert and App Developer"
#     else:
#         profile = "We don't know anyone named %s"%(username)
#     stat = "<h1>%s</h1> <br> <h3>%s </h3> "%(username,profile)
#     return stat
@app.route('/')
def index():


    return render_template('home.html')

@app.route('/userlogin')
def userlogin():


    return render_template('add_user.html')

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
    app.run()
