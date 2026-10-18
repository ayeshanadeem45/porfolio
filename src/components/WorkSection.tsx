import './Sections.css'

const projects = [
  {
    name: 'CSuite',
    tag: 'Automation · SaaS',
    desc: 'Automated workflow platform for businesses — streamlines operations with intelligent process automation and team collaboration tools.',
    tech: ['React', 'TypeScript', 'Python', 'REST API'],
  },
  {
    name: 'AI Shopping Assistant',
    tag: 'AI · E-commerce',
    desc: 'Conversational AI shopping assistant that understands user preferences and delivers personalized product recommendations in real time.',
    tech: ['React', 'TypeScript', 'OpenAI', 'Python'],
  },
  {
    name: 'Decision Models Game',
    tag: 'AI · Gaming',
    desc: 'Full-stack competitive game featuring OpenAI, JEV, Decision 1, and Microsoft decision models powered by TypeSafe AI playing autonomously instead of humans. Real-time game state, round simulations, and scoring analytics.',
    tech: ['React', 'TypeScript', 'TypeSafe AI', 'JEV', 'Decision 1', 'OpenAI'],
  },
  {
    name: 'Agentic XP',
    tag: 'Frontend · Agentic AI',
    desc: 'Frontend for an agentic AI experience platform. Built dynamic, responsive interfaces for complex multi-agent workflow visualization.',
    tech: ['React', 'TypeScript', 'Tailwind CSS'],
  },
  {
    name: 'Converge',
    tag: 'Frontend · Platform',
    desc: 'Built the complete frontend for Converge — a modern collaboration and data platform with a clean, responsive UI and seamless backend integration.',
    tech: ['React', 'TypeScript', 'Material UI'],
  },
  {
    name: 'ZooCode Dashboard',
    tag: 'Analytics · Dashboard',
    desc: 'Analytics dashboard tracking VS Code extension usage metrics — active users, token consumption, session data, and trend visualization.',
    tech: ['React', 'TypeScript', 'Recharts', 'Shadcn/ui'],
  },
  {
    name: 'Sales Performance Dashboard',
    tag: 'Business Intelligence · Analytics',
    desc: 'Power BI executive dashboard analyzing revenue growth, regional sales distribution, profit margins, and dynamic product-level sales forecasting.',
    tech: ['Power BI', 'DAX', 'Data Modeling', 'KPI Visuals'],
  },
  {
    name: 'Employee Attrition Dashboard',
    tag: 'HR Analytics · Power BI',
    desc: 'Comprehensive HR intelligence dashboard identifying turnover trends, retention risk factors, departmental attrition rates, and demographic breakdowns.',
    tech: ['Power BI', 'DAX', 'HR Analytics', 'Data Viz'],
  },
]

export default function WorkSection() {
  return (
    <section id="work" className="section section-work">
      <div className="section-inner">
        <div className="section-header">
          <span className="section-eyebrow">Selected Projects</span>
          <h2 className="section-title">Work</h2>
          <p className="section-subtitle">
            Full-stack projects built during my internship at Systems Limited (Jul – Oct 2026)
            and beyond — from AI-powered tools to analytics dashboards.
          </p>
        </div>

        <div className="projects-grid">
          {projects.map((p) => (
            <article key={p.name} className="project-card">
              <div className="project-card-inner">
                <div className="project-top">
                  <span className="project-tag">{p.tag}</span>
                  <span className="project-arrow">↗</span>
                </div>
                <h3 className="project-name">{p.name}</h3>
                <p className="project-desc">{p.desc}</p>
                <div className="project-tech">
                  {p.tech.map((t) => (
                    <span key={t} className="tech-chip">{t}</span>
                  ))}
                </div>
              </div>
            </article>
          ))}
        </div>
      </div>
    </section>
  )
}
