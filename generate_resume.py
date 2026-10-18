"""
Generate ATS Resume matching the user's provided structure/template:
- Clean header without any Visionet logo/mention or address on top
- Candidate: Ayesha Siddiqua
- Sub-headline: Frontend Developer | React, TypeScript & Python | Full-Stack Integration
- Professional Summary
- Technologies & Skills (categorized style)
- Professional Experience (Systems Limited, LDA)
- Key Projects (CSuite, AI Shopping Assistant, Decision Models Game, Agentic XP, Converge, ZooCode Dashboard)
- Education (BSIT Univ of Education, FSc PGC, Cert Punjab Univ)
- Hobbies & Interests
"""
import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER

pdf_path = "public/resume.pdf"
os.makedirs(os.path.dirname(pdf_path), exist_ok=True)

# 0.5 inch margins for ATS clarity and content fit
doc = SimpleDocTemplate(
    pdf_path,
    pagesize=letter,
    leftMargin=36,
    rightMargin=36,
    topMargin=36,
    bottomMargin=36
)

styles = getSampleStyleSheet()

PRIMARY = colors.HexColor('#0f172a')    # Deep Slate
SECONDARY = colors.HexColor('#2563eb')  # Professional Blue accent
TEXT_DARK = colors.HexColor('#1e293b')  # Dark charcoal
TEXT_MUTED = colors.HexColor('#475569') # Muted Slate
LINE_COLOR = colors.HexColor('#cbd5e1') # Light slate divider

name_style = ParagraphStyle(
    'CandidateName',
    parent=styles['Normal'],
    fontName='Helvetica-Bold',
    fontSize=18,
    leading=22,
    textColor=PRIMARY
)

subhead_style = ParagraphStyle(
    'CandidateSubhead',
    parent=styles['Normal'],
    fontName='Helvetica-Bold',
    fontSize=10,
    leading=14,
    textColor=SECONDARY,
    spaceBefore=2
)

contact_style = ParagraphStyle(
    'ContactLine',
    parent=styles['Normal'],
    fontName='Helvetica',
    fontSize=8.5,
    leading=12,
    textColor=TEXT_MUTED,
    spaceBefore=3,
    spaceAfter=6
)

section_title_style = ParagraphStyle(
    'SectionTitle',
    parent=styles['Normal'],
    fontName='Helvetica-Bold',
    fontSize=11,
    leading=15,
    textColor=PRIMARY,
    spaceBefore=9,
    spaceAfter=2
)

role_company_style = ParagraphStyle(
    'RoleCompany',
    parent=styles['Normal'],
    fontName='Helvetica-Bold',
    fontSize=9.5,
    leading=13,
    textColor=TEXT_DARK
)

date_style = ParagraphStyle(
    'DateLocation',
    parent=styles['Normal'],
    fontName='Helvetica-Oblique',
    fontSize=8.5,
    leading=12,
    textColor=TEXT_MUTED,
    spaceAfter=2
)

body_style = ParagraphStyle(
    'Body',
    parent=styles['Normal'],
    fontName='Helvetica',
    fontSize=8.5,
    leading=12.5,
    textColor=TEXT_DARK,
    spaceAfter=3
)

bullet_style = ParagraphStyle(
    'Bullet',
    parent=styles['Normal'],
    fontName='Helvetica',
    fontSize=8.5,
    leading=12,
    textColor=TEXT_DARK,
    leftIndent=12,
    firstLineIndent=-8,
    spaceAfter=2
)

story = []

def add_section_header(title):
    story.append(Paragraph(title, section_title_style))
    story.append(HRFlowable(width="100%", thickness=0.8, color=LINE_COLOR, spaceBefore=1, spaceAfter=4))

# ─── 1. HEADER (No logos, clean ATS layout) ───
story.append(Paragraph("Ayesha Siddiqua", name_style))
story.append(Paragraph("Frontend Developer &nbsp;|&nbsp; React, TypeScript &amp; Python &nbsp;|&nbsp; End-to-End Full-Stack Integration", subhead_style))
story.append(Paragraph("Email: a.siddiqua.nadeem@gmail.com &nbsp;|&nbsp; Phone: +92 315 4486062 &nbsp;|&nbsp; Lahore, Pakistan &nbsp;|&nbsp; GitHub: github.com/ayeshanadeem45", contact_style))

# ─── 2. PROFESSIONAL SUMMARY ───
add_section_header("Professional Summary")
summary = (
    "Dedicated <b>Frontend Developer</b> with solid full-stack development experience, specializing in modern web applications "
    "using <b>React, TypeScript, Python</b>, and design systems including <b>Tailwind CSS, Shadcn/ui</b>, and <b>Material UI</b>. "
    "Demonstrated expertise delivering 6 complete frontend-and-backend integrated projects during an internship at <b>Systems Limited (CADM Department)</b>, "
    "ranging from automated enterprise workflow platforms and AI shopping assistants to model decision games and extension analytics dashboards. "
    "Passionate about writing clean, maintainable code, architecting intuitive user experiences, and integrating robust RESTful APIs."
)
story.append(Paragraph(summary, body_style))

# ─── 3. TECHNOLOGIES & SKILLS ───
add_section_header("Technologies &amp; Skills")
story.append(Paragraph("<b>Frontend Engineering:</b> React, TypeScript, JavaScript (ES6+), HTML5, CSS3, Tailwind CSS, Shadcn/ui, Material UI, Component Architecture, Responsive Design, State Management", bullet_style))
story.append(Paragraph("<b>Backend &amp; APIs:</b> Python, RESTful API Development, API Integration, JSON Data Pipelines, Backend Service Integration", bullet_style))
story.append(Paragraph("<b>Tools &amp; Workflow:</b> Git, GitHub, VS Code, npm, Vite, Postman, Agile/Scrum", bullet_style))
story.append(Paragraph("<b>Core Competencies:</b> Full-Stack Web Integration, Decision AI Integration, Analytics Dashboards, Performance Optimization", bullet_style))

# ─── 4. PROFESSIONAL EXPERIENCE ───
add_section_header("Professional Experience")

# Systems Limited
story.append(Paragraph("Systems Limited", role_company_style))
story.append(Paragraph("<b>Frontend Developer</b> &nbsp;|&nbsp; CADM Department", body_style))
story.append(Paragraph("Jul 2026 – Oct 2026 &nbsp;|&nbsp; Lahore, Pakistan", date_style))
story.append(Paragraph("Responsibilities:", ParagraphStyle('SubResp', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=8.5, leading=12, textColor=TEXT_DARK, spaceBefore=2, spaceAfter=2)))
story.append(Paragraph("• Architected and developed user interfaces and integrated full-stack logic for 6 major enterprise and client-facing web applications.", bullet_style))
story.append(Paragraph("• Built dynamic, responsive frontends and connected backend Python and API services ensuring zero-lag state synchronization and consistent data validation.", bullet_style))
story.append(Paragraph("• Standardized reusable UI component libraries utilizing Tailwind CSS, Shadcn/ui, and Material UI across enterprise modules.", bullet_style))
story.append(Paragraph("• Collaborated closely in cross-functional CADM agile sprints, performing peer code reviews and participating in deployment pipelines.", bullet_style))
story.append(Spacer(1, 4))

# LDA
story.append(Paragraph("Lahore Development Authority (LDA)", role_company_style))
story.append(Paragraph("<b>IT Intern</b> &nbsp;|&nbsp; IT Department", body_style))
story.append(Paragraph("2025 (3 Months) &nbsp;|&nbsp; Lahore, Pakistan", date_style))
story.append(Paragraph("Responsibilities:", ParagraphStyle('SubResp2', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=8.5, leading=12, textColor=TEXT_DARK, spaceBefore=2, spaceAfter=2)))
story.append(Paragraph("• Supported IT department infrastructure, digital records maintenance, and enterprise software systems in an active government environment.", bullet_style))
story.append(Paragraph("• Coordinated with department engineers to streamline IT workflows, monitor portal performance, and assist in technical support operations.", bullet_style))

# ─── 5. KEY PROJECTS ───
add_section_header("Key Projects")

# CSuite
story.append(Paragraph("<b>CSuite – Automated Business Workflow Platform</b>", role_company_style))
story.append(Paragraph("• Engineered an automated workflow solution designed for modern business operations, streamlining inter-departmental task routing and execution.", bullet_style))
story.append(Paragraph("• Built an interactive React and TypeScript frontend with full backend API integration, supporting real-time process monitoring and status tracking.", bullet_style))
story.append(Spacer(1, 2))

# AI Shopping Assistant
story.append(Paragraph("<b>AI Shopping Assistant</b>", role_company_style))
story.append(Paragraph("• Developed an intelligent conversational shopping application that analyzes customer preferences and delivers real-time product recommendations.", bullet_style))
story.append(Paragraph("• Implemented fluid chat interfaces with dynamic product cards, cart interactions, and smooth asynchronous API communication.", bullet_style))
story.append(Spacer(1, 2))

# Decision Models Game
story.append(Paragraph("<b>AI Decision Models Game (OpenAI &amp; Decision 1)</b>", role_company_style))
story.append(Paragraph("• Built an innovative full-stack decision game featuring AI models (OpenAI, Decision 1, and Microsoft decision models) competing autonomously in place of human players.", bullet_style))
story.append(Paragraph("• Implemented game state management, round simulation algorithms, score tabulation, and real-time frontend visualization demonstrating which model prevailed.", bullet_style))
story.append(Spacer(1, 2))

# ZooCode Dashboard
story.append(Paragraph("<b>ZooCode Analytics Dashboard</b>", role_company_style))
story.append(Paragraph("• Designed an analytics dashboard monitoring developer VS Code extension adoption, tracking total active users, token consumption rates, and session trends.", bullet_style))
story.append(Paragraph("• Integrated data visualization charts and key KPI metric cards using modern component libraries.", bullet_style))
story.append(Spacer(1, 2))

# Agentic XP & Converge
story.append(Paragraph("<b>Agentic XP &amp; Converge Platforms</b>", role_company_style))
story.append(Paragraph("• Built high-performance frontend interfaces for Agentic XP, allowing visual monitoring of autonomous agent interactions and execution graphs.", bullet_style))
story.append(Paragraph("• Developed responsive module components for Converge with Material UI, ensuring cohesive accessibility and cross-browser responsiveness.", bullet_style))

# ─── 6. EDUCATION ───
add_section_header("Education")
story.append(Paragraph("<b>Bachelor of Science in Information Technology (BSIT)</b>", role_company_style))
story.append(Paragraph("University of Education, Lahore &nbsp;|&nbsp; 7th Semester (Ongoing) &nbsp;|&nbsp; <b>CGPA: 3.72 / 4.00</b>", date_style))
story.append(Spacer(1, 2))

story.append(Paragraph("<b>FSc Pre-Engineering</b>", role_company_style))
story.append(Paragraph("Punjab Group of Colleges (PGC) &nbsp;|&nbsp; <b>Grade: A+</b>", date_style))
story.append(Spacer(1, 2))

story.append(Paragraph("<b>Certificate in Programming</b>", role_company_style))
story.append(Paragraph("Punjab University, Lahore &nbsp;|&nbsp; 2023", date_style))

# ─── 7. HOBBIES & INTERESTS ───
add_section_header("Hobbies &amp; Interests")
story.append(Paragraph("Book Reading, Sketching &amp; Calligraphy, Painting, Language Learning, Poetry, and Gaming.", body_style))

doc.build(story)
print("Template-based ATS resume successfully created at:", pdf_path)
