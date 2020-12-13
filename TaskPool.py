import Task
import json

user = {
    "root": {
        "id": "root",
        "name": "WCY",
        "signature": "胡博头号粉丝",
        "avatar": "https://www.gx8899.com/uploads/allimg/2016062815/yddciyonaq3.jpg"
    },
    "hjh": {
        "id": "hjh",
        "name": "HJH",
        "signature": "胡博本人",
        "avatar": "https://tse2-mm.cn.bing.net/th/id/OIP.vRY1U0-rSP2pXM-5qIQIuAAAAA?pid=Api&rs=1"
    },
    "lxr": {
        "id": "lxr",
        "name": "LXR",
        "signature": "胡博二号粉丝",
        "avatar": "https://www.keaidian.com/uploads/allimg/180927/co1P92F95035-0-9.jpg"
    },
    "lh": {
        "id": "lh",
        "name": "HUGE",
        "signature": "虎子哥",
        "avatar": "https://tse1-mm.cn.bing.net/th/id/OIP.mbbH-lakXg_XIZmfX0xG_AAAAA?pid=Api&rs=1"
    }
}


data = [
    Task.Task(
        1,
        "求购复旦大学纪念章",
        "复旦大学纪念章",
        [
            "https://pic13.997788.com/_pic_auction/00/08/01/22/8012210c.jpg",
            "https://tse2-mm.cn.bing.net/th/id/OIP.J2MgFnLale171Ppo-l0ZUwAAAA?pid=Api&w=460&h=460&rs=1"
        ],
        {
          'name': "复旦大学",
          'longitude': 121.50904,
          'latitude': 31.33541
        },
        {
          'name': "交通大学闵行校区",
          'longitude': 121.43102,
          'latitude': 31.0176
        },
        "1000",
        "2020-12-25 11:32:45",
        "求复旦纪念章。",
        0,
        "15619202209",
        user['root'],
        "2020-12-10 08:15:44"
    ),
    Task.Task(
        2,
        "2999求购原价RTX3060Ti",
        "NVIDIA RTX 3060Ti",
        [
            "https://3c.3dmgame.com/uploadfile/2020/1202/20201202115919476.jpg",
            "https://tse1-mm.cn.bing.net/th/id/OIP.PIlOjgDn1rEkZJznZ5thjQHaJd?pid=Api&rs=1",
            "https://tse4-mm.cn.bing.net/th/id/OIP.O4_--i7Wb6Gq9R6U3Ii5pAHaEK?pid=Api&rs=1"
        ],
        {
          'name': "交通大学闵行校区",
          'longitude': 121.43102,
          'latitude': 31.0176
        },
        {
          'name': "交通大学闵行校区",
          'longitude': 121.43102,
          'latitude': 31.0176
        },
        "1000",
        "2020-12-13 11:32:45",
        "2999收3060ti。",
        1,
        "15619202209",
        user['root'],
        "2020-12-14 15:30:31",
        puchaser=user['lxr'],
        p_location='x36',
        p_details='易摔坏',
        p_finish_time='2020-12-17 11:32:45',
        p_send_location=
        {
          'name': "x36阿姨处",
          'longitude': 121.43101,
          'latitude': 31.0176
        },
        p_money='100'
    ),
    Task.Task(
        3,
        "求上海交大马克杯",
        "上海交大马克杯",
        [
            "https://gd2.alicdn.com/imgextra/i2/2200771700801/O1CN01jJjQjq1HmtsGaaGCl_!!2200771700801.jpg",
            "https://gd1.alicdn.com/imgextra/i2/475407752/O1CN01D5fHF1278SstKxHbC_!!475407752.jpg",
            "https://gd3.alicdn.com/imgextra/i3/475407752/O1CN0113fcY9278Sslva6px_!!475407752.jpg"
        ],
        {
          'name': "交通大学闵行校区",
          'longitude': 121.43102,
          'latitude': 31.0176
        },
        {
          'name': "莘庄地铁站",
          'longitude': 121.392186,
          'latitude': 31.116872
        },
        "30",
        "2020-12-20 11:32:45",
        "求上海交大LOGO纪念款马克杯。",
        1,
        "15619202209",
        user['hjh'],
        "2020-12-13 19:23:10",
        puchaser=user['root'],
        p_location='上海交大纪念品店',
        p_details='易碎品，已放至软件大楼圆厅。',
        p_finish_time='2020-12-15 11:32:45',
        p_send_location={
          'name': "莘庄地铁站",
          'longitude': 121.392186,
          'latitude': 31.116872
        },
        p_money='15'
    ),
    Task.Task(
        4,
        "求同济大学书签",
        "同济大学书签",
        [
            "https://sh.eastday.com/eastday/shnews/slideshow/20070520_3/images/00048523.jpg",
            "https://sh.eastday.com/images/thumbnailimg/month_1706/201706200654469656.jpg"
        ],
        {
          'name': "同济大学四平路校区",
          'longitude': 121.508532,
          'latitude': 31.289027
        },
        {
          'name': "交通大学闵行校区",
          'longitude': 121.43102,
          'latitude': 31.0176
        },
        "10",
        "2020-12-19 09:00:02",
        "求同济大学限定书签QAQ。",
        2,
        "15619202209",
        user['root'],
        "2020-12-13 21:30:11",
        puchaser=user['lh'],
        p_location='同济大学纪念品店',
        p_details='限定款书签',
        p_finish_time='2020-12-16 11:32:45',
        p_send_location={
          'name': "同济大学四平路校区邮政室",
          'longitude': 121.508532,
          'latitude': 31.289027
        },
        p_money='5',
        deliver=user['lh'],
        d_current_location='121.21792,31.28698',
        d_finish_time='2020-12-18 12:30:15',
        d_money='15'
    ),
    Task.Task(
        5,
        "上海交大钥匙扣",
        "上海交大钥匙扣",
        [
            "https://img.alicdn.com/imgextra/i2/67428829/TB24AZudpXXXXaFXXXXXXXXXXXX_!!67428829.jpg",
        ],
        {
          'name': "交通大学闵行校区",
          'longitude': 121.43102,
          'latitude': 31.0176
        },
        {
          'name': "虹桥机场T2",
          'longitude': 121.333972,
          'latitude': 31.200914
        },
        "25",
        "2020-12-11 22:35:43",
        "交大青花瓷钥匙扣。",
        2,
        "15619202209",
        user['lxr'],
        "2020-12-13 21:30:11",
        puchaser=user['hjh'],
        p_location='上海交大纪念品店',
        p_details='限定款钥匙扣',
        p_finish_time='2020-12-13 11:45:15',
        p_send_location={
          'name': "交通大学闵行校区",
          'longitude': 121.43102,
          'latitude': 31.0176
        },
        p_money='20',
        deliver=user['root'],
        d_current_location={
          'name': "交通大学闵行校区",
          'longitude': 121.43102,
          'latitude': 31.0176
        },
        d_finish_time='2020-12-15 14:30:11',
        d_money='10'
    )
]


class TaskPool:
    def __init__(self):
        self.currId = 1
        self.tasks = data

    def convertToDict(self, task):
        return {
            "id": task.id,
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
            "p_location": task.p_location,
            "p_finish_time": task.p_finish_time,
            "p_send_location": task.p_send_location,
            "p_details": task.p_details,
            "p_money": task.p_money,

            # status == 2:
            "deliver": task.deliver,
            "d_current_location": task.d_current_location,
            "d_finish_time": task.d_finish_time,
            "d_money": task.d_money,

            # status == 3:
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
                res.append(self.convertToDict(task))
        return res

    def getDeliveryTasks(self):
        res = []
        for task in self.tasks:
            if task.status == 1:
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
