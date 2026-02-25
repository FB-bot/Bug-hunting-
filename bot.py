import os
import threading

from telegram.ext import ApplicationBuilder, CommandHandler
from web import app

from core.engine import start_scan
from core.massscan import mass_scan
from core.internet_scan import internet_scan

from toolkit import repeater,fuzzer,session,csrf,clickjack,api,websocket

TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    raise Exception("BOT_TOKEN missing")


async def scan(update,context):

    if not context.args:
        await update.message.reply_text("/scan example.com")
        return

    target=context.args[0]

    msg=await update.message.reply_text("Scanning...")

    result,pdf=await start_scan(target,msg)

    await update.message.reply_text(result)
    await update.message.reply_document(pdf)


def start_bot():

    tg = ApplicationBuilder().token(TOKEN).build()

    tg.add_handler(CommandHandler("scan",scan))
    tg.add_handler(CommandHandler("mass",mass_scan))
    tg.add_handler(CommandHandler("internet",internet_scan))

    tg.add_handler(CommandHandler("repeat",repeater.repeat))
    tg.add_handler(CommandHandler("fuzz",fuzzer.fuzz))
    tg.add_handler(CommandHandler("cookie",session.cookie))
    tg.add_handler(CommandHandler("csrf",csrf.generate))
    tg.add_handler(CommandHandler("clickjack",clickjack.test))
    tg.add_handler(CommandHandler("apitest",api.test))
    tg.add_handler(CommandHandler("ws",websocket.connect))

    print("Telegram Bot Started")

    tg.run_polling()


# Run bot in background thread
threading.Thread(target=start_bot).start()


# Run Flask Web Service
port = int(os.environ.get("PORT", 10000))
app.run(host="0.0.0.0", port=port)
