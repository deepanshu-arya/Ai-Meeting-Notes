from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

def create_pdf(filename, summary, action_points):
    pdf_path = f"{filename}.pdf"
    doc = SimpleDocTemplate(pdf_path)

    styles = getSampleStyleSheet()

    content = []
    content.append(Paragraph("<b>Summary</b>", styles['Heading2']))
    content.append(Paragraph(summary, styles['BodyText']))

    content.append(Paragraph("<b>Action Points</b>", styles['Heading2']))
    content.append(Paragraph(action_points, styles['BodyText']))

    doc.build(content)

    return pdf_path