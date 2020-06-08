from flask import Flask, render_template, url_for, request, redirect
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

    #Function to return a string when new element is added
    def __repr__(self):
        return "<Task %r>" % self.id

#App URL
@app.route('/', methods=['POST', 'GET'])
#Website fucntion
def index():
    #Post request action
    if request.method == 'POST':
        #Variable to store form data
        task_content = request.form['content']
        #Creating database object
        new_task = Todo(content=task_content)

        #Push to database
        try:
            #Add item to db
            db.session.add(new_task)
            #Commit change
            db.session.commit()
            #Return to application
            return redirect('/')
        except:
            #Report error
            return 'Unable to add item to DB'

    else:
        #Variable with database data
        tasks = Todo.query.order_by(Todo.date_created).all()
        #Run page with giving varibles
        return render_template('index.html', tasks=tasks)

#App URL to delete item
@app.route('/delete/<int:id>')
#Function to delete item
def delete(id):
    #Variable to store the id of the item to be deleted
    task_to_delete = Todo.query.get_or_404(id)

    try:
        #Delete item in db
        db.session.delete(task_to_delete)
        #Commit change
        db.session.commit()
        #Return to application
        return redirect('/')

    except:
        #Report error
        return 'Unable to delete task'

#App URL to update item
@app.route('/update/<int:id>', methods=['POST', 'GET'])
#Function to update item
def update(id):
    #Variable to store task 
    task = Todo.query.get_or_404(id)
    #Post request action
    if request.method == 'POST':
        #Variable to store form data
        task.content = request.form['content']

        try:
            #Commit changes
            db.session.commit()
            #Return to application
            return redirect('/')
        except:
            return 'Unable to update task'

    else:
        #Run page with giving varibles
        return render_template('update.html', task=task)

#Executing the app
if __name__ == "__main__":
    #Running the app
    app.run(debug=True)
