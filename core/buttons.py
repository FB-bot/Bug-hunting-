from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def main_menu():

    keyboard = [
        [InlineKeyboardButton("🔎 Scan Website", callback_data="scan")],
        [InlineKeyboardButton("⚡ Fuzzer", callback_data="fuzz")],
        [InlineKeyboardButton("🧪 Tools", callback_data="tools")]
    ]

    return InlineKeyboardMarkup(keyboard)
