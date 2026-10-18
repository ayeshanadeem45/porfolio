import { useEffect, useRef, useState } from 'react'
import './CustomCursor.css'

export default function CustomCursor() {
  const dotRef = useRef<HTMLDivElement>(null)
  const ringRef = useRef<HTMLDivElement>(null)
  const posRef = useRef({ x: -100, y: -100 })
  const ringPosRef = useRef({ x: -100, y: -100 })
  const isHoveringRef = useRef(false)
  const rafRef = useRef<number>(0)
  const [visible, setVisible] = useState(false)

  useEffect(() => {
    const onMouseMove = (e: MouseEvent) => {
      posRef.current = { x: e.clientX, y: e.clientY }
      if (!visible) setVisible(true)
    }
    const onMouseLeave = () => setVisible(false)
    const onMouseEnter = () => setVisible(true)

    // Detect interactive elements for scale-up
    const onMouseOver = (e: MouseEvent) => {
      const target = e.target as Element
      const isInteractive = target.closest('a, button, [role="button"], nav')
      isHoveringRef.current = !!isInteractive
    }

    document.addEventListener('mousemove', onMouseMove, { passive: true })
    document.addEventListener('mouseleave', onMouseLeave)
    document.addEventListener('mouseenter', onMouseEnter)
    document.addEventListener('mouseover', onMouseOver, { passive: true })

    // RAF loop for silky smooth ring trailing
    const animate = () => {
      rafRef.current = requestAnimationFrame(animate)
      const ring = ringRef.current
      const dot = dotRef.current
      if (!ring || !dot) return

      const target = posRef.current
      const ring_pos = ringPosRef.current

      // Trailing lag for the ring (0.12 = slower follow = luxurious feel)
      ring_pos.x += (target.x - ring_pos.x) * 0.12
      ring_pos.y += (target.y - ring_pos.y) * 0.12

      dot.style.transform = `translate(${target.x}px, ${target.y}px)`
      ring.style.transform = `translate(${ring_pos.x}px, ${ring_pos.y}px) scale(${isHoveringRef.current ? 2.2 : 1})`
    }
    rafRef.current = requestAnimationFrame(animate)

    return () => {
      cancelAnimationFrame(rafRef.current)
      document.removeEventListener('mousemove', onMouseMove)
      document.removeEventListener('mouseleave', onMouseLeave)
      document.removeEventListener('mouseenter', onMouseEnter)
      document.removeEventListener('mouseover', onMouseOver)
    }
  }, [visible])

  return (
    <>
      <div
        ref={dotRef}
        className={`cursor-dot ${visible ? 'cursor-visible' : ''}`}
      />
      <div
        ref={ringRef}
        className={`cursor-ring ${visible ? 'cursor-visible' : ''} ${isHoveringRef.current ? 'cursor-hover' : ''}`}
      />
    </>
  )
}
