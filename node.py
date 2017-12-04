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


# Replace the three dots below with the URL of a JPEG image of a celebrity.
@app.route("/node/", methods=['GET', 'POST'])
def node():

    if request.method == "POST":
     
        u = request.data
                
        print("Recebi isso: ")          
        print(u) 

        #teste = [s.encode('utf-8') for s in u] 
        
        teste = str(u)
        resp = list(teste)
        resp.pop(0)
        resp.pop(len(resp)-1)       
        teste = ''.join(resp)        
        #teste = str(teste)

        body = "{'url':'"+teste+"'}"
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
            msg  = (json.dumps(parsed, sort_keys=True, indent=2))
            conn.close()

        except Exception as e:
            print('Error:')
            print(e)
        print(msg)
        return msg
        
       

if __name__ == "__main__":
    app.run(debug=True,host='172.10.10.102')