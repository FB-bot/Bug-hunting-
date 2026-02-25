import requests

async def scan(url):

    try:
        r=requests.get("http://"+url,timeout=5)
        return f"[STATUS] {r.status_code}"
    except:
        return "[STATUS] DOWN"
