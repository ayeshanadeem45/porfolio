import './HeroText.css'

export default function HeroText() {
  const scrollTo = (e: React.MouseEvent<HTMLAnchorElement>, id: string) => {
    e.preventDefault()
    document.getElementById(id)?.scrollIntoView({ behavior: 'smooth', block: 'start' })
  }

  return (
    <section className="hero-text" aria-label="Hero introduction">
      {/* Greeting + Name */}
      <div className="hero-greeting">
        <span className="greeting-hi">Hi, I'm</span>
        <h1 className="hero-name">Ayesha Siddiqua</h1>
      </div>

      {/* Bio */}
      <p className="hero-bio">
        A <strong>Full Stack Developer</strong> crafting seamless digital experiences —
        pixel-perfect React interfaces, powerful Python APIs, and everything in between.
      </p>

      {/* Action Buttons */}
      <div className="hero-buttons" role="group">
        <a
          href="#contact"
          className="btn btn-primary"
          onClick={(e) => scrollTo(e, 'contact')}
        >
          <span>Let's Talk</span>
          <svg width="15" height="15" viewBox="0 0 16 16" fill="none" aria-hidden="true">
            <path d="M3 8h10M9 4l4 4-4 4" stroke="currentColor" strokeWidth="1.6" strokeLinecap="round" strokeLinejoin="round"/>
          </svg>
        </a>
        <a
          href="/resume.pdf"
          className="btn btn-secondary"
          download
          target="_blank"
          rel="noopener noreferrer"
        >
          <span>Resume</span>
          <svg width="15" height="15" viewBox="0 0 16 16" fill="none" aria-hidden="true">
            <path d="M8 3v8M4 7l4 4 4-4M3 13h10" stroke="currentColor" strokeWidth="1.6" strokeLinecap="round" strokeLinejoin="round"/>
          </svg>
        </a>
      </div>

      {/* Contact micro-info */}
      <div className="hero-contact-meta">
        <a href="tel:+923154486062" className="meta-link">
          <svg width="11" height="11" viewBox="0 0 12 12" fill="none" aria-hidden="true">
            <path d="M2 2.5a1 1 0 011-1h1.28a.5.5 0 01.48.36l.56 2a.5.5 0 01-.14.5L4 5.5a7 7 0 003.5 3.5l1.14-1.2a.5.5 0 01.5-.14l2 .56a.5.5 0 01.36.48V9.5a1 1 0 01-1 1A8.5 8.5 0 012 2.5z" stroke="currentColor" strokeWidth="1" strokeLinecap="round" strokeLinejoin="round"/>
          </svg>
          03154486062
        </a>
        <span className="meta-dot">·</span>
        <a href="mailto:a.siddiqua.nadeem@gmail.com" className="meta-link">
          <svg width="11" height="11" viewBox="0 0 12 12" fill="none" aria-hidden="true">
            <rect x="1" y="2.5" width="10" height="7" rx="1" stroke="currentColor" strokeWidth="1"/>
            <path d="M1 4l5 3 5-3" stroke="currentColor" strokeWidth="1" strokeLinecap="round"/>
          </svg>
          a.siddiqua.nadeem@gmail.com
        </a>
      </div>
    </section>
  )
}
