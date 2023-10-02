from flask import Flask, render_template,jsonify,request
import dotenv
import datetime
import requests
import json 
import asyncio
dotenv.load_dotenv()
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import os

uri = 'mongodb+srv://'+os.environ.get("DB_USER")+':'+os.environ.get("DB_PASS")+"@cluster0.3v8vfkh.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri, server_api=ServerApi('1'))

try:
    client.admin.command('ping')
except Exception as e:
    print(e)


app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route("/api/cep",endpoint='cep',methods=['POST']) 
async def index():
    print('verificou cep')
    data = request.json
    content_type = request.headers.get('body')
    json = request.json
    print("json é",json)
    data={"msg":"",'status':""}
    newcep = ''
    cep= json["cep"]
    if(cep[5]=='-'):
        newcep =cep
    else: 
        newcep = cep[0:5]+'-'+cep[5:11]
    link = 'https://cdn.apicep.com/file/apicep/'+newcep+'.json'
    res = requests.get(link)
    response = json.loads(res.text)
    state = response['state']
    if state !='SP': return jsonify({'msg':"O cep informado nao e de SP",'Status':"401"})  
    else:return jsonify({"status":"200"})
    await asyncio.sleep(1)
    return jsonify(data)
    
@app.route("/api/users", methods = ['POST'])
def get_users():
    username = request.form['name']
    cep = request.form['cep']
    adress = request.form['adress']
    adress = request.form['date']
    return 'username'
    db = client['match']
    collection = db['users']
    collection.insert_one({'name':username,'cep':cep,'adress':adress,"date":date})




@app.route("/api/age",endpoint='age',methods = ['POST'])
def index():
    print('verificou age')
    data = request.json
    content_type = request.headers.get('body')
    json = request.json
    print("json é",json)
    current_date = datetime.datetime.now()
    print('requsitou age')
    x = str(current_date)
    born = json["age"]
    y= int(born[6:10])
    m = int(born[4:5])
    d= int(born[0:2])
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
    
