import requests

subs=["www","api","dev","test","admin"]

async def recon(update,context):

    domain=context.args[0]

    found=[]

    for s in subs:
        url=f"http://{s}.{domain}"
        try:
            r=requests.get(url,timeout=3)
            if r.status_code<500:
                found.append(url)
        except:
            pass

    await update.message.reply_text(
        "🌐 Recon Result\n\n"+ "\n".join(found)
    )
