import requests
from time import sleep
import threading

channel = # Enter your channel url

headers = {

# Enter your headers, I can't give mine.

}

data = '{"content":"!d bump","tts":false}'

def poster():
    count = 1
    while True:
        requests.post(channel, headers=headers, data=data)
        print(f'{count}. bump is done.')
        count += 1
        sleep(7200)

x = threading.Thread(target = poster)
x.start()

