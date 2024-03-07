import requests
import sys

def looper():
    for word in sys.stdin:
        res= requests.get(url=f"http://headers.jsontest.com/{word}")
        if res.status_code==404:
            looper()
        else:
            data=res.json()
            print(data)
            print(res.status_code)

    #data = res.json()
    #print(data)
            
looper()