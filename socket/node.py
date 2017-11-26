import httplib, urllib, base64, json
from flask import Flask,request
#from cliente import cliente
import requests
import socket

app = Flask(__name__)

subscription_key = '60d3407a418f4dae9d0133a11cb1719d'

uri_base = 'westcentralus.api.cognitive.microsoft.com'

headers = {    
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': subscription_key,
}

params = urllib.urlencode({    
    'visualFeatures': 'Categories,Description,Color',
    'language': 'en',
})

# The URL of a JPEG image to analyze.
#body = "{'url':'https://upload.wikimedia.org/wikipedia/commons/1/12/Broadway_and_Times_Square_by_night.jpg'}"

# Replace the three dots below with the URL of a JPEG image of a celebrity.
@app.route("/node/", methods=['GET', 'POST'])
def node():

    if request.method == "POST":
     
        u = request.data
                
        print("Recebi isso: ")          
        print(u)        
                
        body = "{'url':'"+u+"'}"
        print(body)
        try:
            # Execute the REST API call and get the response.
            conn = httplib.HTTPSConnection('westcentralus.api.cognitive.microsoft.com')
            conn.request("POST", "/vision/v1.0/analyze?%s" % params, body, headers)
            response = conn.getresponse()
            data = response.read()

            # 'data' contains the JSON data. The following formats the JSON data for display.
            parsed = json.loads(data)
            print ("Response:")
            print (json.dumps(parsed, sort_keys=True, indent=2))
            msg  = data
            conn.close()

        except Exception as e:
            print('Error:')
            print(e)
        return data
        
        #host = '127.0.0.1'
        #port = 8080
        #msg  = "teste"       
        
        #cliente(host,port,msg)


def cliente(host,port,msg):
    
    HOST = host     # Endereco IP do Servidor
    PORT = port            # Porta que o Servidor esta
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    dest = (HOST, PORT)
    tcp.connect(dest)
    print 'Para sair use CTRL+X\n'
    msg = msg

    ativo = True    
    while ativo:
        tcp.send (msg)
        ativo = False
    tcp.close()


        

if __name__ == "__main__":
    app.run(debug=True)