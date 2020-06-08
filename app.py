from flask import Flask

#Referencing this file
app = Flask(__name__)

#App URL
@app.route('/')
#Website fucntion
def index():
    return "Hello World !!!"

if __name__ == "__main__":
    app.run()
