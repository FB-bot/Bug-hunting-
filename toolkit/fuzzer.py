import aiohttp

payloads = ["'", "<script>", "../"]

async def fuzz(update, context):

    if not context.args:
        await update.message.reply_text(
            "Usage:\n/fuzz https://site.com?id="
        )
        return

    base = context.args[0]

    hits = []

    async with aiohttp.ClientSession() as session:

        for p in payloads:
            try:
                async with session.get(base + p) as r:
                    if r.status == 200:
                        hits.append(p)
            except:
                pass

    await update.message.reply_text(
        f"Payload Hits:\n{hits}"
    )
