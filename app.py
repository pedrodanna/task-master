from flask import Flask, render_template

#Referencing this file
app = Flask(__name__)

#App URL
@app.route('/')
#Website fucntion
def index():
    return render_template('index.html')

#Executing the app
if __name__ == "__main__":
    #Running the app
    app.run(debug=True)
