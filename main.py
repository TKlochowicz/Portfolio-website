from flask import Flask, render_template, redirect, url_for, flash, request, abort
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

app =Flask(__name__)
Bootstrap(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///projects.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Project(db.Model):
    __tablename__ = "projects"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    git_url = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=False)


def addProject():
    name = input("Name:")
    git_url = input("Git URL:")
    description = input("Description:")
    new_project = Project(name=name,git_url=git_url, description=description)
    db.session.add(new_project)
    db.session.commit()

@app.route('/')
def home():
    projects = Project.query.all()
    return render_template('index.html', projects= projects)

if __name__ =='__main__':
    app.run()