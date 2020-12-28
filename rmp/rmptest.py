import requests, json

# get
url = 'http://202.120.40.87:14642/rmp-resource-service/project/5fe7edf32ef44e00153874ff/resource/book/'
r = requests.get(url=url)
print(r.text)

# post
url = 'http://202.120.40.87:14642/rmp-resource-service/project/5fe7edf32ef44e00153874ff/resource/book/'
headers = {
    'Content-Type': 'application/json',
    'passwd': 'lxr123456',
}
data = {'ID':1, 'name':'test'}
r = requests.post(url=url, headers=headers, data=json.dumps(data))
print(r.text)

# put
url = 'http://202.120.40.87:14642/rmp-resource-service/project/5fe7edf32ef44e00153874ff/resource/book/'
headers = {
    'Content-Type': 'application/json',
}
data = {'ID':2, 'name':'test'}
r = requests.put(url=url+'1', headers=headers, data=json.dumps(data))
print(r.text)