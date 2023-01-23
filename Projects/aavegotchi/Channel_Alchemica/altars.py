import datetime
import time
import requests


def send(c):
    base_url = f'https://api.telegram.org/bot5373652188:AAF46DEh9k56Jaqt6teZCgXEC-S1_cPXLGI/sendMessage?chat_id=-710589490&text=District {c}\nin 20 minutes'
    requests.get(base_url)
    time.sleep(60)


def send41():
    base_url = f'https://api.telegram.org/bot5373652188:AAF46DEh9k56Jaqt6teZCgXEC-S1_cPXLGI/sendMessage?chat_id=-710589490&text=District 41 in 20 minutes\n24 minutes\n27 minutes\n34 minutes\n40 minutes'
    requests.get(base_url)
    time.sleep(60)


while True:
    if (datetime.datetime.now().time().hour == 10) or (datetime.datetime.now().time().hour == 22) and (datetime.datetime.now().time().minute == 36):
        send(c='5  middle up, lower district 22')
    elif (datetime.datetime.now().time().hour == 10) or (datetime.datetime.now().time().hour == 22) and (datetime.datetime.now().time().minute == 16):
        send(c='5 spawned')
    if (datetime.datetime.now().time().hour == 11) or (datetime.datetime.now().time().hour == 23) and (datetime.datetime.now().time().minute == 1):
        send(c='5  upper right')
    if (datetime.datetime.now().time().hour == 10) or (datetime.datetime.now().time().hour == 22) and (datetime.datetime.now().time().minute == 57):
        send(c='3  middle right')
    if (datetime.datetime.now().time().hour == 11) or (datetime.datetime.now().time().hour == 23) and (datetime.datetime.now().time().minute == 4):
        send41()
