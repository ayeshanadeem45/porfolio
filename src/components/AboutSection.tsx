import './Sections.css'

const skills = {
  Frontend: ['React', 'TypeScript', 'JavaScript', 'Tailwind CSS', 'Shadcn/ui', 'Material UI', 'CSS / SCSS'],
  Backend:  ['Python', 'REST APIs', 'FastAPI / Flask', 'SQLite', 'Database Integration'],
  'Cloud & AI': ['Microsoft Azure', 'Azure AI Foundry', 'Azure App Service', 'Cloud Deployment'],
  'BI & Analytics': ['Power BI', 'DAX', 'Data Modeling', 'Interactive Dashboards', 'KPI Analytics'],
  Tools:    ['Git', 'GitHub', 'Figma', 'VS Code', 'Agile / Scrum'],
}

const experience = [
  {
    role: 'Frontend Developer',
    org: 'Systems Limited',
    dept: 'CADM Department',
    period: 'Jul 2026 – Oct 2026 · 4 months',
    desc: 'Built 6 complete full-stack projects: CSuite, AI Shopping Assistant, Decision Models Game, Agentic XP, Converge, and ZooCode Dashboard — with end-to-end frontend & backend integration, Azure frontend deployment, and Azure AI Foundry.',
  },
  {
    role: 'IT Department Intern',
    org: 'LDA (Lahore Development Authority)',
    dept: 'IT Department',
    period: '2025 · 3 months',
    desc: 'Supported IT operations and digital infrastructure in a government enterprise environment.',
  },
]

const education = [
  {
    degree: 'Bachelor of Science in Information Technology (BSIT)',
    inst: 'University of Education',
    period: '7th Semester (Ongoing)',
    detail: 'CGPA: 3.72 / 4.00',
    icon: '🎓',
  },
  {
    degree: 'FSc (Pre-Engineering)',
    inst: 'Punjab Group of Colleges (PGC)',
    period: 'Completed',
    detail: 'Grade: A+',
    icon: '📘',
  },
  {
    degree: 'Certificate in Programming',
    inst: 'Punjab University, Lahore',
    period: '2023',
    detail: 'Foundational programming concepts',
    icon: '📜',
  },
]

const hobbies = ['Book Reading', 'Sketching', 'Calligraphy', 'Painting', 'Language Learning', 'Poetry', 'Gaming']

export default function AboutSection() {
  return (
    <section id="about" className="section section-about">
      <div className="section-inner">
        <div className="section-header">
          <span className="section-eyebrow">Who I Am</span>
          <h2 className="section-title">About</h2>
        </div>

        <div className="about-grid">
          {/* Bio column */}
          <div className="about-bio-col">
            <p className="about-bio-text">
              I'm <strong>Ayesha Siddiqua</strong>, a Full Stack Developer with a love for
              building things that are both beautiful and functional. Currently in my
              7th semester of BSIT at the University of Education with a CGPA of 3.72.
            </p>
            <p className="about-bio-text">
              I enjoy the full journey — from designing pixel-perfect interfaces in React
              to engineering robust Python APIs. I've shipped 6 production-level projects
              at Systems Limited, each a complete frontend-to-backend integration.
            </p>

            {/* Hobbies */}
            <div className="hobbies-row">
              {hobbies.map((h) => (
                <span key={h} className="hobby-chip">{h}</span>
              ))}
            </div>
          </div>

          {/* Skills column */}
          <div className="about-skills-col">
            {Object.entries(skills).map(([cat, items]) => (
              <div key={cat} className="skill-group">
                <span className="skill-group-label">{cat}</span>
                <div className="skill-chips">
                  {items.map((s) => (
                    <span key={s} className="skill-chip">{s}</span>
                  ))}
                </div>
              </div>
            ))}
          </div>
        </div>

        {/* Education */}
        <div className="education-block">
          <h3 className="block-title">Education</h3>
          <div className="education-cards">
            {education.map((e) => (
              <div key={e.degree} className="edu-card">
                <span className="edu-icon">{e.icon}</span>
                <div className="edu-body">
                  <span className="edu-degree">{e.degree}</span>
                  <span className="edu-inst">{e.inst}</span>
                  <div className="edu-meta-row">
                    <span className="edu-period">{e.period}</span>
                    <span className="edu-detail">{e.detail}</span>
                  </div>
                </div>
              </div>
            ))}
          </div>
        </div>

        {/* Experience */}
        <div className="experience-block">
          <h3 className="block-title">Experience</h3>
          <div className="exp-timeline">
            {experience.map((ex) => (
              <div key={ex.org} className="exp-item">
                <div className="exp-dot" />
                <div className="exp-body">
                  <div className="exp-top-row">
                    <span className="exp-role">{ex.role}</span>
                    <span className="exp-period">{ex.period}</span>
                  </div>
                  <span className="exp-org">{ex.org} · {ex.dept}</span>
                  <p className="exp-desc">{ex.desc}</p>
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>
    </section>
  )
}
