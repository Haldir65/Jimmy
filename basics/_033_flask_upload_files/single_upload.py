import os
from flask import Flask, request, redirect, url_for,render_template,send_file
from werkzeug import secure_filename
import logging

UPLOAD_FOLDER =  os.getcwd()+"/static"
if not os.path.exists(UPLOAD_FOLDER):
    os.mkdir(UPLOAD_FOLDER)

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files.get('file',None)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('index'))
    return render_template('upload.html',files=["/static/"+x for x in os.listdir(app.config['UPLOAD_FOLDER'],)])

@app.route('/static/<filename>', methods=['GET'])
def get_image(filename):
    fullpath = os.path.join(UPLOAD_FOLDER, filename)
    return send_file(fullpath, mimetype='image/jpeg')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)