"""
Generate an ATS-Friendly Clean PDF Resume for Ayesha Siddiqua
"""
import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT

pdf_path = "public/resume.pdf"
os.makedirs(os.path.dirname(pdf_path), exist_ok=True)

doc = SimpleDocTemplate(
    pdf_path,
    pagesize=letter,
    rightMargin=40,
    leftMargin=40,
    topMargin=36,
    bottomMargin=36
)

styles = getSampleStyleSheet()

# ATS Styles - simple, clean typography without multi-column parsing traps
name_style = ParagraphStyle(
    'Name',
    parent=styles['Normal'],
    fontName='Helvetica-Bold',
    fontSize=20,
    leading=24,
    textColor=colors.HexColor('#1a1a1a'),
    alignment=TA_CENTER
)

contact_style = ParagraphStyle(
    'Contact',
    parent=styles['Normal'],
    fontName='Helvetica',
    fontSize=9.5,
    leading=14,
    textColor=colors.HexColor('#444444'),
    alignment=TA_CENTER
)

section_heading = ParagraphStyle(
    'SectionHeading',
    parent=styles['Normal'],
    fontName='Helvetica-Bold',
    fontSize=11,
    leading=15,
    textColor=colors.HexColor('#2b2b2b'),
    spaceBefore=8,
    spaceAfter=3
)

job_title_style = ParagraphStyle(
    'JobTitle',
    parent=styles['Normal'],
    fontName='Helvetica-Bold',
    fontSize=10,
    leading=14,
    textColor=colors.HexColor('#1f1f1f')
)

job_meta_style = ParagraphStyle(
    'JobMeta',
    parent=styles['Normal'],
    fontName='Helvetica-Oblique',
    fontSize=9,
    leading=13,
    textColor=colors.HexColor('#555555')
)

bullet_style = ParagraphStyle(
    'Bullet',
    parent=styles['Normal'],
    fontName='Helvetica',
    fontSize=9,
    leading=13,
    textColor=colors.HexColor('#333333'),
    leftIndent=14,
    firstLineIndent=-10,
    spaceAfter=2
)

body_style = ParagraphStyle(
    'Body',
    parent=styles['Normal'],
    fontName='Helvetica',
    fontSize=9,
    leading=13,
    textColor=colors.HexColor('#333333')
)

story = []

def add_section(title):
    story.append(Paragraph(title.upper(), section_heading))
    story.append(HRFlowable(width="100%", thickness=0.75, color=colors.HexColor('#888888'), spaceBefore=1, spaceAfter=5))

# Header
story.append(Paragraph("<b>AYESHA SIDDIQUA</b>", name_style))
story.append(Spacer(1, 4))
contact_line = "Lahore, Pakistan &nbsp;|&nbsp; +92 315 4486062 &nbsp;|&nbsp; a.siddiqua.nadeem@gmail.com &nbsp;|&nbsp; github.com/ayeshanadeem45"
story.append(Paragraph(contact_line, contact_style))
story.append(Spacer(1, 10))

# Summary
add_section("Professional Summary")
summary_text = (
    "Results-driven <b>Frontend & Full Stack Developer</b> with hands-on experience building scalable, responsive web "
    "applications using <b>React, TypeScript, Tailwind CSS, Python, and REST APIs</b>. Proven track record of developing "
    "end-to-end applications across AI systems, analytics dashboards, and business automation workflows during internships "
    "at Systems Limited and LDA. Strong foundation in software engineering and modern UI/UX architecture."
)
story.append(Paragraph(summary_text, body_style))
story.append(Spacer(1, 6))

# Technical Skills
add_section("Technical Skills")
story.append(Paragraph("<b>Frontend:</b> React.js, TypeScript, JavaScript (ES6+), HTML5, CSS3, Tailwind CSS, Shadcn/ui, Material UI, Responsive Design", bullet_style))
story.append(Paragraph("<b>Backend & APIs:</b> Python, RESTful API Development, FastAPI, Flask, Backend Integration", bullet_style))
story.append(Paragraph("<b>Developer Tools & Methodologies:</b> Git, GitHub, VS Code, Postman, Agile/Scrum, Vite", bullet_style))
story.append(Spacer(1, 6))

# Experience
add_section("Work Experience")

# Systems Limited
story.append(Paragraph("<b>Frontend Developer</b> &nbsp;|&nbsp; Systems Limited (CADM Department)", job_title_style))
story.append(Paragraph("July 2026 – October 2026 &nbsp;|&nbsp; Lahore, Pakistan", job_meta_style))
story.append(Paragraph("• Developed and integrated 6 full-stack production-grade projects featuring dynamic UI components and robust backend connectivity.", bullet_style))
story.append(Paragraph("• Built <b>CSuite</b>, an automated enterprise workflow solution improving business process efficiency.", bullet_style))
story.append(Paragraph("• Implemented conversational interfaces and real-time recommendation engines for an <b>AI Shopping Assistant</b>.", bullet_style))
story.append(Paragraph("• Created the <b>Decision Models Game</b> showcasing decision AI model scoring (OpenAI & Decision 1) vs interactive UI.", bullet_style))
story.append(Paragraph("• Engineered frontend architecture for <b>Agentic XP</b> and <b>Converge</b> platform using React, TypeScript, and Material UI.", bullet_style))
story.append(Paragraph("• Designed and deployed <b>ZooCode Dashboard</b>, tracking developer extension telemetry, user engagement, and token utilization.", bullet_style))
story.append(Spacer(1, 5))

# LDA
story.append(Paragraph("<b>IT Intern</b> &nbsp;|&nbsp; Lahore Development Authority (LDA)", job_title_style))
story.append(Paragraph("2025 &nbsp;|&nbsp; Lahore, Pakistan", job_meta_style))
story.append(Paragraph("• Assisted the IT Department in government digital infrastructure support and software systems operations.", bullet_style))
story.append(Paragraph("• Collaborated with senior teams on internal tech troubleshooting, data management, and operational workflows.", bullet_style))
story.append(Spacer(1, 6))

# Education
add_section("Education")
story.append(Paragraph("<b>Bachelor of Science in Information Technology (BSIT)</b>", job_title_style))
story.append(Paragraph("University of Education, Lahore &nbsp;|&nbsp; 7th Semester (Ongoing) &nbsp;|&nbsp; <b>CGPA: 3.72 / 4.00</b>", job_meta_style))
story.append(Spacer(1, 4))

story.append(Paragraph("<b>FSc Pre-Engineering</b>", job_title_style))
story.append(Paragraph("Punjab Group of Colleges (PGC) &nbsp;|&nbsp; <b>Grade: A+</b>", job_meta_style))
story.append(Spacer(1, 4))

story.append(Paragraph("<b>Certificate in Programming</b>", job_title_style))
story.append(Paragraph("Punjab University, Lahore &nbsp;|&nbsp; 2023", job_meta_style))
story.append(Spacer(1, 6))

# Interests
add_section("Interests & Hobbies")
story.append(Paragraph("Language Learning, Sketching & Calligraphy, Painting, Book Reading, Poetry, and Competitive Gaming.", body_style))

doc.build(story)
print(f"ATS Resume successfully generated at: {pdf_path}")
