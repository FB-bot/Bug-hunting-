import os
import threading

from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler
)

from web import start_web

from core.buttons import main_menu, tools_menu
from core.animation import scanning
from core.ui import panel

from bounty import recon, params, jsfinder
from toolkit import sqli, fuzzer

TOKEN = os.getenv("BOT_TOKEN")

threading.Thread(target=start_web).start()

app = ApplicationBuilder().token(TOKEN).build()


# ================= START =================
async def start(update, context):

    await update.message.reply_text(
        panel("BUGBOT-X", "Select Option"),
        reply_markup=main_menu()
    )


# ================= BUTTON SYSTEM =================
async def buttons(update, context):

    query = update.callback_query
    await query.answer()

    data = query.data

    # OPEN TOOL MENU
    if data == "tools":
        await query.edit_message_text(
            "🧰 Select Tool",
            reply_markup=tools_menu()
        )

    # BACK BUTTON
    elif data == "back":
        await query.edit_message_text(
            "Main Menu",
            reply_markup=main_menu()
        )

    # ---------- RECON ----------
    elif data == "recon":

        await query.edit_message_text("🌐 Running Recon...")
        await scanning(query)

        context.args = ["example.com"]
        await recon.recon(query, context)

    # ---------- PARAMS ----------
    elif data == "params":

        await query.edit_message_text("🎯 Finding Parameters...")
        await scanning(query)

        context.args = ["example.com"]
        await params.params(query, context)

    # ---------- JS FINDER ----------
    elif data == "js":

        await query.edit_message_text("📜 Searching JS Files...")
        await scanning(query)

        context.args = ["example.com"]
        await jsfinder.jsfinder(query, context)

    # ---------- SQLi ----------
    elif data == "sqli":

        await query.edit_message_text("💉 SQLi Testing...")
        await scanning(query)

        context.args = ["https://example.com?id="]
        await sqli.test(query, context)

    # ---------- FUZZER ----------
    elif data == "fuzz":

        await query.edit_message_text("⚡ Fuzzing...")
        await scanning(query)

        context.args = ["https://example.com?id="]
        await fuzzer.fuzz(query, context)


# COMMAND SUPPORT ALSO
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("recon", recon.recon))
app.add_handler(CommandHandler("params", params.params))
app.add_handler(CommandHandler("js", jsfinder.jsfinder))
app.add_handler(CommandHandler("sqli", sqli.test))
app.add_handler(CommandHandler("fuzz", fuzzer.fuzz))

app.add_handler(CallbackQueryHandler(buttons))

print("🔥 FULL BUTTON SYSTEM ACTIVE")

app.run_polling()
