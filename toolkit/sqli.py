import aiohttp

payload = "'"

async def test(update, context):

    if not context.args:
        await update.message.reply_text(
            "Usage:\n/sqli https://site.com?id="
        )
        return

    url = context.args[0] + payload

    await update.message.reply_text("💉 Testing SQL Injection...")

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, timeout=10) as r:

                text = await r.text()

                if "sql" in text.lower():
                    await update.message.reply_text(
                        "⚠️ Possible SQL Injection Found"
                    )
                else:
                    await update.message.reply_text(
                        "✅ No SQLi Detected"
                    )

    except Exception as e:
        await update.message.reply_text(
            f"Error: {str(e)}"
        )
