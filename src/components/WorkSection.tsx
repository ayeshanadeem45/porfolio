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
    desc: 'Full-stack competitive game where OpenAI decision models (Decision 1, Microsoft) play against each other. Live game state, model scoring, and results dashboard.',
    tech: ['React', 'Java', 'OpenAI', 'Decision 1'],
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
