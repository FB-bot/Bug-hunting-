async def generate(update,context):

    url=context.args[0]

    html=f'<form action="{url}" method="POST"></form>'

    await update.message.reply_text(html)
