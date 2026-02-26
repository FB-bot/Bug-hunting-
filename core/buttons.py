from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def main_menu():
    keyboard = [
        [InlineKeyboardButton("🧰 Tools", callback_data="tools")]
    ]
    return InlineKeyboardMarkup(keyboard)


def tools_menu():
    keyboard = [
        [InlineKeyboardButton("🌐 Recon", callback_data="recon")],
        [InlineKeyboardButton("🎯 Params", callback_data="params")],
        [InlineKeyboardButton("📜 JS Finder", callback_data="js")],
        [InlineKeyboardButton("💉 SQLi", callback_data="sqli")],
        [InlineKeyboardButton("⚡ Fuzzer", callback_data="fuzz")],
        [InlineKeyboardButton("⬅ Back", callback_data="back")]
    ]
    return InlineKeyboardMarkup(keyboard)
