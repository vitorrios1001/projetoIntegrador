from flask import Flask, render_template, request, url_for, redirect

from flask.ext.sqlalchemy import SQLAlchemy

from sqlalchemy.orm import relationship

from datetime import date, datetime

app = Flask(__name__,template_folder='Templates')

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/projetoIntegrador'

db = SQLAlchemy(app)

class Imagem(db.Model):
    __tablename__='TBLIMG'

    _url = db.Column(db.String(255), primary_key=True)    
    processada = db.Column(db.Integer)
    result = db.Column(db.String(100000))
    
    def __init__(self,dataInclusao, processada, result):
        self.dataInclusao = dataInclusao
        self.processada = processada
        self.result = result


class Produto(db.Model):
    __tablename__='produto'

    _id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    desc = db.Column(db.String(50))
    qtdEstoque = db.Column(db.Integer)
    vlr = db.Column(db.Float)
    catProd = db.Column(db.Integer,db.ForeignKey('catproduto._id'),nullable=False)


    def __init__(self, desc, qtdEstoque, vlr, catProd):
        self.desc = desc
        self.qtdEstoque = qtdEstoque
        self.vlr = vlr
        self.catProd = catProd

db.create_all()

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/insert")
def insert():    
    c = Categoria.query.all()

    return render_template("insert.html", categorias=c)

    return render_template

@app.route("/newInsert", methods=['GET','POST'])
def newInsert():
    if request.method == 'POST':
        desc = (request.form.get("desc"))
        qtdEstoque = (request.form.get("qtdEstoque"))
        vlr = (request.form.get("vlr"))
        catProd = (request.form.get("catProd"))

        if desc and qtdEstoque and vlr and catProd:
            p = Produto(desc,qtdEstoque,vlr,catProd)
            db.session.add(p)
            db.session.commit()

    return redirect(url_for("list"))

@app.route("/list")
def list():
    produto = Produto.query.all()

    return render_template("list.html", produtos=produto)

@app.route('/delete/<int:id>')
def delete(id): 
                    
    p = Produto.query.filter_by(_id=id).first()
    db.session.delete(p)
    db.session.commit()   
           
    prod = Produto.query.all()
    return redirect(url_for("list")) 

    return render_template("list.html",produtos=prod)
    
@app.route("/update/<int:id>", methods=['GET', 'POST'])
def update(id):
    p = Produto.query.filter_by(_id=id).first()

    if request.method == "POST":
        desc = request.form.get("desc")
        qtdEstoque = request.form.get("qtdEstoque")
        vlr = request.form.get("vlr")

        if desc and qtdEstoque and vlr:
            p.desc = desc
            p.qtdEstoque = qtdEstoque
            p.vlr = vlr

            db.session.commit()

            return redirect(url_for("list"))

    return render_template("update.html", produto=p)

if __name__ == "__main__":
    app.run(debug=True)

