import requests

async def scan(url):

    payload="<script>alert(1)</script>"

    try:
        r=requests.get("http://"+url+payload)
        if payload in r.text:
            return "[XSS] Possible"
    except:
        pass

    return "[XSS] Not Found"
