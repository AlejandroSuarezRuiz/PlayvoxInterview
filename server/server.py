from flask import Flask, jsonify
from flask_cors import CORS
from pymongo import MongoClient
from bson.json_util import dumps
import json
import datetime

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

client = MongoClient(host = "127.0.0.1", port = 27017)
db = client.Playvox

@app.route('/api/authors')
def get_authors():
    pipeline = [
        {"$group" : {
            "_id" : "$NOMBRE_ESCRITOR","copies": { "$sum": "$COPIAS_VENDIDAS" }
        }},
        { "$sort" : { "copies" : -1}},
        { "$limit": 5 }
    ]
    data = dumps(db.BOOKS.aggregate(pipeline))
    f= open("booksRes.txt","w")
    f.write(data+"\n")
    f.write(str(datetime.datetime.now().replace(second=0, microsecond=0))+"\n")
    f.close()
    return jsonify(data)

@app.route('/api/logs')
def get_logs():
    pipeline = [
        {"$group" : { "_id" : '$ID_USUARIO', "count" : {"$sum" : 1}}},
        {"$project": {
            "item": 1,
            "count":1,
            "inRange": {  
                "$cond": [ { "$and": [ { "$gt": [ "$count", 1000 ] }, { "$lt": [ "$count", 2000 ] } ] }, 1, 0]
            }
        }},
        {"$match" : { "inRange" : 1.0 }},
        {"$count": "myCount" }
    ]
    data = dumps(db.EVENTOS_LOG.aggregate(pipeline))
    f= open("logsRes.txt","w")
    f.write(data+"\n")
    f.write(str(datetime.datetime.now().replace(second=0, microsecond=0))+"\n")
    f.close()
    return jsonify(data)

@app.route('/api/consultelogs')
def consulte_logs():
    f= open("logsRes.txt","r")
    readData = open('logsRes.txt','r').read().split('\n')
    data = json.loads(readData[0])
    time = readData[1]
    data[0]["date"] = time
    return json.dumps(data[0])

@app.route('/api/salaries')
def get_salaries():
    pipeline = [
        {"$lookup": {
            "from": 'EMPLEADOS',
            "localField": 'EMPLEADO_ID',
            "foreignField": 'EMPLEADO_ID',
            "as": 'new_field'
        }},
        {"$unwind": '$new_field'},
        {"$project": {
            "SALARIO": 1,
            "AREA": '$new_field.AREA_NOMBRE'
        }},
        {"$group" : {
            "_id" : "$AREA",
            "averageQuantity": { "$avg": "$SALARIO" },
            "count": { "$sum": 1 }
        }},
        { "$sort" : { "_id" : 1} }
    ]
    data = dumps(db.SALARIOS.aggregate(pipeline))
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)