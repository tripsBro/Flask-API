from flask import Flask, url_for, request, render_template
from flask_sqlalchemy import SQLAlchemy
from sentry import convert
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_project1'] = 'postgresql://postgres:*******@localhost/trips'
db = SQLAlchemy(app)



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

@app.route('/')
def index():
    ref = url_for('con', text="are you who")
    s = "<h1>index page of Team Unicom Solutions</h1>" \
        "<br> <h3>We provide the following services:-<h3>" \
        "<ul> <li><a href = '%s' >Sentence corrector</a></li></ul>"%(ref)
    return render_template('home.html')

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         do_the_login()
#     else:
#         show_the_login_form()

# @app.route('/post/<int:post_id>')
# def show_post(post_id):
#     # show the post with the given id, the id is an integer
#     return 'Post %d' % post_id

@app.route('/convert/<string:text>')
def con(text):
    # show the post with the given id, the id is an integer
    ans = convert(text)
    ret = ans + "<br>" + "to correct any other sentence type after convert in the url"
    return ret

if __name__== "__main__":
    app.run()
