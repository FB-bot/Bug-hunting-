from core.internet_targets import get_targets
from core.engine import start_scan

async def internet_scan(update,context):

    msg=await update.message.reply_text("Collecting")

    targets=await get_targets()

    for t in targets:

        await msg.edit_text(f"Scanning {t}")

        result,pdf=await start_scan(t,msg)

        await update.message.reply_document(pdf)

    await update.message.reply_text("Finished")
