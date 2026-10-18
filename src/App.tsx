import { useEffect, useRef, useState } from 'react'
import CustomCursor from './components/CustomCursor'
import NavBar from './components/NavBar'
import HeroText from './components/HeroText'
import WorkSection from './components/WorkSection'
import AboutSection from './components/AboutSection'
import ContactSection from './components/ContactSection'
import './App.css'

const TOTAL_FRAMES = 64
const BG_COLOR = '#907467'

// Build frame URL array
const frameUrls: string[] = []
for (let i = 0; i < TOTAL_FRAMES; i++) {
  frameUrls.push(`/frames/frame_${String(i).padStart(3, '0')}.webp`)
}
const centerUrl = '/center.webp'

/** Lerp between two angles along the shortest arc (both in radians). */
function lerpAngle(a: number, b: number, t: number): number {
  let diff = b - a
  while (diff > Math.PI) diff -= 2 * Math.PI
  while (diff < -Math.PI) diff += 2 * Math.PI
  return a + diff * t
}

/** Wrap angle to [0, 2π) */
function wrapAngle(a: number): number {
  let r = a % (2 * Math.PI)
  if (r < 0) r += 2 * Math.PI
  return r
}

export default function App() {
  const canvasRef = useRef<HTMLCanvasElement>(null)
  const mouseRef = useRef<{ x: number; y: number } | null>(null)
  const hasInteractedRef = useRef(false)
  const smoothAngleRef = useRef(0)
  const rafRef = useRef<number>(0)
  const framesRef = useRef<HTMLImageElement[]>([])
  const centerImgRef = useRef<HTMLImageElement | null>(null)
  const allLoadedRef = useRef(false)
  const [isLoaded, setIsLoaded] = useState(false)

  // ─── Preload all frames ───────────────────────────────────────────────────
  useEffect(() => {
    const total = TOTAL_FRAMES + 1
    let loaded = 0
    const onLoad = () => {
      loaded++
      if (loaded >= total) {
        allLoadedRef.current = true
        setIsLoaded(true)
      }
    }
    frameUrls.forEach((url, i) => {
      const img = new Image()
      img.onload = onLoad
      img.onerror = onLoad
      img.src = url
      framesRef.current[i] = img
    })
    const centerImg = new Image()
    centerImg.onload = onLoad
    centerImg.onerror = onLoad
    centerImg.src = centerUrl
    centerImgRef.current = centerImg
  }, [])

  // ─── Pointer & Touch tracking (Desktop & Mobile) ───────────────────────────
  useEffect(() => {
    const onPointerMove = (e: MouseEvent | TouchEvent) => {
      hasInteractedRef.current = true
      if ('touches' in e && e.touches.length > 0) {
        mouseRef.current = { x: e.touches[0].clientX, y: e.touches[0].clientY }
      } else if ('clientX' in e) {
        mouseRef.current = { x: (e as MouseEvent).clientX, y: (e as MouseEvent).clientY }
      }
    }

    window.addEventListener('mousemove', onPointerMove, { passive: true })
    window.addEventListener('touchmove', onPointerMove, { passive: true })
    window.addEventListener('touchstart', onPointerMove, { passive: true })

    return () => {
      window.removeEventListener('mousemove', onPointerMove)
      window.removeEventListener('touchmove', onPointerMove)
      window.removeEventListener('touchstart', onPointerMove)
    }
  }, [])

  // ─── Canvas draw loop ─────────────────────────────────────────────────────
  useEffect(() => {
    const canvas = canvasRef.current
    if (!canvas) return
    const ctx = canvas.getContext('2d', { alpha: false })
    if (!ctx) return

    const resize = () => {
      canvas.width = window.innerWidth
      canvas.height = window.innerHeight
    }
    resize()
    window.addEventListener('resize', resize)
    window.addEventListener('orientationchange', resize)

    // Adapt face coordinates based on device aspect ratio / width
    const getFaceCenter = () => {
      const isMobile = canvas.width < 768
      return {
        x: isMobile ? canvas.width * 0.50 : canvas.width * 0.62,
        y: isMobile ? canvas.height * 0.32 : canvas.height * 0.40,
      }
    }

    const getDeadzone = () => Math.min(canvas.width, canvas.height) * 0.12
    const LERP_FACTOR = 0.26
    let lastTime = 0

    const draw = (time: number) => {
      rafRef.current = requestAnimationFrame(draw)
      const dt = time - lastTime
      if (dt < 8) return
      lastTime = time

      if (!allLoadedRef.current) {
        ctx.fillStyle = BG_COLOR
        ctx.fillRect(0, 0, canvas.width, canvas.height)
        return
      }

      const face = getFaceCenter()
      let imgToDraw: HTMLImageElement | null = null

      if (!hasInteractedRef.current || !mouseRef.current) {
        // Initial state: look directly straight at user
        imgToDraw = centerImgRef.current
      } else {
        const mouse = mouseRef.current
        const dx = mouse.x - face.x
        const dy = mouse.y - face.y
        const dist = Math.sqrt(dx * dx + dy * dy)
        const deadzone = getDeadzone()
        const rawTargetAngle = Math.atan2(dy, dx)
        const newSmooth = lerpAngle(wrapAngle(smoothAngleRef.current), wrapAngle(rawTargetAngle), LERP_FACTOR)
        smoothAngleRef.current = newSmooth

        if (dist < deadzone) {
          imgToDraw = centerImgRef.current
        } else {
          // Invert the angular mapping so horizontal cursor movement matches head rotation direction:
          // Moving cursor right -> character turns and looks right
          // Moving cursor left -> character turns and looks left
          const normalized = (2 * Math.PI - wrapAngle(newSmooth)) / (2 * Math.PI)
          const frameIdx = Math.round(normalized * TOTAL_FRAMES) % TOTAL_FRAMES
          imgToDraw = framesRef.current[frameIdx]
        }
      }

      if (!imgToDraw || !imgToDraw.complete || imgToDraw.naturalWidth === 0) return

      ctx.fillStyle = BG_COLOR
      ctx.fillRect(0, 0, canvas.width, canvas.height)

      const imgW = imgToDraw.naturalWidth
      const imgH = imgToDraw.naturalHeight
      const isMobile = canvas.width < 768

      // On mobile portrait, scale slightly higher and align so head remains fully centered and visible
      const scale = Math.max(canvas.width / imgW, canvas.height / imgH) * (isMobile ? 1.05 : 1)
      const drawW = imgW * scale
      const drawH = imgH * scale
      
      // On mobile center horizontally and position head nicely in top-half
      const offsetX = isMobile 
        ? (canvas.width - drawW) / 2 - (drawW * 0.08) 
        : (canvas.width - drawW) / 2
      const offsetY = isMobile
        ? Math.min(0, canvas.height * 0.05)
        : (canvas.height - drawH) / 2

      ctx.globalAlpha = 1
      ctx.globalCompositeOperation = 'source-over'
      ctx.drawImage(imgToDraw, offsetX, offsetY, drawW, drawH)
    }

    rafRef.current = requestAnimationFrame(draw)
    return () => {
      cancelAnimationFrame(rafRef.current)
      window.removeEventListener('resize', resize)
      window.removeEventListener('orientationchange', resize)
    }
  }, [])

  return (
    <>
      {/* Custom magnetic cursor — fixed, desktop only */}
      <CustomCursor />

      {/* Fixed nav — always visible while scrolling */}
      <NavBar />

      {/* ─── HERO SECTION ─────────────────────────────────── */}
      <section id="home" className="hero-section">
        {/* Full-screen canvas */}
        <canvas ref={canvasRef} className="hero-canvas" aria-hidden="true" />

        {/* Loading overlay */}
        {!isLoaded && (
          <div className="loading-overlay">
            <div className="loading-bar"><div className="loading-progress" /></div>
          </div>
        )}

        {/* Hero text */}
        <div className={`hero-ui ${isLoaded ? 'hero-ui-visible' : ''}`}>
          <HeroText />
        </div>

        {/* Scroll hint */}
        {isLoaded && (
          <a href="#work" className="scroll-hint" aria-label="Scroll to work section">
            <span className="scroll-hint-line" />
            <span className="scroll-hint-label">scroll</span>
          </a>
        )}
      </section>

      {/* ─── BELOW-FOLD SECTIONS ──────────────────────────── */}
      <main>
        <WorkSection />
        <AboutSection />
        <ContactSection />
      </main>
    </>
  )
}
