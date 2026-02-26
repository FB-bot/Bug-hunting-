import os
import threading

from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler
)

from web import start_web

from core.buttons import main_menu,tools_menu
from core.animation import loading,scanning
from core.ui import panel

from bounty import recon,params,jsfinder,secrets,scheduler
from toolkit import sqli,fuzzer

TOKEN=os.getenv("BOT_TOKEN")

threading.Thread(target=start_web).start()

app=ApplicationBuilder().token(TOKEN).build()


# START
async def start(update,context):

    await update.message.reply_text(
        panel("BUGBOT-X PRO","Bug Hunting Mode Active"),
        reply_markup=main_menu()
    )


# BUTTON MENU
async def buttons(update,context):

    query=update.callback_query
    await query.answer()

    data=query.data

    if data=="tools_menu":
        await query.edit_message_text(
            "🧰 Select Tool",
            reply_markup=tools_menu()
        )

    elif data=="back_main":
        await query.edit_message_text(
            "Main Menu",
            reply_markup=main_menu()
        )


app.add_handler(CommandHandler("start",start))

# CORE BOUNTY COMMANDS
app.add_handler(CommandHandler("recon",recon.recon))
app.add_handler(CommandHandler("params",params.params))
app.add_handler(CommandHandler("js",jsfinder.jsfinder))
app.add_handler(CommandHandler("secret",secrets.secrets))

# AUTO RECON
app.add_handler(CommandHandler("autorecon",scheduler.autorecon))
app.add_handler(CommandHandler("stoprecon",scheduler.stoprecon))

# TOOLKIT
app.add_handler(CommandHandler("sqli",sqli.test))
app.add_handler(CommandHandler("fuzz",fuzzer.fuzz))

app.add_handler(CallbackQueryHandler(buttons))

print("🔥 BUGBOT PRO MODE RUNNING")

app.run_polling()
