from flask import Flask, flash, redirect, render_template, request, session, abort, url_for
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
UPLOAD_FOLDER = './'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
@app.route("/success", methods = ['POST','GET'])
def success():
    if request.method == 'POST':
        action = request.form['name']
        print(action)
        if action == 'yes':
            return redirect('/')



@app.route("/", methods = ['POST','GET'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return render_template("success.html")
    return render_template("index.html")

@app.route("/hello/<string:name>/")
def hello(name):
    return render_template(
        'index.html',name=name)

if __name__ == "__main__":
    app.run()
