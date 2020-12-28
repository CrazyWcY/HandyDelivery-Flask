import requests, json


# https://lbs.amap.com/api/webservice/guide/api/direction#distance

def get_url(origin, destination):
    return 'https://restapi.amap.com/v3/distance?origins={},{}&destination={},{}&output=JSON&type=0&key=8c444ac8409a4a2ea2b1b3bc8f842e98'.format(
        origin[0],origin[1],destination[0],destination[1])

def get_distance(origin, destination):
    url = get_url(origin, destination)
    r = requests.get(url=url)
    obj = json.loads(r.text)
    return obj['results'][0]['distance']

# for purchaser
def nearest_first(tasks, cur_location):
    # 距离：当前位置与商品期待购买位置
    task_dis = [(task, get_distance(cur_location, task.d_destination)) for task in tasks]
    task_dis.sort(key=lambda item: item[1]) # ascending
    return [item[0] for item in task_dis]

# for delivery
def shortest_first(tasks, cur_location):
    # 距离：当前位置与发货位置 + 发货位置与目标位置距离
    task_dis = [(task, get_distance(cur_location, task.d_destination)+get_distance(task.d_destination, task.p_destination)) for task in tasks]
    task_dis.sort(key=lambda item: item[1]) # ascending
    return [item[0] for item in task_dis]


print(get_distance((121.50904,31.33541),(121.43102,31.0176)))