import httplib, urllib, base64, json
from flask import Flask, request
import requests
import socket
import os
import sys
import pickle

app = Flask(__name__)


@app.route("/processamento/", methods=['GET', 'POST'])
def processamento():
    
    if request.method == "POST":
            
        url = request.data
        teste = str(url)
        print(teste)
      
        r = requests.post('http://localhost:5000/node/', data = teste)
         
        resp = r.json()
        
        jstr = json.dumps(resp,ensure_ascii=True, indent=2)
              
        
        print(jstr)    
        return jstr
        

if __name__ == "__main__":
    app.run(debug=True, port=3000, host="192.168.43.57")