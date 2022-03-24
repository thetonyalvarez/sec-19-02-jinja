from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import *

app = Flask(__name__)
app.config['SECRET_KEY'] = "very-cool"

debug = DebugToolbarExtension(app)

@app.route('/')
def show_form():
	return render_template('form.html')

@app.route('/story')
def show_story():
	results = dict(request.args)
	newStory = story.generate(results)
	return newStory
