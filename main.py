from flask import Flask, render_template, redirect, url_for, flash, request, abort
from flask_bootstrap import Bootstrap

app =Flask(__name__)
Bootstrap(app)

@app.route('/')
def home():
    projects = []
    return render_template('index.html', projects= projects)

if __name__ =='__main__':
    app.run(debug=True)