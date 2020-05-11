import requests
import time

starttime = time.time()
count = 0
x = True
while x == True:

    print('tick')

    url = 'https://harry-search.herokuapp.com/'
    requests.get(url)

    time.sleep(1200.0 - ((time.time() - starttime) % 1200.0))

    count = count + 1

    if count == 51:
        x = False
