from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

#Referencing this file
app = Flask(__name__)

#Database location
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
#Initializing database
db = SQLAlchemy(app)

#DB Model class
class Todo(db.Model):
    #Primary Key
    id = db.Column(db.Integer, primary_key=True)
    #Content
    content = db.Column(db.String(200), nullable = False)
    #Date Created
    date_created = db.Column(db.DateTime, default = datetime.utcnow)

    #Function to return a string when new element is entered
    def __repr__(self):
        return "<Task %r>" % self.id

#App URL
@app.route('/')
#Website fucntion
def index():
    return render_template('index.html')

#Executing the app
if __name__ == "__main__":
    #Running the app
    app.run(debug=True)
