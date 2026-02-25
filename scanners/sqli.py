import requests

async def scan(url):

    payload="'"

    try:
        r=requests.get("http://"+url+payload)
        if "sql" in r.text.lower():
            return "[SQLI] Possible"
    except:
        pass

    return "[SQLI] Not Found"
