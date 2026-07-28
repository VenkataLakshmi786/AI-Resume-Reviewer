from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet


def generate_report(
    filename,
    job_role,
    ats_result,
    ai_analysis
):

    styles = getSampleStyleSheet()

    doc = SimpleDocTemplate(filename)

    story = []

    story.append(Paragraph("<b>AI Resume Reviewer Report</b>", styles["Title"]))

    story.append(Paragraph(f"<b>Target Role:</b> {job_role}", styles["Normal"]))

    story.append(Paragraph(f"<b>ATS Score:</b> {ats_result['score']}%", styles["Normal"]))

    story.append(Paragraph("<br/>", styles["Normal"]))

    story.append(Paragraph("<b>Skills Found</b>", styles["Heading2"]))

    for skill in ats_result["found"]:
        story.append(Paragraph(f"• {skill}", styles["Normal"]))

    story.append(Paragraph("<br/>", styles["Normal"]))

    story.append(Paragraph("<b>Missing Skills</b>", styles["Heading2"]))

    for skill in ats_result["missing"]:
        story.append(Paragraph(f"• {skill}", styles["Normal"]))

    story.append(Paragraph("<br/>", styles["Normal"]))

    story.append(Paragraph("<b>AI Analysis</b>", styles["Heading2"]))

    story.append(Paragraph(ai_analysis.replace("\n", "<br/>"), styles["Normal"]))

    doc.build(story)