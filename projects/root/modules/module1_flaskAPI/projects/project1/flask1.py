from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sentry import convert
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_project1'] = 'postgresql://postgres:tripsBr0@localhost/trips'
db = SQLAlchemy(app)

@app.route('/')

def index():
    return "index page of Team Unicom Solutions"

@app.route('/about')

def about():
    ab = "Team Unicom Solutions is one of the 9 teams in the world to be selected to pitch for the final of enable makeathon 2.0"
    return ab

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    if username.lower()=="rahul":
        profile = "Image processing Expert"
    elif username.lower() == "ankit":
        profile = "Machine Learning and Data Analytics Expert"
    elif username.lower() == "sahaja":
        profile = "NLP Expert and App Developer"
    else:
        profile = "We don't know anyone named %s"%(username)
    stat = "<h1>%s</h1> <br> <h3>%s </h3> "%(username,profile)
    return stat

# @app.route('/post/<int:post_id>')
# def show_post(post_id):
#     # show the post with the given id, the id is an integer
#     return 'Post %d' % post_id

@app.route('/convert/<string:text>')
def con(text):
    # show the post with the given id, the id is an integer
    ans = convert(text)
    return ans

if __name__== "__main__":
    app.run()
