from flask import Flask, render_template,jsonify,request
import os 
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

os.environ.setdefault("DB_USER","Dayvison")
os.environ.setdefault("DB_PASS", "hRHJq0ovjYoxvUCT")

uri = 'mongodb+srv://'+os.environ.get("DB_USER")+':'+os.environ.get("DB_PASS")+"@cluster0.3v8vfkh.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

db = client['match']
collection = db['users']
collection.insert_one({'name':"dayvison","server":"rodou o update"})

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/users", methods = ['GET'])
def get_users():
   if(request.method == 'GET'):
        data = {
            "Modules" : 15,
            "Subject" : "Data Structures and Algorithms",
        }
  
        return jsonify(data)
if __name__ == "__main__":
    app.run()
    
