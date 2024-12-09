#
from flask import Flask
from flask import render_template, request, redirect
import textblob
import os
api = os.getenv("makersuite")

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST']) # front end to back end: post
def index():
    return(render_template('index.html'))

@app.route('/main', methods=['GET', 'POST']) # front end to back end: post
def main():
    name = request.form.get('q')
    return(render_template('main.html'))

@app.route('/SA', methods=['GET', 'POST']) # front end to back end: post
def SA():
    return(render_template('SA.html'))

@app.route('/SA_result', methods=['GET', 'POST']) # front end to back end: post
def SA_result():
    q = request.form.get("q")
    r = textblob.TextBlob(q).sentiment
    return(render_template('SA_result.html', r=r))

if __name__ == '__main__':
    app.run() # app.run(port=1234)