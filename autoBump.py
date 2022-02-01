import requests
from time import sleep
import threading
from random import randint

channel = # Enter your channel url
headers = {
            # Enter your headers
}

json_file = # The program will read the content of the url in order to check what Disboard said. Give a filename to save that information.


data = '{"content":"!d bump","tts":false}'
success_notification = '{"content":"ACTIVATED!","tts":false}'
fail_notification = '{"content":"NOT ACTIVATED!","tts":false}'

def poster():
    count = 1
    send_notification = True
    success = True
    time_left = 0

    while True:
        response = requests.post(channel, headers=headers, data=data)
        get_response = requests.get(channel, headers=headers)

        f = open(json_file, "w")
        f.write(str(get_response.json()))
        f.close()

        f = open(json_file, "r")

        list_f = f.readline().split()

        if "bekle'," in list_f[42]:
            requests.post(channel, headers=headers, data=fail_notification)
            time_left = int(list_f[40])
            print(f"Will be activated in {time_left} minutes")

        sleep(int(time_left)*60 + 10)

        f.close()

        f = open(json_file, "w")
        f.write("")
        f.close()

        if response.status_code == 200:
            if send_notification:
                requests.post(content, headers=headers, data=success_notification)    
            print(f'Bump {count} is done!')
            send_notification = False

        elif response.status_code in [401,404]:
            print('[-] An error accured, bump didn\'t succeed')

        else:
            print(f'[*] Unexpected response with the status code of {status_code}')

        count += 1
        sleep(randint(7205,7210))

x = threading.Thread(target = poster)
x.start()
