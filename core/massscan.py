import asyncio
from core.engine import start_scan

async def load_targets():
    with open("data/targets.txt") as f:
        return f.read().splitlines()

async def worker(queue,update):

    while not queue.empty():

        target=await queue.get()

        try:
            result,pdf=await start_scan(target,update.message)

            await update.message.reply_document(pdf)

        except:
            await update.message.reply_text("Fail")

        queue.task_done()

async def mass_scan(update,context):

    await update.message.reply_text("Mass Scan Start")

    targets=await load_targets()

    queue=asyncio.Queue()

    for t in targets:
        await queue.put(t)

    workers=[asyncio.create_task(worker(queue,update))
             for _ in range(3)]

    await queue.join()

    for w in workers:
        w.cancel()

    await update.message.reply_text("Done")
