import requests

payload="'"

async def test(update,context):

    url=context.args[0]

    r=requests.get(url+payload)

    if "sql" in r.text.lower():
        await update.message.reply_text(
            "⚠️ Possible SQLi"
        )
    else:
        await update.message.reply_text(
            "✅ SQLi Not Detected"
        )
