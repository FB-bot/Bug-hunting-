import requests
import re

async def params(update,context):

    domain=context.args[0]

    r=requests.get("http://"+domain)

    params=set(re.findall(r"[?&]([a-zA-Z0-9_]+)=",r.text))

    await update.message.reply_text(
        "🎯 Parameters:\n"+str(params)
    )
