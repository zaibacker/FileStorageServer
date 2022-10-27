#!/usr/bin/env python3

from os import path, getcwd, mkdir, urandom, listdir, remove
from werkzeug.utils import secure_filename
from flask import Flask, flash, request, jsonify
from flask_cors import CORS

#basic extensions
EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'doc', 'docs', 'xls', 'xlsx', 'xml'}
WORKING_FOLDER = './files/'

#create files repository
FILES_DIR = getcwd() + '/files/'
try:
    mkdir(FILES_DIR)
except FileExistsError :
    print("Files Repertory exists")
		

application = Flask(__name__)
application.config['WORKING_FOLDER'] = WORKING_FOLDER
application.debug = False
CORS(application) 

#POST a file
@application.route('/files', methods=['POST'])
def upload_file():
    """Upload file to server and return message"""
    """Handles POST-requests by url /files"""
	
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file found')
            return 'no file found'
        file = request.files['file']
        if file.filename == '':
            flash('No file selected ')
            return 'No file selected '
        if file and extension_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(path.join(application.config['WORKING_FOLDER'], filename))
            return 'All good'

#Delete a file
@application.route('/files/<filename>', methods=['DELETE'])
def delete_file(filename):
    """Delete file if exists and return message"""
    """Handles Delete-requests by url /files/<filename>"""
	
    if path.exists("./files/" + filename):
        remove("./files/" + filename)
        return 'All good!'
    else:
        return 'file not found'


#Get the files list
@application.route('/files', methods=['GET'])
def list_files():
    """Delete file if exists and return response info in json format"""
    """Handles GET-requests by url /files"""
	
    directory = listdir(WORKING_FOLDER)
    filesInfos = []
    for fileName in directory:
        filesInfos.append(fileName)
    return jsonify(filesInfos)


def extension_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in EXTENSIONS	

if __name__ == "__main__":
    application.run(host='0.0.0.0', port=8081)