# FileStorageServer
simple file storage server with a command line interface in Python

this server should support the following functions :

1. Upload a file
ex. POST /files/<name>, Content-Type: multipart/form-data
2. Delete a file
ex. DELETE /files/<name>
3. List uploaded files (if a file is uploaded then deleted it should not be listed)
ex. GET /files may return a list of files: [file1.txt, file2.txt, ..]

  The Server should create automatically a 'files' repository from the folder it´s being launched.
(if not , probably it does not have the rights, so do it manually please).


1) **** Run the Server with the following command


python3 StorageServer.py


2) **** Run the client with the following 3 commands

[upload_file , delete_file , list_files]

a) python3 fs-store.py upload_file  <path_to_file + filename>
ex : python3 fs-store.py upload_file  c:/Users/HP/Documents/Downloads/foto.jpg

This option allow you to add any file with following formats ['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'doc', 'docs', 'xls', 'xlsx', 'xml']

b) python3 fs-store.py list_files

This option display all the elements uploaded. You can access directly with the browser running http://127.0.0.1:8081/files

c) python3 fs-store.py delete_file <filename>
ex: python3 fs-store.py delete_file foto.jpg

This option allows you to delete an element from the list. (Don´t forget to add the extension to the filename).


*Dependencies

flask 2.2.2
werkzeug 2.2.2
fire 0.4.0
requests 2.27.1

Tested with python 3.9.10  under Cygwin (Windows)

*Next Features
Sorting by name functionality
Search/Delete/Add function for web client 

*Distribution of this product in production :
- linux : With Cron after booting the machine
          create a executeServer.sh file calling the StorageServer.py and make that file executable(chmod +x)
          crontab -e  > @reboot executeServer.sh
- Windows : Copy and paste the shortcut to the app from the file location to the Startup folder.
	    The Server will start when Windows boots.

  
