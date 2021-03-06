import random
from time import sleep
from Queue import *
from threading import Thread, Lock
import httplib, urllib, base64, json
from flask import Flask, request
import requests
import socket
import os
import sys
import pickle
import backports 

class Node(object):
    
    def __init__(self, host, url):
        self.host = host
        self.url  = url

global processamento

global fila
global processado


app = Flask(__name__)


@app.route("/processamento/", methods=['GET', 'POST'])
def processamento():
    
        
    if request.method == "POST":
            
        global processado
        global processamento
        global fila 
        
        fila= Queue(Node)  
                
        url = request.data
        urlStr = str(url)
        print(urlStr)
   
        #r = requests.post('http://localhost:5000/node/', data = teste)
        
        host1 = 'http://172.10.10.100:5000/node/'
        host2 = 'http://172.10.10.102:5000/node/'
        

        listaDeHosts = [host1,host2]
             
        
        #Empilhando objetos node para processamento
        for host in listaDeHosts:
            print 'Colocando o host '+host+' na fila'
            node = Node(host,urlStr)
            fila.put(node)
        
        print(fila)

        processado = False
        
        #Startando Hosts para processamento    
        
        for node in listaDeHosts:
            
            teste = Thread(target=ProcessaImagem)
            teste.setDaemon(True)
            teste.start()
            print 'Eu startei a thread com host: '+node  

        
        
        i = 0
        while i < fila.qsize():              
            fila.join()
        
        
        print "Finalizou"
        
        processou = False
        
        while not processou:
            if processado == True:
                r = processamento
                processou = True    
        
        print(processamento)    
        return processamento
     
        

#funcao para consumir a fila
def ProcessaImagem():
    global processado
    global processamento
    job = fila.get() 
    sleep(random.randint(1,3)) 
    print 'Sou o host: '+job.host

    r = requests.post(job.host, data = job.url )
    
    if processado == False:
        processado = True
        resp = r.json()
        
        jstr = json.dumps(resp,ensure_ascii=True, indent=2)
        
        processamento = jstr
        fila.queue.clear
        
    print 'Pronto'
    fila.task_done() #finaliza o job



if __name__ == "__main__":
    app.run(debug=True, port=3000,host="172.10.10.102")


