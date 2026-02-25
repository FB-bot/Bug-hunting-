import requests

async def scan(url):

    r=requests.get("http://"+url)

    return f"[HEADERS] Server: {r.headers.get('Server')}"
