from flask import Flask
from test2 import template
app = Flask(__name__)

@app.route("/")
def hello():
    return str(template(0,100,100,100,50,100))

if __name__ == "__main__":
    app.run()
