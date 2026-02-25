async def test(update,context):

    url=context.args[0]

    await update.message.reply_text(
        f'<iframe src="{url}"></iframe>'
    )
