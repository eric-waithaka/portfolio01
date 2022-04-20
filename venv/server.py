from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def myHome():
    return render_template('index.html')

@app.route('/blog')
def blog():
    return 'These are my thoughts'