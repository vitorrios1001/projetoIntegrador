import httplib, urllib, base64, json
from flask import Flask, request
import requests
import socket
import os
import sys
import pickle

#from servidor import servidor

app = Flask(__name__)


@app.route("/processamento/", methods=['GET', 'POST'])
def processamento():
    
    if request.method == "POST":
            
        url = request.data
        print(url)
      
        r = requests.post('http://localhost:5000/node/', data = url)
        print "r"
        print(type(r))
        
        teste = [s.encode('utf-8') for s in r]            
        
        
        resp = str(teste)

        resp = list(resp)
        resp.pop(0)
        resp.pop(0)
        resp.pop(len(resp)-1)
        resp.pop(len(resp)-1)
        teste = ''.join(resp)
       #teste = r.json()
        print(teste)
        
        return str(teste)
        

def servidor(host,port):
    HOST = host     # Endereco IP do Servidor
    PORT = port     # Porta que o Servidor esta
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    orig = (HOST, PORT)
    tcp.bind(orig)
    tcp.listen(1)

    ativo = True
    while ativo:
        con, cliente = tcp.accept()
        pid = os.fork()
        if pid == 0:
            tcp.close()
            print 'Conectado por', cliente
            while ativo:
                msg = con.recv(1024)
                #if not msg: break
                print cliente, msg
                ativo = False
            print 'Finalizando conexao do cliente', cliente
            con.close()
            sys.exit(0)
        else:
            con.close()

    return msg        





if __name__ == "__main__":
    app.run(debug=True, port=3000)