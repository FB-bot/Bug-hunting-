async def cookie(update,context):

    cookie=" ".join(context.args)

    await update.message.reply_text(cookie)
