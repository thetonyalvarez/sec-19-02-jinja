from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import *

app = Flask(__name__)
app.config['SECRET_KEY'] = "very-cool"

debug = DebugToolbarExtension(app)

@app.route('/')
def show_home():
	return render_template('base.html')

@app.route('/form-1')
def show_form_1():
	return render_template('form-1.html')

@app.route('/story-1')
def show_story_1():
	results = dict(request.args)
	newStory = story_1.generate(results)
	return render_template('story-1.html', story=newStory)




@app.route('/form-2')
def show_form_2():
	return render_template('form-2.html')

@app.route('/story-2')
def show_story_2():
	results = dict(request.args)
	newStory = story_2.generate(results)
	return render_template('story-2.html', story=newStory)



@app.route('/form-3')
def show_form_3():
	return render_template('form-3.html')

@app.route('/story-3')
def show_story_3():
	results = dict(request.args)
	newStory = story_3.generate(results)
	return render_template('story-3.html', story=newStory)




@app.route('/form-4')
def show_form_4():
	return render_template('form-4.html')

@app.route('/story-4')
def show_story_4():
	results = dict(request.args)
	newStory = story_4.generate(results)
	return render_template('story-4.html', story=newStory)




@app.route('/form-5')
def show_form_5():
	return render_template('form-5.html')

@app.route('/story-5')
def show_story_5():
	results = dict(request.args)
	newStory = story_5.generate(results)
	return render_template('story-5.html', story=newStory)
