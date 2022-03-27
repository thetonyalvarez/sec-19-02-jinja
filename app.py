from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import *
from wtforms import Form, StringField, validators


app = Flask(__name__)
app.config['SECRET_KEY'] = "very-cool"

debug = DebugToolbarExtension(app)
class MadlibsForm(Form):
    place = StringField('Place', [
		validators.Length(min=3, max=35),
		validators.DataRequired()
		])
    noun = StringField('Noun', [
		validators.Length(min=3, max=35),
		validators.DataRequired()
		])
    verb = StringField('Verb', [
		validators.Length(min=3, max=35),
		validators.DataRequired()
		])
    adjective = StringField('Adjective', [
		validators.Length(min=3, max=35),
		validators.DataRequired()
		])
    plural_noun = StringField('Plural Noun', [
		validators.Length(min=3, max=35),
		validators.DataRequired()
		])


@app.route('/')
def show_home():
	return render_template('base.html')

@app.route('/form-1')
def show_form_1():
	form = MadlibsForm(request.form)
	return render_template('form-1.html', form=form, title="Once Upon A Time")

@app.route('/story-1')
def show_story_1():
	results = dict(request.args)
	newStory = story_1.generate(results)
	return render_template('story-1.html', story=newStory, title="Once Upon A Time")

@app.route('/form-2')
def show_form_2():
	form = MadlibsForm(request.form)
	return render_template('form-2.html', form=form, title="Going on Vacation")

@app.route('/story-2')
def show_story_2():
	results = dict(request.args)
	newStory = story_2.generate(results)
	return render_template('story-2.html', story=newStory, title="Going on Vacation")

@app.route('/form-3')
def show_form_3():
	form = MadlibsForm(request.form)
	return render_template('form-3.html', form=form, title="The Zoo")

@app.route('/story-3')
def show_story_3():
	results = dict(request.args)
	newStory = story_3.generate(results)
	return render_template('story-3.html', story=newStory, title="The Zoo")

@app.route('/form-4')
def show_form_4():
	form = MadlibsForm(request.form)
	return render_template('form-4.html', form=form, title="The Amusement Park")

@app.route('/story-4')
def show_story_4():
	results = dict(request.args)
	newStory = story_4.generate(results)
	return render_template('story-4.html', story=newStory, title="The Amusement Park")

@app.route('/form-5')
def show_form_5():
	form = MadlibsForm(request.form)
	return render_template('form-5.html', form=form, title="About The X-Men")

@app.route('/story-5')
def show_story_5():
	results = dict(request.args)
	newStory = story_5.generate(results)
	return render_template('story-5.html', story=newStory, title="About The X-Men")

