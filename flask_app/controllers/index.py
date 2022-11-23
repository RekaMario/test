from flask_app import app
from flask import render_template ,session ,redirect ,request



@app.route('/')
def homePage():
    return render_template('index.html')