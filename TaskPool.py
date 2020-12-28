import Task
import json
import datetime
from rmp.initial_data import user, tasks



class TaskPool:
    def __init__(self):
        self.tasks = []
        self.messageLists = None
        self.reset()

    def reset(self):
        self.tasks = tasks

        self.messageLists = {
            "hjh": [
                {
                    "type": "message",
                    "value": '王博真帅',
                    "selfSend": False,
                },
                {
                    "type": "message",
                    "value": '王博真帅',
                    "selfSend": True,
                },
                {
                    "type": "link",
                    "value": '',
                    "selfSend": False,
                    "taskId": 11,
                    "imageFiles": [
                        "https://pic13.997788.com/_pic_auction/00/08/01/22/8012210c.jpg",
                        "https://tse2-mm.cn.bing.net/th/id/OIP.J2MgFnLale171Ppo-l0ZUwAAAA?pid=Api&w=460&h=460&rs=1"
                    ]
                },
                {
                    "type": "link",
                    "value": '',
                    "selfSend": True,
                    "taskId": 12,
                    "imageFiles": [
                        "https://pic13.997788.com/_pic_auction/00/08/01/22/8012210c.jpg",
                        "https://tse2-mm.cn.bing.net/th/id/OIP.J2MgFnLale171Ppo-l0ZUwAAAA?pid=Api&w=460&h=460&rs=1"
                    ]
                }
            ],
            "lxr": [
                {
                    "type": "message",
                    "value": '王博真帅',
                    "selfSend": False,
                },
                {
                    "type": "message",
                    "value": '王博真帅',
                    "selfSend": True,
                }
            ],
            "lh": [
                {
                    "type": "message",
                    "value": '王博真帅',
                    "selfSend": False,
                },
                {
                    "type": "message",
                    "value": '王博真帅',
                    "selfSend": True,
                }
            ],
            "wyx": [
                {
                    "type": "message",
                    "value": '王博真帅',
                    "selfSend": False,
                },
                {
                    "type": "message",
                    "value": '王博真帅',
                    "selfSend": True,
                }
            ],
            "csd": [
                {
                    "type": "message",
                    "value": '王博真帅',
                    "selfSend": False,
                },
                {
                    "type": "message",
                    "value": '王博真帅',
                    "selfSend": True,
                }
            ]
        }
        return True

    def convertToDict(self, task):
        return {
            "id": task.id,
            "special_user": task.special_user,
            "p_title": task.p_title,
            "good": task.good,
            "good_pictures": task.good_pictures,
            "p_destination": task.p_destination,  # 带坐标
            "d_destination": task.d_destination,  # 带坐标
            "money": task.money,
            "deadline": task.deadline,
            "details": task.details,
            "status": task.status,
            "phone": task.phone,
            "author": task.author,
            "time": task.time,

            # status == 1:
            "puchaser": task.puchaser,

            # status == 2:
            "p_location": task.p_location,
            "p_finish_time": task.p_finish_time,
            "p_send_location": task.p_send_location,
            "p_details": task.p_details,
            "p_money": task.p_money,

            # status == 3:
            "deliver": task.deliver,
            "d_current_location": task.d_current_location,
            "d_finish_time": task.d_finish_time,
            "d_money": task.d_money,

            # status == 4:
            "appraise": task.appraise,
            "p_appraise": task.p_appraise,
            "d_appraise": task.d_appraise
        }

    def getTasks(self):
        res = []
        for task in self.tasks:
            res.append(self.convertToDict(task))
        return res

    def getPurchasingTasks(self):
        res = []
        for task in self.tasks:
            if task.status == 0:
                if task.special_user == None:
                    res.append(self.convertToDict(task))
        return res

    def getDeliveryTasks(self):
        res = []
        for task in self.tasks:
            if task.status == 2:
                res.append(self.convertToDict(task))
        return res

    def getTask(self, id):
        for task in self.tasks:
            if str(task.id) == id:
                return self.convertToDict(task)

    def getPostedTask(self, id):
        res = []
        for task in self.tasks:
            if str(task.author['id']) == id:
                res.append(self.convertToDict(task))
        return res

    def getAcceptedPurchasingTask(self, id):
        res = []
        for task in self.tasks:
            if task.puchaser and str(task.puchaser['id']) == id:
                res.append(self.convertToDict(task))
        return res

    def getAcceptedDeliveryTask(self, id):
        res = []
        for task in self.tasks:
            if task.deliver and str(task.deliver['id']) == id:
                res.append(self.convertToDict(task))
        return res

    def getFriendsById(self, id):
        res = []
        for friend in user[id]['friends']:
            res.append(user[friend])
        return res

    def getUserById(self, id):
        return user[id]

    def addNewTask(self, taskJson):
        task = json.loads(taskJson)
        imgFiles = []

        for img in task['imgFiles']:
            imgFiles.append(img['url'])

        self.tasks.append(Task.Task(
            len(self.tasks) + 1,
            task['title'],
            task['itemName'],
            imgFiles,
            task['purchasePlace'],
            task['address'],
            task['money'],  # need to change
            task['deadLine'],
            task['description'],
            0,
            task['phone'],
            user['root'],
            datetime.datetime.strftime(
                datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')  # need to change
        ))

        print(task)
        return task

    def receivePurchasingTask(self, task_id, user_id):
        for data in self.tasks:
            if str(data.id) == str(task_id):
                data.status = 1
                data.puchaser = user[user_id]
                return True
        return False

    def receiveDeliveryTask(self, task_id, user_id):
        for data in self.tasks:
            if str(data.id) == str(task_id):
                data.status = 3
                data.deliver = user[user_id]
                data.d_current_location = data.p_send_location
                return True
        return False

    def finishPayment(self, id):
        for data in self.tasks:
            if str(data.id) == str(id):
                data.status = 5
                return True
        return False

    def finishStar(self, id, p_star, d_star):
        for data in self.tasks:
            if str(data.id) == str(id):
                data.status = 6
                data.p_appraise = float(p_star)
                data.d_appraise = float(d_star)
                data.appraise = (float(p_star) + float(d_star)) / 2
                return True
        return False

    def finishPurchasingTask(self, taskJson):
        task = json.loads(taskJson)

        for data in self.tasks:
            if str(data.id) == str(task['id']):
                data.status = 2
                data.p_location = task['purchasePlace']
                data.p_finish_time = datetime.datetime.strftime(
                    datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')
                data.p_send_location = task['address']
                data.p_details = task['description']
                data.p_money = task['money']
        return task

    def finishDeliveryTask(self, id, money):
        for data in self.tasks:
            if str(data.id) == str(id):
                data.status = 4
                data.d_finish_time = datetime.datetime.strftime(
                    datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')
                data.d_money = money
                return True
        return False

    def addSpecialTask(self, taskJson):
        task = json.loads(taskJson)
        imgFiles = []

        for img in task['imgFiles']:
            imgFiles.append(img['url'])

        self.tasks.append(Task.Task(
            len(self.tasks) + 1,
            task['title'],
            task['itemName'],
            imgFiles,
            task['purchasePlace'],
            task['address'],
            task['money'],  # need to change
            task['deadLine'],
            task['description'],
            0,
            task['phone'],
            user['root'],
            datetime.datetime.strftime(
                datetime.datetime.now(), '%Y-%m-%d %H:%M:%S'),  # need to change
            special_user=task['special_user']
        ))
        self.messageLists[task['special_user']['id']].append({
            "type": "link",
                    "value": '',
                    "selfSend": False,
                    "taskId": len(self.tasks),
                    "imageFiles": imgFiles
        })

        print(self.messageLists[task['special_user']['id']])
        return task

    def getChatListById(self, id):
        return self.messageLists[id]

    def addChatMessage(self, idx, message):
        print(idx)
        self.messageLists[idx].append({
            "type": "message",
            "value": message,
            "selfSend": False,
        })
        return True
