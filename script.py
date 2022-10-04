import json
from datetime import datetime


def get_duration(duration):
    hours = int(duration / 3600)
    minutes = int(duration % 3600 / 60)
    seconds = int((duration % 3600) % 60)
    return '{:02d}:{:02d}:{:02d}'.format(hours, minutes, seconds)

f = open('result.json')

data = json.load(f)
remote_time = {}

for i in data['messages']:
    time_status = i['text'][0]
    time_status = time_status.split(" - ")
    time = datetime.strptime(time_status[0], '%Y/%m/%d %H:%M:%S')
    status = time_status[1][:-1]
    login = i['text'][2]
    login = login.split(", ")
    login = login[1]
    if login in remote_time.keys():
        if remote_time[login]['flag'] == status:
            continue
        else:
            if status == 'CONNECT':
                remote_time[login]['flag'] = status
                remote_time[login][status] = time
            else:
                remote_time[login]['time'] += (
                    (time - remote_time[login]['CONNECT']).total_seconds()
                )
                remote_time[login]['flag'] = status

    else:
        remote_time[login] = {}
        remote_time[login]['flag'] = status
        remote_time[login][status] = time
        remote_time[login]['time'] = 0
for remote in sorted(remote_time):
    print(remote, get_duration(remote_time[remote]['time']))
