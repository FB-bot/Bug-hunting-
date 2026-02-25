from scanners import status,headers,sqli,xss,admin,dirscan

async def run(target,subs):

    results=[]

    results.append(await status.scan(target))
    results.append(await headers.scan(target))
    results.append(await sqli.scan(target))
    results.append(await xss.scan(target))
    results.append(await admin.scan(target))
    results.append(await dirscan.scan(target))

    for s in subs:
        results.append(await status.scan(s))

    return results
