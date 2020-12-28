from flask import Flask, redirect, url_for, request
import json
from TaskPool import TaskPool

pool = TaskPool()

app = Flask(__name__)

@app.route('/reload', methods=['GET'])
def reload():
    if pool.reset():
        return {
            'data': '数据重置成功',
            'code': 200
        }

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


@app.route('/receivePurchasingTask', methods=['GET'])
def receivePurchasingTask():
    id = request.args.get('id')
    user = request.args.get('user')
    if pool.receivePurchasingTask(id, user):
        return {
            'data': '任务接受成功',
            'code': 200
        }
    else:
        return {
            'data': '任务接受失败',
            'code': 500
        }

@app.route('/receiveDeliveryTask', methods=['GET'])
def receiveDeliveryTask():
    id = request.args.get('id')
    user = request.args.get('user')
    if pool.receiveDeliveryTask(id, user):
        return {
            'data': '任务接受成功',
            'code': 200
        }
    else:
        return {
            'data': '任务接受失败',
            'code': 500
        }

@app.route('/finishPayment', methods=['GET'])
def finishPayment():
    id = request.args.get('id')
    if pool.finishPayment(id):
        return {
            'data': '支付成功',
            'code': 200
        }
    else:
        return {
            'data': '支付失败',
            'code': 500
        }

@app.route('/finishStar', methods=['GET'])
def finishStar():
    id = request.args.get('id')
    p_appraise = request.args.get('pstar')
    d_appraise = request.args.get('dstar')

    if pool.finishStar(id, p_appraise, d_appraise):
        return {
            'data': '支付成功',
            'code': 200
        }
    else:
        return {
            'data': '支付失败',
            'code': 500
        }

@app.route('/finishPurchasingTask', methods=['GET', 'POST'])
def finishPurchasingTask():
    pool.finishPurchasingTask(request.form.get('data'))
    return {
        'code': 200
    }

@app.route('/finishDeliveryTask', methods=['GET'])
def finishDeliveryTask():
    id = request.args.get('id')
    money = request.args.get('money')

    if pool.finishDeliveryTask(id, money):
        return {
            'data': '支付成功',
            'code': 200
        }
    else:
        return {
            'data': '支付失败',
            'code': 500
        }

@app.route('/createNewSpecialTask', methods=['GET', 'POST'])
def createNewSpecialTask():
    print('****************************POST****************************')
    print(request.form.get('data'))
    pool.addSpecialTask(request.form.get('data'))
    return {
        'code': 200
    }

@app.route('/getChatListById', methods=['GET'])
def getChatListById():
    id = request.args.get('id')

    return {
        'data': pool.getChatListById(id),
        'code': 200
    }

@app.route('/addChatMessage', methods=['GET', 'POST'])
def addChatMessage():
    idx = request.form.get('id')
    message = request.form.get('message')
    pool.addChatMessage(idx, message)
    return {
        'code': 200
    }


if __name__ == '__main__':
    # app.run(host='10.162.179.113', debug=True)
    app.run(host='127.0.0.1', debug=True)