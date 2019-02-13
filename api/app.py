"""
Recive data from logstash
Insert error record to errorlog.db
Judge time and send text&email alarm to Chris
"""
#!flask/bin/python
from flask import Flask, jsonify
from flask import request
import time
import sqlite3
import boto3
import configparser
import os

curpath = os.path.dirname(os.path.realpath(__file__))
cfgpath = os.path.join(curpath, "configure.ini")
conf = configparser.ConfigParser()


app = Flask(__name__)
global tasks
tasks = []


@app.route('/tasks', methods=['GET'])
def get_tasks():
    print('get_tasks start')
    print('get_tasks end')
    return jsonify({'tasks': tasks})

@app.route('/tasks', methods=['POST'])
def create_task():
    if not request.json or not 'message' in request.json:
        abort(400)
    tasks = outputdb()
    task = {
        'id': int(tasks[-1]['id']) + 1,
        'message': request.json['message'],
        'host': request.json.get('host', ""),
        'tags': request.json.get('tags', ""),
        'path': request.json.get('path', ""),
        '@version': request.json.get('@version', ""),
        '@timestamp': request.json.get('@timestamp', ""),
	'pythontime': time.time()
    }

    sendtext(tasks,task)

    inputdb(task)
    return jsonify({'task': task}), 201


def sendtext(tasks,task):
    conf.read(cfgpath, encoding="utf-8")
    x = tasks[len(tasks)-1]['pythontime']
    y = task['pythontime']
    time = int(conf.getint("flask","duration_time"))
    print (time)
    if y - x < time:
        print( 'Not time now!!!')
    else:
        print( 'This is the time to input NEW TIME!!!')
        client = boto3.client('sns', region_name='ap-southeast-2',
                      aws_access_key_id="",
                    aws_secret_access_key="")

        response = client.publish(
            PhoneNumber="+61422566402",
            Message='WebOffice Urgency')

def inputdb(data):
    conn = sqlite3.connect('../data/errorlog.db')
    cursor = conn.cursor()
    cursor.execute('insert into errorlog (id, message, timestamp_, pythontime) values (%i, %a, %a, %a)' %(data['id'], data['message'], data['@timestamp'], data['pythontime']))
    cursor.close()
    conn.commit()
    conn.close()

def outputdb():
    connection = sqlite3.connect("../data/errorlog.db")
    connection.row_factory = dict_factory
    cursor = connection.cursor()
    cursor.execute("select * from errorlog order by id desc limit 0,1")
    results = cursor.fetchall()
    print(results)
    connection.close()
    return results

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d



if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0')
