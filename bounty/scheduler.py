import asyncio
from bounty import recon

running=False

async def autorecon(update,context):

    global running

    if running:
        await update.message.reply_text("Already Running")
        return

    running=True

    await update.message.reply_text("🤖 Auto Recon Started")

    while running:

        try:
            await recon.recon(update,context)
        except:
            pass

        await asyncio.sleep(3600)   # every 1 hour


async def stoprecon(update,context):

    global running
    running=False

    await update.message.reply_text("Auto Recon Stopped")
