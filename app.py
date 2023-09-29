from flask import Flask, render_template,jsonify,request
import dotenv
import datetime
import requests
import json 
dotenv.load_dotenv()
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import os

uri = 'mongodb+srv://'+os.environ.get("DB_USER")+':'+os.environ.get("DB_PASS")+"@cluster0.3v8vfkh.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)



app = Flask(__name__)

@app.route("/api/cep/<cep>",endpoint='cep')
def index():
    newcep = cep[0:6]
    res = requests.get('https://cdn.apicep.com/file/apicep/01153-000.json')
    response = json.loads(res.text)
    
    def verify(x):
        if x != "SP":
            print("esse cep não é de SP")  
        else: print('esse cep é de SP')
    
    verify(response['state'])

    return response


# @app.route("/")
# def index():
#     return render_template("index.html")

# @app.route("/api/users", methods = ['GET'])
# def get_users():
#    if(request.method == 'GET'):
#         data = {
#             "Modules" : 15,
#             "Subject" : "Data Structures and Algorithms",
#         }
#     db = client['match']
#     collection = db['users']
#     collection.insert_one({'name':"dayvison","server":"rodou o update com mongodb"})

@app.route("/api/age",endpoint='age')
def index():
    current_date = datetime.datetime.now()
    x = str(current_date)
#print(x[0:10])
    born = '27/09/2001'
    y= int(born[6:10])
    m = int(born[4:5])
    d= int(born[0:2])
#print(type(type (x[0:4])))
    year = int(x[0:4])- y
    month= int(x[5:7])- m
    day= int(x[8:10])-d
    data={"msg":'1'}
    if (year>18): data['msg']='é de maior'
    elif (year<17):  data['msg']='é de menor'
    elif (month>=0 and day>=0):  data['msg']='é de maior '
    else:  data['msg'] ='é de menor'

    return jsonify(data)



if __name__ == "__main__":
    app.run()
    
