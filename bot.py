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

from bounty import recon,params
from toolkit import sqli,fuzzer

TOKEN=os.getenv("BOT_TOKEN")

threading.Thread(target=start_web).start()

app=ApplicationBuilder().token(TOKEN).build()


# START
async def start(update,context):
    await update.message.reply_text(
        panel("BUGBOT-X","System Online"),
        reply_markup=main_menu()
    )


# BUTTON HANDLER
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
            "⚡ Main Menu",
            reply_markup=main_menu()
        )

    elif data=="tool_sqli":
        await query.edit_message_text("💉 SQLi Loading")
        await loading(query)
        await query.message.reply_text(
            panel("SQLi Tool","/sqli https://site.com?id=")
        )

    elif data=="tool_fuzz":
        await query.edit_message_text("⚡ Fuzzer Ready")
        await scanning(query)
        await query.message.reply_text(
            panel("Fuzzer","/fuzz https://site.com?id=")
        )

    elif data=="tool_recon":
        await query.edit_message_text("🌐 Recon Module")
        await scanning(query)
        await query.message.reply_text(
            panel("Recon","/recon example.com")
        )

    elif data=="tool_params":
        await query.edit_message_text("🎯 Params Finder")
        await scanning(query)
        await query.message.reply_text(
            panel("Params","/params example.com")
        )


app.add_handler(CommandHandler("start",start))
app.add_handler(CommandHandler("recon",recon.recon))
app.add_handler(CommandHandler("params",params.params))
app.add_handler(CommandHandler("sqli",sqli.test))
app.add_handler(CommandHandler("fuzz",fuzzer.fuzz))

app.add_handler(CallbackQueryHandler(buttons))

print("🔥 BUGBOT RUNNING")

app.run_polling()
