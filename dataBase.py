import http.client, urllib.request, urllib.parse, urllib.error, base64, json
from flask import Flask, render_template, request, url_for, redirect,jsonify
import requests
#from flask.ext.sqlalchemy import SQLAlchemy

#from sqlalchemy.orm import relationship, session


app = Flask(__name__)

#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/projetoIntegrador'

#db = SQLAlchemy(app)

#class Imagem(db.Model):
 #   __tablename__='TBLIMG'
 #   _id = db.Column(db.Integer, primary_key=True, autoincrement=True)
 #   url = db.Column(db.Text(255))    
 #   processada = db.Column(db.Integer)
 #   result = db.Column(db.Text(100000))
    
 #   def __init__(self,url, processada, result):
  
  #      self.url = url
  #      self.processada = processada
  #      self.result = result

#db.create_all()

@app.route("/processamento/", methods=['GET', 'POST'])
def processamento():
    
    if request.method == "POST":
            
        u = request.data
        resp = str(u)            
                
        resp = list(resp)
        
        resp.pop(0)
        resp.pop(0)
        
        resp.pop(len(resp)-1)        
        url = ''.join(resp)
        #print(url)
        
        payload = {'b':"'"+url+"'"}
      
        r = requests.post('http://localhost:5000/node/',data = json.dumps(payload))
        result = json.dumps(r)
        return result
        




if __name__ == "__main__":
    app.run(debug=True, port=3000)