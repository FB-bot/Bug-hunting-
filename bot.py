import os
import threading

from telegram.ext import ApplicationBuilder, CommandHandler

from web import start_web

from core.engine import start_scan
from core.massscan import mass_scan
from core.internet_scan import internet_scan

from toolkit import repeater,fuzzer,session,csrf,clickjack,api,websocket

TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    raise Exception("BOT_TOKEN missing")


async def scan(update, context):

    if not context.args:
        await update.message.reply_text("/scan example.com")
        return

    target = context.args[0]

    msg = await update.message.reply_text("Scanning...")

    result, pdf = await start_scan(target, msg)

    await update.message.reply_text(result)
    await update.message.reply_document(pdf)


# ✅ Start Flask in background
threading.Thread(target=start_web).start()

print("Web Server Started")


# ✅ Telegram bot MAIN THREAD এ চলবে
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("scan", scan))
app.add_handler(CommandHandler("mass", mass_scan))
app.add_handler(CommandHandler("internet", internet_scan))

app.add_handler(CommandHandler("repeat", repeater.repeat))
app.add_handler(CommandHandler("fuzz", fuzzer.fuzz))
app.add_handler(CommandHandler("cookie", session.cookie))
app.add_handler(CommandHandler("csrf", csrf.generate))
app.add_handler(CommandHandler("clickjack", clickjack.test))
app.add_handler(CommandHandler("apitest", api.test))
app.add_handler(CommandHandler("ws", websocket.connect))

print("Telegram Bot Running")

app.run_polling()
