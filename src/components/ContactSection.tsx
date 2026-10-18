import { useState } from 'react'
import './Sections.css'

export default function ContactSection() {
  const [copied, setCopied] = useState<string | null>(null)

  const copy = (text: string, label: string) => {
    navigator.clipboard.writeText(text).then(() => {
      setCopied(label)
      setTimeout(() => setCopied(null), 2000)
    })
  }

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
              Send →
            </span>
          </a>

          <button
            className="contact-card"
            onClick={() => copy('03154486062', 'phone')}
          >
            <span className="contact-card-icon">
              <svg width="22" height="22" viewBox="0 0 24 24" fill="none">
                <path d="M4 4a2 2 0 012-2h2.56a1 1 0 01.96.73l1.12 4a1 1 0 01-.29 1L8 9.5A14 14 0 0014.5 16l1.77-2.35a1 1 0 011-.29l4 1.12a1 1 0 01.73.96V18a2 2 0 01-2 2A17 17 0 014 4z" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round"/>
              </svg>
            </span>
            <div className="contact-card-body">
              <span className="contact-card-label">Phone</span>
              <span className="contact-card-value">+92 315 4486062</span>
            </div>
            <span className="contact-card-action">
              {copied === 'phone' ? '✓ Copied' : 'Copy'}
            </span>
          </button>
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
