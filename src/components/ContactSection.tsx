import './Sections.css'

export default function ContactSection() {

  return (
    <section id="contact" className="section section-contact">
      <div className="section-inner section-inner-narrow">
        <div className="section-header">
          <span className="section-eyebrow">Get In Touch</span>
          <h2 className="section-title">Let's Talk</h2>
          <p className="section-subtitle">
            Open to full-time roles, freelance projects, and exciting collaborations.
            Drop me a message — I read everything.
          </p>
        </div>

        {/* Contact cards */}
        <div className="contact-cards">
          <a href="mailto:a.siddiqua.nadeem@gmail.com" className="contact-card contact-card-primary">
            <span className="contact-card-icon">
              <svg width="22" height="22" viewBox="0 0 24 24" fill="none">
                <rect x="2" y="4" width="20" height="16" rx="2" stroke="currentColor" strokeWidth="1.5"/>
                <path d="M2 7l10 7 10-7" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round"/>
              </svg>
            </span>
            <div className="contact-card-body">
              <span className="contact-card-label">Email</span>
              <span className="contact-card-value">a.siddiqua.nadeem@gmail.com</span>
            </div>
            <span className="contact-card-action">
              Send Email →
            </span>
          </a>
        </div>

        {/* Bottom strip */}
        <div className="contact-footer">
          <span className="contact-footer-text">
            Based in Lahore, Pakistan · Available for remote & on-site
          </span>
          <a href="mailto:a.siddiqua.nadeem@gmail.com" className="btn-contact-cta">
            Say Hello
            <svg width="14" height="14" viewBox="0 0 16 16" fill="none">
              <path d="M3 8h10M9 4l4 4-4 4" stroke="currentColor" strokeWidth="1.6" strokeLinecap="round" strokeLinejoin="round"/>
            </svg>
          </a>
        </div>

        {/* Footer credit */}
        <p className="site-credit">Designed & built by Ayesha Siddiqua · 2026</p>
      </div>
    </section>
  )
}
