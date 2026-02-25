from core import recon,vulnscan,reporter,database,screenshot

async def start_scan(target,msg):

    await msg.edit_text("Recon...")
    subs=await recon.subdomains(target)

    await msg.edit_text("Scanning...")
    vulns=await vulnscan.run(target,subs)

    await screenshot.take("http://"+target)

    report=reporter.make_text(target,vulns)

    pdf=reporter.make_pdf(report)

    await database.save(target,report)

    return report,pdf
