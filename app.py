from flask import Flask, redirect, url_for, request
import json
from TaskPool import TaskPool

pool = TaskPool()

app = Flask(__name__)


@app.route('/getPurchasingTasks', methods=['GET'])
def getPurchasingTasks():
    return {
        'data': pool.getPurchasingTasks(),
        'code': 200
    }


@app.route('/getDeliveryTasks', methods=['GET'])
def getDeliveryTasks():
    return {
        'data': pool.getDeliveryTasks(),
        'code': 200
    }


@app.route('/getTask', methods=['GET'])
def getTask():
    id = request.args.get('id')
    return {
        'data': pool.getTask(id),
        'code': 200
    }


@app.route('/getPostedTask', methods=['GET'])
def getPostedTask():
    id = request.args.get('id')
    return {
        'data': pool.getPostedTask(id),
        'code': 200
    }


@app.route('/getAcceptedPurchasingTask', methods=['GET'])
def getAcceptedPurchasingTask():

    id = request.args.get('id')
    print('compare with:', id)
    return {
        'data': pool.getAcceptedPurchasingTask(id),
        'code': 200
    }


@app.route('/getAcceptedDeliveryTask', methods=['GET'])
def getAcceptedDeliveryTask():
    id = request.args.get('id')

    return {
        'data': pool.getAcceptedDeliveryTask(id),
        'code': 200
    }


@app.route('/createNewTask', methods=['GET', 'POST'])
def createNewTask():
    print('****************************POST****************************')
    print(request.form.get('data'))
    pool.addNewTask(request.form.get('data'))
    return {
        'code': 200
    }


@app.route('/getFriendsById', methods=['GET'])
def getFriendsById():
    id = request.args.get('id')

    return {
        'data': pool.getFriendsById(id),
        'code': 200
    }

@app.route('/getUserById', methods=['GET'])
def getUserById():
    id = request.args.get('id')
    return {
        'data': pool.getUserById(id),
        'code': 200
    } 


if __name__ == '__main__':
    app.run(debug=True)
