from telegram import InlineKeyboardButton,InlineKeyboardMarkup

def main_menu():

    keyboard=[
        [InlineKeyboardButton("🧰 Tools",callback_data="tools_menu")]
    ]

    return InlineKeyboardMarkup(keyboard)


def tools_menu():

    keyboard=[
        [InlineKeyboardButton("💉 SQLi",callback_data="tool_sqli")],
        [InlineKeyboardButton("⚡ Fuzzer",callback_data="tool_fuzz")],
        [InlineKeyboardButton("🌐 Recon",callback_data="tool_recon")],
        [InlineKeyboardButton("🎯 Params",callback_data="tool_params")],
        [InlineKeyboardButton("⬅ Back",callback_data="back_main")]
    ]

    return InlineKeyboardMarkup(keyboard)
