#!/usr/bin/python
from flask import Flask, jsonify, make_response

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


@app.route('/todo/api/v1.0/tasks/<int:task_id>',methods=['GET'])
def get_task(task_id):
    task1 = filter(lambda t: t['id']== task_id, tasks)
    if len(task1)==0:
        abort(404)
    return jsonify({'task1':task1[0]})

@app.errorhandler(500)
def not_found(error):
    return make_response(jsonify({'error':'Not found'}), 404)

if __name__=="__main__":
    app.run()



