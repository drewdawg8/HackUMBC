from flask import Flask, flash, redirect, render_template, request, session, abort, url_for
from werkzeug.utils import secure_filename
import os
from parse import parse_text


app = Flask(__name__)
UPLOAD_FOLDER = './'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
@app.route("/success/<name>", methods = ['POST','GET'])
def success(name):
    text = str(parse_text(name))
    os.remove(name)
    return render_template("success.html",value = text)

@app.route("/text/<filename>")
def text(filename):

    file = open('text.txt','r')
    lines = file.read()
    return str(lines)


@app.route("/", methods = ['POST','GET'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        #return render_template("success.html")
        return redirect(url_for('success',name = filename))
    return render_template("index.html")



if __name__ == "__main__":
	app.run()
