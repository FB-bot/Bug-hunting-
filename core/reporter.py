from reportlab.platypus import SimpleDocTemplate,Paragraph
from reportlab.lib.styles import getSampleStyleSheet

def make_text(target,data):

    text=f"TARGET: {target}\n\n"

    for d in data:
        text+=d+"\n"

    return text

def make_pdf(text):

    file="reports/report.pdf"

    doc=SimpleDocTemplate(file)
    styles=getSampleStyleSheet()

    story=[Paragraph(text.replace("\n","<br/>"),
    styles["Normal"])]

    doc.build(story)

    return file
