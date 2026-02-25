import requests

paths=["admin","login","dashboard"]

async def scan(url):

    found=[]

    for p in paths:
        try:
            r=requests.get(f"http://{url}/{p}")
            if r.status_code==200:
                found.append(p)
        except:
            pass

    return "[ADMIN] "+str(found)
