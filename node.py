import http.client, urllib.request, urllib.parse, urllib.error, base64, json
from flask import Flask, request


app = Flask(__name__)

#Chave de segurança para a api
subscription_key = '60d3407a418f4dae9d0133a11cb1719d'

uri_base = 'westcentralus.api.cognitive.microsoft.com'

headers = {
    # Request headers.
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': subscription_key,
}

params = urllib.parse.urlencode({
    # Request parameters. All of them are optional.
    'visualFeatures': 'Categories,Description,Color',
    'language': 'en',
})



# Replace the three dots below with the URL of a JPEG image of a celebrity.
@app.route("/node/", methods=['GET', 'POST'])
def node():

    if request.method == "POST":
        
        u = request.data
        resp = str(u) 
            

        print("Recebi isso: ")          
        print(u)        
        resp = list(resp)
        resp.pop(0)
        resp.pop(0)
        resp.pop(0)
        resp.pop(0)
        resp.pop(0)
        resp.pop(0)
        resp.pop(0)
        resp.pop(0)
        resp.pop(0)
        resp.pop(0)
        resp.pop(0)
        resp.pop(len(resp)-1)
        resp.pop(len(resp)-1)
        resp.pop(len(resp)-1)
        resp.pop(len(resp)-1)
        resp.pop(len(resp)-1)
        url = ''.join(resp)
        print("Converti nisso: ")
        print(url)
        body = "{'url':'"+url+"'}"
        print("Esse é o body: ")
        print(body)
        try:
            # Execute the REST API call and get the response.
            conn = http.client.HTTPSConnection('westcentralus.api.cognitive.microsoft.com')
            conn.request("POST", "/vision/v1.0/analyze?%s" % params, body, headers)
            response = conn.getresponse()
            data = response.read()

            # 'data' contains the JSON data. The following formats the JSON data for display.
            parsed = json.loads(data)
            #print("Response:")
            #print(json.dumps(parsed, sort_keys=True, indent=2))            
            #return (json.dumps(parsed, sort_keys=True, indent=2))
            
            conn.close()

        except Exception as e:
            print('Error:')
            print(e)

        x = data
        x = str(x)  
        print("Tipo: ")
        print(x) 
        
        
        return x


if __name__ == "__main__":
    app.run(debug=True)