import asyncio

async def loading(msg):

    frames=[
        "⚡ Loading.",
        "⚡ Loading..",
        "⚡ Loading..."
    ]

    for _ in range(2):
        for f in frames:
            await msg.edit_text(f)
            await asyncio.sleep(0.5)


async def scanning(msg):

    steps=[
        "🔎 Recon Running",
        "🧪 Testing",
        "📂 Searching",
        "📄 Finishing"
    ]

    for s in steps:
        await msg.edit_text(s)
        await asyncio.sleep(1)
