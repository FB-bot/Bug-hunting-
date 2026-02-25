import requests

async def test(update,context):

    url=context.args[0]
    token=context.args[1]

    r=requests.get(url,headers={"Authorization":token})

    await update.message.reply_text(str(r.status_code))
