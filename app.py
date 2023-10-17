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
    content_type = request.headers.get('body')
    jsonData = request.json
    if jsonData:
        data={"msg":""}
        newcep = ''
        cep= jsonData
        if(cep[5]=='-'):
            newcep =cep
        else: 
            newcep = cep[0:5]+'-'+cep[5:11]
        link = 'https://viacep.com.br/ws/'+newcep+'/json/'
        res = requests.get(link)
        response = json.loads(res.text)
        state = response["uf"]

        if(res.status_code !=200): return jsonify({'msg':"O cep informado nao valido",'status':400})
        elif (state !='SP'): return jsonify({'msg':"O cep informado nao e de SP",'Status':400})  
        else:return jsonify({"status":200,'msg':"cep validado"})
        await asyncio.sleep(1)
        return jsonify(data)
    else: return jsonify({"status":400,'msg':"cep nao enviado"})
@app.route("/api/users", methods = ['POST'])
def get_users():

    # username = request.form['name']
    # cep = request.form['cep']
    # adress = request.form['adress']
    # date = request.form['date']
    db = client['match']
    collection = db['users']
    vagas  = collection.find_one({"name":"vagas"})
  
    
    total = { "$set": { 'total': vagas["total"]+1 } }
    collection.update_one({"name":"vagas"},total,upsert=True)
    return render_template('finalizado.html')
    
    #collection.insert_one({'name':username,'cep':cep,'adress':adress,"date":date})
@app.route("/api/age",endpoint='age',methods = ['POST'])
def index():
    content_type = request.headers.get('body')
    jsonData = request.json
    if(jsonData):
        current_date = datetime.datetime.now()
        x = str(current_date)
        born = jsonData
        y= int(born[0:4])
        m = int(born[5:7])
        d= int(born[8:10])
        year = int(x[0:4])- y
        month= int(x[5:7])- m
        day= int(x[8:10])-d
        data={"msg":''}
        if (year>18): data={"msg":"é de maior",'status':200}
        elif (year<17): data={"msg":"Só Maiores de Idade Permitidos",'status':400}
        elif (month>=0 and day>=0):  data={"msg":"é de maior",'status':200}
        else:  data={"msg":"é de menor",'status':400}
        return jsonify(data)
    else: return jsonify({"status":400,"msg":"data nao preenchida"})
       
  
@app.route("/api/vagas",endpoint='vagas')
def get_users():

    db = client['match']
    collection = db['users']
    vagas  = collection.find_one({"name":"vagas"})
 
    return jsonify(vagas["total"])
    



if __name__ == "__main__":
    app.run()
    
