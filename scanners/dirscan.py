import requests

async def scan(url):

    found=[]

    with open("wordlist.txt") as f:
        words=f.read().splitlines()

    for w in words:
        try:
            r=requests.get(f"http://{url}/{w}")
            if r.status_code==200:
                found.append(w)
        except:
            pass

    return "[DIR] "+str(found)
