import asyncio

async def scanning(msg):

    frames = [
        "🔎 Initializing scan.",
        "🔎 Initializing scan..",
        "🔎 Initializing scan..."
    ]

    for _ in range(2):
        for f in frames:
            await msg.edit_text(f)
            await asyncio.sleep(0.5)


async def progress(msg):

    steps = [
        "▱▱▱▱▱▱▱▱▱▱ 0%",
        "▰▱▱▱▱▱▱▱▱▱ 10%",
        "▰▰▱▱▱▱▱▱▱▱ 30%",
        "▰▰▰▰▱▱▱▱▱▱ 50%",
        "▰▰▰▰▰▰▱▱▱▱ 70%",
        "▰▰▰▰▰▰▰▰▱▱ 90%",
        "▰▰▰▰▰▰▰▰▰▰ 100%"
    ]

    for s in steps:
        await msg.edit_text(f"⚡ Scanning\n{s}")
        await asyncio.sleep(0.6)
