import os
import threading

from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler
)

from web import start_web

from core.engine import start_scan
from core.massscan import mass_scan
from core.internet_scan import internet_scan

from core.ui import panel
from core.animation import scanning, progress
from core.buttons import main_menu

from toolkit import (
    repeater,
    fuzzer,
    session,
    csrf,
    clickjack,
    api,
    websocket,
    sqli
)

TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    raise Exception("BOT_TOKEN missing")


# ================= START MENU =================
async def start(update, context):

    await update.message.reply_text(
        "⚡ BUGBOT-X READY",
        reply_markup=main_menu()
    )


# ================= BUTTON HANDLER =================
async def button_handler(update, context):

    query = update.callback_query
    await query.answer()

    data = query.data

    if data == "scan":
        await query.edit_message_text(
            "Use command:\n/scan example.com"
        )

    elif data == "fuzz":
        await query.edit_message_text(
            "Use command:\n/fuzz https://site.com?id="
        )

    elif data == "tools":
        await query.edit_message_text(
            "🧪 Available Tools:\n"
            "/sqli\n"
            "/repeat\n"
            "/csrf\n"
            "/clickjack\n"
            "/apitest\n"
            "/ws"
        )


# ================= FULL SCAN =================
async def scan(update, context):

    if not context.args:
        await update.message.reply_text("/scan example.com")
        return

    target = context.args[0]

    msg = await update.message.reply_text("Starting Scan...")

    await scanning(msg)
    await progress(msg)

    result, pdf = await start_scan(target, msg)

    await update.message.reply_text(
        panel("SCAN COMPLETE", result)
    )

    await update.message.reply_document(pdf)


# ================= WEB SERVER =================
threading.Thread(target=start_web).start()


# ================= TELEGRAM BOT =================
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("scan", scan))
app.add_handler(CommandHandler("mass", mass_scan))
app.add_handler(CommandHandler("internet", internet_scan))

# TOOLKIT
app.add_handler(CommandHandler("repeat", repeater.repeat))
app.add_handler(CommandHandler("fuzz", fuzzer.fuzz))
app.add_handler(CommandHandler("cookie", session.cookie))
app.add_handler(CommandHandler("csrf", csrf.generate))
app.add_handler(CommandHandler("clickjack", clickjack.test))
app.add_handler(CommandHandler("apitest", api.test))
app.add_handler(CommandHandler("ws", websocket.connect))
app.add_handler(CommandHandler("sqli", sqli.test))

# ⭐ BUTTON CLICK HANDLER
app.add_handler(CallbackQueryHandler(button_handler))

print("🚀 BUGBOT-X RUNNING")

app.run_polling()
