import dns.resolver

async def subdomains(domain):

    words=["www","api","dev","test"]

    found=[]

    for w in words:
        try:
            dns.resolver.resolve(f"{w}.{domain}")
            found.append(f"{w}.{domain}")
        except:
            pass

    return found
