from flask import render_template
from . import main

@main.route('/')
def index():
  '''
  view root page function that returns the index page and its function
  '''
  return render_template('index.html')