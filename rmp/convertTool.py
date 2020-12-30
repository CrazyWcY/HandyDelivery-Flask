import sys
sys.path.append('..')
import Task
from TaskPool import user


def print_task(task):
    for key,value in task.__dict__.items():
        print('{}: {}'.format(key,value))


def rmpFormat2task(data):
    good_pictures = []
    if data['good_pictures_1']:
        good_pictures.append(data['good_pictures_1']) 
    if data['good_pictures_2']:
        good_pictures.append(data['good_pictures_2']) 
    if data['good_pictures_3']:
        good_pictures.append(data['good_pictures_3'])        
    
    return Task.Task(
        id              = data['task_id'],
        p_title         = data['p_title'],
        good            = data['good'],
        good_pictures   = good_pictures,
        p_destination   = {
            'name': data['p_destination_name'],
            'longitude': data['p_destination_longitude'],
            'latitude': data['p_destination_latitude'],
        },
        d_destination   = {
            'name': data['d_destination_name'],
            'longitude': data['d_destination_longitude'],
            'latitude': data['d_destination_latitude'],
        },
        money           = data['money'],
        deadline        = data['deadline'],
        details         = data['details'],
        status          = data['status'],
        phone           = data['phone'],
        author          = user[data['author']],
        time            = data['time'],
        puchaser        = user[data['puchaser']] if data['puchaser'] else None,
        p_location      = data['p_location'],
        p_finish_time   = data['p_finish_time'],
        p_send_location = {
            'name': data['p_send_location_name'],
            'longitude': data['p_send_location_longitude'],
            'latitude': data['p_send_location_latitude'],
        }  if data['p_send_location_name'] else None,
        p_details       = data['p_details'],
        p_money         = data['p_money'],
        deliver         = user[data['deliver']]  if data['deliver'] else None,
        d_current_location  = {
            'name': data['d_current_location_name'],
            'longitude': data['d_current_location_longitude'],
            'latitude': data['d_current_location_latitude'],
        }  if data['d_current_location_name'] else None,     
        d_finish_time   = data['task_id'],
        d_money         = data['d_money'],
        appraise        = data['appraise'],
        p_appraise      = data['p_appraise'],
        d_appraise      = data['d_appraise'],
        special_user    = user[data['special_user']]  if data['special_user'] else None,
    )

def task2rmpFormat(task):
    data = {}
        
    data['task_id'] = task.id
    data['p_title'] = task.p_title
    data['good'] = task.good

    data['good_pictures_1'] = None
    data['good_pictures_2'] = None
    data['good_pictures_3'] = None
    i = 1
    for pic in task.good_pictures:
        data['good_pictures_{}'.format(i)] = pic
        i += 1  

    data['p_destination_name'] = task.p_destination['name']
    data['p_destination_longitude'] = task.p_destination['longitude']
    data['p_destination_latitude'] = task.p_destination['latitude']

    data['d_destination_name'] = task.d_destination['name']
    data['d_destination_longitude'] = task.d_destination['longitude']
    data['d_destination_latitude'] = task.d_destination['latitude']

    data['money'] = task.money
    data['deadline'] = task.deadline
    data['details'] = task.details
    data['status'] = task.status
    data['phone'] = task.phone
    data['author'] = task.author['id']
    data['time'] = task.time
    if task.puchaser:
        data['puchaser'] = task.puchaser['id']
    else:
        data['puchaser'] = None

    data['p_location'] = task.p_location

    data['p_finish_time'] = task.p_finish_time

    if task.p_send_location:
        data['p_send_location_name'] = task.p_send_location['name']
        data['p_send_location_longitude'] = task.p_send_location['longitude']
        data['p_send_location_latitude'] = task.p_send_location['latitude']
    else:
        data['p_send_location_name'] = None
        data['p_send_location_longitude'] = None
        data['p_send_location_latitude'] = None

    data['p_details'] = task.p_details
    data['p_money'] = task.p_money
    if task.deliver:
        data['deliver'] = task.deliver['id']
    else:
        data['deliver'] = None

    if task.d_current_location:
        data['d_current_location_name'] = task.d_current_location['name']
        data['d_current_location_longitude'] = task.d_current_location['longitude']
        data['d_current_location_latitude'] = task.d_current_location['latitude']
    else:
        data['d_current_location_name'] = None
        data['d_current_location_longitude'] = None
        data['d_current_location_latitude'] = None

    data['d_finish_time'] = task.d_finish_time
    data['d_money'] = task.d_money
    data['appraise'] = task.appraise
    data['p_appraise'] = task.p_appraise
    data['d_appraise'] = task.d_appraise
    if task.special_user:
        data['special_user'] = task.special_user['id']
    else:
        data['special_user'] = None

    return data
