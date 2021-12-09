import urllib.request, time, datetime,random
from socket import timeout
def relay(number, state):
    # Your IP here.
    ip = "x.x.x.x"
    try:
        if state == 1:
            print(f"Relay is active.\n")
        if state == 0:
            print(f"Relay is off.\n")
        urllib.request.urlopen(url=f'http://{ip}/state.xml?relay{number}State={state}&noReply=1', timeout=.1)
    except timeout:
        pass
firstrun = True
while True:  
    try:
        now = datetime.datetime.now()
        check = now.strftime("%H:%M:%S").split(":")
        # Check if time is between 4:00PM and 10:30PM
        if (int(check[0]) > 16) and (int(check[0]) <= 21 or ((int(check[0]) == 22 and int(check[1]) < 30))):
                if firstrun == True:
                    waittime = random.randrange(0,600)
                    print(f"Delaying first run for {waittime} seconds.\n")
                    time.sleep(waittime)
                waittime = random.randrange(300,900)
                print(f"Next action in {waittime} seconds.\n")
                time.sleep(waittime)
                relay(1,1)
                waittime = random.randrange(300,900)
                print(f"Next action in {waittime} seconds.\n")
                time.sleep(waittime)
                relay(1,0)
                firstrun = False
        else:
            time.sleep(60)
            firstrun = True
    except KeyboardInterrupt:
        relay(1,0)
        exit(1)