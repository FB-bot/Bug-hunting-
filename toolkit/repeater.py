import requests

async def repeat(update,context):

    url=context.args[0]

    r=requests.get(url)

    await update.message.reply_text(f"Status {r.status_code}")
