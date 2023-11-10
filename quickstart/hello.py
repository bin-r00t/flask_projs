from flask import Flask, request, url_for, redirect, render_template, abort
from markupsafe import escape
from werkzeug.utils import secure_filename

print(__name__)
app = Flask(__name__)



@app.route('/')
def home():
    return redirect(url_for('login'))


@app.route('/<name>')
def sayHello(name):
    # return "Hello, " + name  # payload: http://127.0.0.1:5000/%3Ca%20onclick=%22javascript:alert(1)%22%3Esdf
    return f"Hello, {escape(name)}!"

@app.get('/login')
def login():
    return render_template('login.html', name='test template')

@app.post('/login')
def doLogin():
    # abort(503)
    # abort(400)
    # abort(404)
    abort(403) 
    # abort(204) # not working... 

@app.get('/upload')
def upload():
    return render_template('upload.html')


@app.post('/upload')
def doUpload():
    f = request.files['userfile']
    filename = secure_filename(f.filename)
    print('filename', filename)
    f.save(f'./uploads/{filename}')
    return 'success uploaded:' + filename


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404