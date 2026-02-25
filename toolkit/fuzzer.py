import requests

payloads=["'","../","<script>1</script>"]

async def fuzz(update,context):

    url=context.args[0]

    hits=[]

    for p in payloads:
        try:
            r=requests.get(url+p)
            if r.status_code==200:
                hits.append(p)
        except:
            pass

    await update.message.reply_text(str(hits))
