import requests
import re

patterns=[
    r"AIza[0-9A-Za-z-_]{35}",      # Google API
    r"sk_live_[0-9a-zA-Z]{24}",    # Stripe
    r"AKIA[0-9A-Z]{16}",           # AWS
    r"api_key.*?['\"](.*?)['\"]",
    r"token.*?['\"](.*?)['\"]"
]

async def secrets(update,context):

    js_url=context.args[0]

    r=requests.get(js_url,timeout=5)

    found=[]

    for p in patterns:
        matches=re.findall(p,r.text)
        found.extend(matches)

    if found:
        await update.message.reply_text(
            "🔥 Possible Secrets Found:\n\n"+str(found)
        )
    else:
        await update.message.reply_text(
            "✅ No secrets detected"
        )
