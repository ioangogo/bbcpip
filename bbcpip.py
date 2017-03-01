import os
import time
import datetime
lastsecond=54
while True:
    now = datetime.datetime.now()
    if now.minute == 59 and now.second > 54 and now.second > lastsecond:
        print("pip")
        if now.second != lastsecond:
            os.system('play -q shortpip.wav')
            lastsecond = now.second
    elif now.minute == 0 and now.second == 0:
        if now.second != lastsecond:
            os.system('play -q longpip.wav')
            print("BEEEEEEP")
    lastsecond = now.second
    time.sleep(0.01)
