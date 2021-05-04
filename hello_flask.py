from flask import Flask 
from markupsafe import escape
app = Flask(__name__)

@app.route('/hello')
def hello_world():
    return 'Hello, World!'

@app.route('/')
def index():
    return 'Index Page'

# VARIABLE RULES
"""
You can add variable sections to a URL by 
marking sections with <variable_name>. 
Your function then receives the <variable_name> 
as a keyword argument. Optionally, you can use a 
converter to specify the type of the argument like 
<converter:variable_name>.
"""

@app.route('/user/<username>')
def show_user(username):
    #show the user profile for that user
    return 'User %s' % escape(username)

@app.route('/post/<int:post_id>')
def show_post(post_id):
    #show the post with the given id, id is an integer
    return 'Post %d' % post_id

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    #show the subpath after /path/
    return 'Subpath %s' % escape(subpath)
