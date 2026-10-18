import { useEffect, useState } from 'react'
import './NavBar.css'

const navItems = [
  { label: 'WORK',    href: '#work'    },
  { label: 'ABOUT',   href: '#about'   },
  { label: 'CONTACT', href: '#contact' },
]

export default function NavBar() {
  const [scrolled, setScrolled] = useState(false)

  useEffect(() => {
    const onScroll = () => setScrolled(window.scrollY > 60)
    window.addEventListener('scroll', onScroll, { passive: true })
    return () => window.removeEventListener('scroll', onScroll)
  }, [])

  const handleNav = (e: React.MouseEvent<HTMLAnchorElement>, href: string) => {
    e.preventDefault()
    const target = document.querySelector(href)
    if (target) {
      target.scrollIntoView({ behavior: 'smooth', block: 'start' })
    }
  }

  return (
    <nav className={`navbar ${scrolled ? 'navbar-scrolled' : ''}`} role="navigation" aria-label="Main navigation">
      <div className="navbar-pill">
        {navItems.map((item, i) => (
          <span key={item.label} className="nav-item-wrap">
            <a
              href={item.href}
              className="nav-item"
              onClick={(e) => handleNav(e, item.href)}
            >
              <span className="nav-bracket">[</span>
              {item.label}
              <span className="nav-bracket">]</span>
            </a>
            {i < navItems.length - 1 && <span className="nav-sep" />}
          </span>
        ))}
      </div>
    </nav>
  )
}
