import aiosqlite

async def save(target,result):

    db=await aiosqlite.connect("data/scans.db")

    await db.execute(
        "CREATE TABLE IF NOT EXISTS scans(target,result)"
    )

    await db.execute(
        "INSERT INTO scans VALUES(?,?)",(target,result)
    )

    await db.commit()
    await db.close()
