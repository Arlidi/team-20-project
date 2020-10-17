import requests
import json
from datetime import datetime
from time import sleep

Cam_ID = '0AF201' # 000001 - FFFFFF  hexadecimal

now = datetime.now()

interval = 2

txt = {
    "cam_id": Cam_ID,
    "cam_fire_danger": "False",
    "cam_time": '{}.{}.{} {}:{}'.format(now.year, now.month, now.day, now.hour, now.minute)
}

def start(Cam_ID):
    r = requests.get('http://127.0.0.1:8000/api/v1/all/').text
    list1 = json.loads(r)
    for i in list1:
        if i['cam_id'] == Cam_ID:
            return i['id']
    requests.post('http://127.0.0.1:8000/api/v1/create/', txt)
    return start(Cam_ID)

class Cam():
    def __init__(self, id):
        self.id = start(id)

    def send_rq(self):
        data = {
            "cam_id": Cam_ID,
            "cam_fire_danger": "True",
            "cam_time": '{}.{}.{} {}:{}'.format(now.year, now.month, now.day, now.hour, now.minute)
        }
        requests.put('http://127.0.0.1:8000/api/v1/deteil/{}'.format(self.id), data)

    def get_temperature(self):
        return int(input("temperature: "))

    def analyze(self, temp1, temp2):
        if temp2 >= 100 or temp2 - temp1 >= 30:
            return True
        else:
            return False

def main(Cam_ID):
    camera = Cam(Cam_ID)
    temperature_1 = temperature_2 = camera.get_temperature()
    while True:
        if camera.analyze(temperature_1, temperature_2):
            camera.send_rq()
        sleep(interval)
        temperature_1, temperature_2 = temperature_2, camera.get_temperature()


if __name__ == '__main__':
    main(Cam_ID)
