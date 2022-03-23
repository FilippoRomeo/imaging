from flask import Flask, render_template,request
import twitter_search as tsp
import json

app = Flask(__name__)     

@app.route('/')
def index():
    
    ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    link = ("https://freegeoip.app/json/{}")
    ipreq = tsp.get_data(link.format(ip))
    iptojson = json.loads(ipreq.content)
    sctojson = ipreq.sc   

    data = tsp.twsejs(iptojson["latitude"],iptojson["longitude"])

    return render_template('index.html',data=data, iptojson = iptojson, sctojson = sctojson)

if __name__ == "__main__": # if you use flask.run I think you dont need this

    app.run()
