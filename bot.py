import os
from telegram.ext import ApplicationBuilder, CommandHandler

from keepalive import keep_alive

from core.engine import start_scan
from core.massscan import mass_scan
from core.internet_scan import internet_scan

from toolkit import repeater,fuzzer,session,csrf,clickjack,api,websocket

TOKEN = os.getenv("BOT_TOKEN")

async def scan(update,context):

    if not context.args:
        await update.message.reply_text("/scan example.com")
        return

    target=context.args[0]

    msg=await update.message.reply_text("Scanning...")

    result,pdf=await start_scan(target,msg)

    await update.message.reply_text(result)
    await update.message.reply_document(pdf)

app=ApplicationBuilder().token(TOKEN).build()

# scanner
app.add_handler(CommandHandler("scan",scan))
app.add_handler(CommandHandler("mass",mass_scan))
app.add_handler(CommandHandler("internet",internet_scan))

# toolkit
app.add_handler(CommandHandler("repeat",repeater.repeat))
app.add_handler(CommandHandler("fuzz",fuzzer.fuzz))
app.add_handler(CommandHandler("cookie",session.cookie))
app.add_handler(CommandHandler("csrf",csrf.generate))
app.add_handler(CommandHandler("clickjack",clickjack.test))
app.add_handler(CommandHandler("apitest",api.test))
app.add_handler(CommandHandler("ws",websocket.connect))

keep_alive()

print("BOT RUNNING ON RENDER")

app.run_polling()
