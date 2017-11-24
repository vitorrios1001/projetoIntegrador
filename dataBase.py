from flask import Flask, render_template, request, url_for, redirect

from flask.ext.sqlalchemy import SQLAlchemy

from sqlalchemy.orm import relationship

from datetime import date, datetime

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/projetoIntegrador'

db = SQLAlchemy(app)

class Imagem(db.Model):
    __tablename__='TBLIMG'
    _id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    url = db.Column(db.Text(255))    
    processada = db.Column(db.Integer)
    result = db.Column(db.Text(100000))
    
    def __init__(self,url, processada, result):
        self.url = url
        self.processada = processada
        self.result = result

db.create_all()


def procImagem(url):
    img = Imagem.query.filter_by(url=url).first()
    print(img.processada)
    while img.processada == 0:
        img = Imagem.query.filter_by(url=url).first()
        
    if img.processada == 1:
        print(img.result)
        return True
    


@app.route("/processamento/<string:url>", methods=['GET', 'POST'])
def processamento(url):
    
    if request.method == "GET":
        myUrl = url
        processada = 0
        result = ""
        if myUrl:
            img = Imagem(myUrl,processada,result)
            db.session.add(img)
            db.session.commit()

    
    if procImagem(myUrl):
        img = Imagem.query.filter_by(url=myUrl).first
                    
    print(img.result)
    return img.result              









if __name__ == "__main__":
    app.run(debug=True)