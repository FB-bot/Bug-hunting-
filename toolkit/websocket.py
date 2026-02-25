from websocket import create_connection

async def connect(update,context):

    url=context.args[0]

    ws=create_connection(url)

    ws.send("hello")

    res=ws.recv()

    ws.close()

    await update.message.reply_text(res)
