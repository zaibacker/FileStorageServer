import requests
import fire

def upload_file(path):
    url = "http://localhost:8081/files"
    files = {'file': open(path, 'rb')}
    response = requests.post(url, files=files)
    return response.text
	
def delete_file(filename):
    url = "http://localhost:8081/files/" + filename
    response = requests.delete(url)
    return response.text

def list_files():
    url = "http://localhost:8081/files"
    response = requests.get(url)
    return response.text

#https://google.github.io/python-fire/guide/

if __name__ == '__main__':
    fire.Fire()