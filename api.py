#!/usr/bin/python
from flask import Flask, jsonify

app=Flask(__name__)

tasks =[
    {
        'id':1,
        'title':u'Buy groceries',
        'description':'Milk,cheese,pizza,fruit',
        'done':False
    },
    {
        'id':2,
        'title':u'Learn ganesh',
        'description':'Need to find a good Python ',
        'done':False
    }
]

@app.route("/todo/api/v1.0/tasks",methods=['GET'])
def get_tasks():
    return jsonify({'tasks':tasks})

if __name__=="__main__":
    app.run()
