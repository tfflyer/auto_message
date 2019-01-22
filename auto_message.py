from twilio.rest import Client
from datetime import datetime
import time
from threading import Timer
from wxpy import *
import requests
bot = None

account = "ACa52b7520cc7514d831e13c9502694cd1"
token = "42f21b95e0b53b436b4cf3c8c476d1b9"

from threading import Timer
from wxpy import *
import requests
bot = None
def get_news1():
#获取金山词霸每日一句，英文和翻译
    url = "http://open.iciba.com/dsapi/"
    r = requests.get(url)
    # print(r.json())
    contents = r.json()['content']
    note = r.json()['note']
    translation = r.json()['translation']
    return contents,note,translation
len=get_news1()


def send_mes(to_l, text, tw_mobile='+16602353919'):
    client = Client(account, token)
    try:
        message = client.messages.create(to=to_l,
                                         from_=tw_mobile,
                                         body=text)
        print('message status:', message.status)
        return True
    except Exception as e:
        print(e)
        return False


if __name__ == '__main__':
    greetings = {'6': 'Good moning!'}
    content=list(get_news1())
    print(content[0])
    print('Script running')
    while True:
        now = datetime.now()
        print('time', now)
        for key in greetings.keys():
            if now.hour == int(key):
                greetings.update({'6':content[0]})
                message = greetings.get(key, 'This is a message from tfflyer ')
                res = send_mes(to='+8613126883674', text=message)
                if res:
                    print('Message send ok at:',
                          datetime.strftime(now, '%Y-%m-%d %H:%M:%S'))
                    time.sleep(60*60)
                else:
                    print('Message send failure')
        time.sleep(5)
