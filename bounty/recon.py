import aiohttp

subs = ["www", "api", "dev", "test", "admin"]

async def recon(update, context):

    if not context.args:
        await update.message.reply_text("/recon example.com")
        return

    domain = context.args[0]

    found = []

    async with aiohttp.ClientSession() as session:

        for s in subs:
            url = f"http://{s}.{domain}"

            try:
                async with session.get(url, timeout=5) as r:
                    if r.status < 500:
                        found.append(url)
            except:
                pass

    await update.message.reply_text(
        "🌐 Recon Result\n\n" + "\n".join(found)
    )
