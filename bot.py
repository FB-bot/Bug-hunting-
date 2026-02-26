import os
import threading

from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler
)

from web import start_web

from core.buttons import main_menu, tools_menu
from core.ui import panel

TOKEN = os.getenv("BOT_TOKEN")

# start render web server
threading.Thread(target=start_web).start()

app = ApplicationBuilder().token(TOKEN).build()


# ================= START =================
async def start(update, context):

    await update.message.reply_text(
        panel("BUGBOT-X", "Select Option"),
        reply_markup=main_menu()
    )


# ================= BUTTON HANDLER =================
async def buttons(update, context):

    query = update.callback_query
    await query.answer()

    data = query.data

    # OPEN TOOLS MENU
    if data == "tools":
        await query.edit_message_text(
            "🧰 Select Tool",
            reply_markup=tools_menu()
        )

    # BACK BUTTON
    elif data == "back":
        await query.edit_message_text(
            "⚡ Main Menu",
            reply_markup=main_menu()
        )

    # TOOL BUTTONS
    elif data == "recon":
        await query.edit_message_text(
            "Use:\n/recon example.com"
        )

    elif data == "params":
        await query.edit_message_text(
            "Use:\n/params example.com"
        )

    elif data == "js":
        await query.edit_message_text(
            "Use:\n/js example.com"
        )

    elif data == "sqli":
        await query.edit_message_text(
            "Use:\n/sqli https://site.com?id="
        )

    elif data == "fuzz":
        await query.edit_message_text(
            "Use:\n/fuzz https://site.com?id="
        )


# ================= REGISTER =================
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(buttons))

print("✅ BUTTON SYSTEM WORKING")

app.run_polling()
