"""
Generate ATS Resume matching the EXACT template style from the screenshot:
- Name centered in large dark navy font
- Sub-headline centered in italicized slate/navy
- Contact line centered below
- Section Titles in bold navy with a thin accent colored underline (Hex #9b2c6f / #a21caf magenta/purple line)
- Bullet points with round disc, clean hanging indent
- Exact hierarchical typography:
  - Company in bold
  - Role in bold italic
  - Dates in italic
  - 'Responsibilities:' subhead followed by indented bullet points
  - Projects with project name in bold, followed by detailed bullet points
- No Visionet logo or address
"""
import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT

pdf_path = "public/resume.pdf"
os.makedirs(os.path.dirname(pdf_path), exist_ok=True)

# Clean standard margins
doc = SimpleDocTemplate(
    pdf_path,
    pagesize=letter,
    leftMargin=44,
    rightMargin=44,
    topMargin=40,
    bottomMargin=40
)

styles = getSampleStyleSheet()

# Exact color scheme from the screenshot:
# Main headings / Name: Deep Navy (#1e3a5f / #172554)
# Subhead: Slate Blue (#334155 / #2563eb)
# Section accent underline: Magenta / Berry (#9d2568 / #9333ea / #a21caf)
# Body text: Charcoal (#1f2937)
NAVY_PRIMARY = colors.HexColor('#1b365d')
SUBHEAD_COLOR = colors.HexColor('#334155')
ACCENT_LINE = colors.HexColor('#a21caf')  # The signature magenta/purple rule in the screenshot
TEXT_MAIN = colors.HexColor('#1f2937')
TEXT_MUTED = colors.HexColor('#4b5563')

name_style = ParagraphStyle(
    'CandidateName',
    parent=styles['Normal'],
    fontName='Helvetica-Bold',
    fontSize=22,
    leading=26,
    textColor=NAVY_PRIMARY,
    alignment=TA_CENTER
)

subhead_style = ParagraphStyle(
    'CandidateSubhead',
    parent=styles['Normal'],
    fontName='Helvetica-Oblique',
    fontSize=9.5,
    leading=14,
    textColor=SUBHEAD_COLOR,
    alignment=TA_CENTER,
    spaceBefore=3
)

contact_style = ParagraphStyle(
    'ContactLine',
    parent=styles['Normal'],
    fontName='Helvetica',
    fontSize=8.5,
    leading=13,
    textColor=TEXT_MUTED,
    alignment=TA_CENTER,
    spaceBefore=4,
    spaceAfter=12
)

section_heading_style = ParagraphStyle(
    'SectionHeading',
    parent=styles['Normal'],
    fontName='Helvetica-Bold',
    fontSize=11.5,
    leading=15,
    textColor=NAVY_PRIMARY,
    spaceBefore=10,
    spaceAfter=1
)

company_style = ParagraphStyle(
    'Company',
    parent=styles['Normal'],
    fontName='Helvetica-Bold',
    fontSize=10,
    leading=13.5,
    textColor=TEXT_MAIN,
    spaceBefore=4
)

role_style = ParagraphStyle(
    'Role',
    parent=styles['Normal'],
    fontName='Helvetica-BoldOblique',
    fontSize=9.5,
    leading=13,
    textColor=TEXT_MAIN
)

date_style = ParagraphStyle(
    'DateStyle',
    parent=styles['Normal'],
    fontName='Helvetica-Oblique',
    fontSize=9,
    leading=12.5,
    textColor=TEXT_MUTED,
    spaceAfter=3
)

sub_label_style = ParagraphStyle(
    'SubLabel',
    parent=styles['Normal'],
    fontName='Helvetica-Bold',
    fontSize=9,
    leading=12.5,
    textColor=TEXT_MAIN,
    spaceBefore=3,
    spaceAfter=2
)

project_title_style = ParagraphStyle(
    'ProjectTitle',
    parent=styles['Normal'],
    fontName='Helvetica-Bold',
    fontSize=9.5,
    leading=13.5,
    textColor=TEXT_MAIN,
    spaceBefore=5,
    spaceAfter=2
)

body_style = ParagraphStyle(
    'BodyStyle',
    parent=styles['Normal'],
    fontName='Helvetica',
    fontSize=9,
    leading=13,
    textColor=TEXT_MAIN,
    spaceAfter=3
)

bullet_style = ParagraphStyle(
    'BulletStyle',
    parent=styles['Normal'],
    fontName='Helvetica',
    fontSize=8.5,
    leading=12.5,
    textColor=TEXT_MAIN,
    leftIndent=14,
    firstLineIndent=-9,
    spaceAfter=2.5
)

story = []

def add_section(title):
    story.append(Paragraph(title, section_heading_style))
    story.append(HRFlowable(width="100%", thickness=0.85, color=ACCENT_LINE, spaceBefore=2, spaceAfter=5))

# ─── 1. CENTERED HEADER ───
story.append(Paragraph("Ayesha Siddiqua", name_style))
story.append(Paragraph("Frontend Developer | React &amp; TypeScript | Python | Microsoft Azure &amp; Azure AI Foundry | Power BI", subhead_style))
story.append(Paragraph("Lahore, Pakistan &nbsp;|&nbsp; +92 315 4486062 &nbsp;|&nbsp; a.siddiqua.nadeem@gmail.com &nbsp;|&nbsp; github.com/ayeshanadeem45", contact_style))

# ─── 2. PROFESSIONAL SUMMARY ───
add_section("Professional Summary")
summary_p = (
    "Dedicated <b>Frontend Developer</b> with solid full-stack engineering, cloud deployment, and business intelligence expertise, "
    "specializing in developing responsive web applications and interactive analytics using <b>React, TypeScript, Python, Microsoft Azure</b>, "
    "and <b>Power BI</b>. Experienced delivering 6 complete frontend-and-backend integrated production-grade projects during an internship at "
    "<b>Systems Limited (CADM Department)</b>, deploying frontend solutions to <b>Microsoft Azure</b>, utilizing <b>Azure AI Foundry</b>, "
    "and designing executive Power BI dashboards for business sales performance and HR employee attrition analysis. Recognized for clean code, "
    "intuitive UI/UX design, cloud deployment workflows, and robust API integration."
)
story.append(Paragraph(summary_p, body_style))

# ─── 3. TECHNOLOGIES & SKILLS ───
add_section("Technologies &amp; Skills")
story.append(Paragraph("• <b>Frontend Engineering:</b> React, TypeScript, JavaScript (ES6+), HTML5, CSS3, Tailwind CSS, Shadcn/ui, Material UI, Component Architecture, Responsive Layouts", bullet_style))
story.append(Paragraph("• <b>Cloud &amp; Azure:</b> Microsoft Azure, Azure AI Foundry, Azure App Service, Cloud Frontend Deployment, Azure Static Web Apps", bullet_style))
story.append(Paragraph("• <b>Backend &amp; APIs:</b> Python, RESTful API Development, FastAPI, Flask, Backend Service Integration, JSON Pipelines", bullet_style))
story.append(Paragraph("• <b>Business Intelligence &amp; Data Analytics:</b> Power BI, DAX, Data Modeling, KPI Dashboards, Sales &amp; Attrition Analytics, Data Visualization", bullet_style))
story.append(Paragraph("• <b>AI &amp; Models Integration:</b> Azure AI Foundry, OpenAI API, Decision Models (Decision 1), Conversational UI, Real-Time Model Comparison", bullet_style))
story.append(Paragraph("• <b>Developer Tools &amp; Methodologies:</b> Git, GitHub, VS Code, Vite, npm, Postman, Agile/Scrum Development", bullet_style))
story.append(Paragraph("• <b>Programming Languages:</b> Python, TypeScript, JavaScript, DAX", bullet_style))

# ─── 4. PROFESSIONAL EXPERIENCE ───
add_section("Professional Experience")

# Systems Limited
story.append(Paragraph("Systems Limited", company_style))
story.append(Paragraph("Frontend Developer", role_style))
story.append(Paragraph("Jul 2026 – Oct 2026", date_style))
story.append(Paragraph("Responsibilities:", sub_label_style))
story.append(Paragraph("• Architected, developed, and deployed the complete frontend interfaces for 6 enterprise and client-facing full-stack applications in the CADM Department.", bullet_style))
story.append(Paragraph("• Configured and managed cloud deployments for frontend applications on <b>Microsoft Azure</b> (Azure App Service / Static Web Apps), ensuring high availability and seamless CI/CD delivery.", bullet_style))
story.append(Paragraph("• Leveraged <b>Azure AI Foundry</b> for AI-driven application modules, integrating decision models and intelligent conversational features with responsive React interfaces.", bullet_style))
story.append(Paragraph("• Integrated dynamic React and TypeScript frontend modules with backend Python services and RESTful APIs, ensuring seamless data flow and zero-lag user interaction.", bullet_style))
story.append(Paragraph("• Built robust, reusable design systems utilizing Tailwind CSS, Shadcn/ui, and Material UI, standardizing visual aesthetics across enterprise projects.", bullet_style))
story.append(Paragraph("• Conducted UI testing, optimized rendering performance, and participated in Agile sprint planning and collaborative peer code reviews.", bullet_style))
story.append(Spacer(1, 4))

# LDA
story.append(Paragraph("Lahore Development Authority (LDA)", company_style))
story.append(Paragraph("IT Department Intern", role_style))
story.append(Paragraph("2025", date_style))
story.append(Paragraph("Responsibilities:", sub_label_style))
story.append(Paragraph("• Provided technical assistance to the IT Department, supporting enterprise infrastructure, network troubleshooting, and internal digital systems.", bullet_style))
story.append(Paragraph("• Collaborated with senior teams on data maintenance, system operations, and departmental workflow streamlining.", bullet_style))

# ─── 5. KEY PROJECTS ───
add_section("Key Projects")

# Power BI Sales Dashboard
story.append(Paragraph("Business Sales Performance Dashboard (Power BI)", project_title_style))
story.append(Paragraph("• Designed an interactive executive Power BI dashboard analyzing revenue trends, profit margins, sales growth by region, and product-level performance metrics.", bullet_style))
story.append(Paragraph("• Built complex DAX measures and custom data models to provide actionable insights for sales forecasting, channel distribution, and quarterly variance analysis.", bullet_style))

# Power BI Attrition Dashboard
story.append(Paragraph("Employee Attrition &amp; HR Analytics Dashboard (Power BI)", project_title_style))
story.append(Paragraph("• Developed a comprehensive HR intelligence dashboard to monitor workforce attrition rates, turnover factors, tenure distribution, and department-level retention risks.", bullet_style))
story.append(Paragraph("• Implemented dynamic drill-through filters and demographic breakdowns helping management uncover key drivers of employee turnover.", bullet_style))

# CSuite
story.append(Paragraph("CSuite – Automated Workflow Platform", project_title_style))
story.append(Paragraph("• Built an automated enterprise workflow platform designed to streamline business operations, task approvals, and departmental communication.", bullet_style))
story.append(Paragraph("• Implemented reactive user dashboards in React and TypeScript with real-time status tracking and end-to-end backend API integration.", bullet_style))

# AI Shopping Assistant
story.append(Paragraph("AI Shopping Assistant", project_title_style))
story.append(Paragraph("• Developed a conversational AI assistant that analyzes user shopping preferences and serves real-time product recommendations.", bullet_style))
story.append(Paragraph("• Designed an intuitive chat-first interface featuring dynamic catalog cards and responsive cart synchronization.", bullet_style))

# Decision Models Game
story.append(Paragraph("AI Decision Models Game (OpenAI &amp; Decision 1)", project_title_style))
story.append(Paragraph("• Built a full-stack competitive gaming platform where autonomous AI decision models (OpenAI, Decision 1, and Microsoft decision models) compete instead of humans.", bullet_style))
story.append(Paragraph("• Engineered the backend simulation engine and a real-time results frontend displaying live game state, scoring mechanics, and winner analytics.", bullet_style))

# ZooCode Dashboard
story.append(Paragraph("ZooCode Extension Analytics Dashboard", project_title_style))
story.append(Paragraph("• Engineered an analytics dashboard monitoring developer extension usage metrics, including active installations, token consumption, and session trends.", bullet_style))
story.append(Paragraph("• Created data visualization charts and key summary KPI metrics with responsive UI components.", bullet_style))

# Agentic XP & Converge
story.append(Paragraph("Agentic XP &amp; Converge Platforms", project_title_style))
story.append(Paragraph("• Built responsive frontend interfaces for Agentic XP, enabling interactive visualization of agent workflows and execution logs.", bullet_style))
story.append(Paragraph("• Designed clean, accessible frontend modules for the Converge platform using Material UI and TypeScript.", bullet_style))

# ─── 6. EDUCATION ───
add_section("Education")
story.append(Paragraph("Bachelor of Science in Information Technology (BSIT)", company_style))
story.append(Paragraph("University of Education, Lahore &nbsp;|&nbsp; 7th Semester (Ongoing) &nbsp;|&nbsp; <b>CGPA: 3.72 / 4.00</b>", date_style))
story.append(Spacer(1, 2))

story.append(Paragraph("FSc Pre-Engineering", company_style))
story.append(Paragraph("Punjab Group of Colleges (PGC) &nbsp;|&nbsp; <b>Grade: A+</b>", date_style))
story.append(Spacer(1, 2))

story.append(Paragraph("Certificate in Programming", company_style))
story.append(Paragraph("Punjab University, Lahore &nbsp;|&nbsp; 2023", date_style))

# ─── 7. HOBBIES & INTERESTS ───
add_section("Hobbies &amp; Interests")
story.append(Paragraph("Book Reading, Sketching, Calligraphy, Painting, Language Learning, Poetry, and Gaming.", body_style))

doc.build(story)
print("Exact-template matching ATS resume built successfully at:", pdf_path)
