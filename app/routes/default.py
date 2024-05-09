from app import app
from flask import render_template

# This is for rendering the home page
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/l')
def l():
    return render_template('l.html')