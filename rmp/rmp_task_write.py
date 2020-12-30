import requests, json
from convertTool import rmpFormat2task, task2rmpFormat, print_task
from initial_data import user, tasks
import pdb


task_rmp_data = []
for task in tasks:
    t = {}
    for key, value in task2rmpFormat(task).items():
        if value:
            t[key] = value
    task_rmp_data.append(t)

# pdb.set_trace()
# post
url = 'http://202.120.40.87:14642/rmp-resource-service/project/5fe7edf32ef44e00153874ff/resource/task'
headers = {
    'Content-Type': 'application/json',
    'passwd': 'lxr123456',
}
# for t in task_rmp_data:
#     r = requests.post(url=url, headers=headers, data=json.dumps(t))
#     print(r.text)

# get
url = 'http://202.120.40.87:14642/rmp-resource-service/project/5fe7edf32ef44e00153874ff/resource/task'
r = requests.get(url=url)
data = json.loads(r.text)['data']

with open('other/res.json', 'w') as f:
    json.dump(data, f)