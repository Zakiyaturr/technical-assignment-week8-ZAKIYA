import pymongo #mengimport library pymongo      
import datetime
from flask import Flask, request 

app = Flask(_name_)


client = pymongo.MongoClient("mongodb+srv://zakiya:zakiya@cluster0.nthf1fl.mongodb.net/?retryWrites=true&w=majority")
db = client['week8']
my_collections = db ['zakiya']
timestamp = datetime.datetime.now()

@app.route('/diraya',methods=['GET','POST'])
def diraya():
    kecepatan = request.args.get('kecepatan')
    latitude = request.args.get('latitude')
    longitude = request.args.get('longitude')
    
    if request.method == 'POST':
    
       results = my_collections.insert_one({"kecepatan":kecepatan,"latitude":latitude,"longitude":longitude, "timestamp":timestamp})
       print(results)
       return {
            "kecepatan":kecepatan,
            "latitude":latitude,
            "longitude":longitude,
            "timestamp":timestamp
                }

if _name_ == '_main_':
    app.run(host ='0.0.0.0', port = 8001, debug = True)
