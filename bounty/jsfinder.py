import requests
import re

async def jsfinder(update,context):

    domain=context.args[0]

    url="http://"+domain

    r=requests.get(url,timeout=5)

    js_files=re.findall(r'src=["\'](.*?\.js)',r.text)

    if not js_files:
        await update.message.reply_text("No JS files found")
        return

    result="\n".join(js_files)

    await update.message.reply_text(
        "📜 JavaScript Files:\n\n"+result
    )
