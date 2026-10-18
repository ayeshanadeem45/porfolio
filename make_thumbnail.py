import cv2
import numpy as np

# Load center character image
center = cv2.imread('public/center.webp')
h, w, _ = center.shape

thumb_w = 1200
thumb_h = 630

# Background base color: #907467 (BGR: [103, 116, 144])
canvas = np.full((thumb_h, thumb_w, 3), [103, 116, 144], dtype=np.uint8)

# Scale character height to fit 630
scale = thumb_h / float(h)
char_w = int(w * scale)
char_h = int(h * scale)
resized_char = cv2.resize(center, (char_w, char_h), interpolation=cv2.INTER_LANCZOS4)

# Align to right
x_start = max(0, thumb_w - char_w + 140)
x_char_crop = 0
paste_w = min(char_w, thumb_w - x_start)

canvas[0:thumb_h, x_start:x_start+paste_w] = resized_char[0:thumb_h, x_char_crop:x_char_crop+paste_w]

# Smooth dark backdrop gradient on left side
gradient = np.zeros((thumb_h, thumb_w), dtype=np.float32)
for x in range(thumb_w):
    if x < 420:
        gradient[:, x] = 0.58
    elif x < 780:
        gradient[:, x] = 0.58 * (1.0 - (x - 420) / 360.0)
    else:
        gradient[:, x] = 0.0

dark_layer = np.full((thumb_h, thumb_w, 3), [38, 44, 56], dtype=np.uint8)
for c in range(3):
    canvas[:, :, c] = (canvas[:, :, c] * (1.0 - gradient) + dark_layer[:, :, c] * gradient).astype(np.uint8)

def put_shadow_text(img, text, pt, font, scale, color, thick=2):
    cv2.putText(img, text, (pt[0]+2, pt[1]+2), font, scale, (0, 0, 0), thick+1, cv2.LINE_AA)
    cv2.putText(img, text, pt, font, scale, color, thick, cv2.LINE_AA)

# 1. Live status badge
overlay = canvas.copy()
cv2.rectangle(overlay, (75, 65), (280, 105), (255, 255, 255), -1)
cv2.addWeighted(overlay, 0.12, canvas, 0.88, 0, canvas)
cv2.rectangle(canvas, (75, 65), (280, 105), (255, 255, 255), 1, cv2.LINE_AA)
cv2.circle(canvas, (95, 85), 5, (74, 222, 128), -1, cv2.LINE_AA)
cv2.putText(canvas, "PORTFOLIO 2026", (112, 91), cv2.FONT_HERSHEY_DUPLEX, 0.55, (255, 255, 255), 1, cv2.LINE_AA)

# 2. Greeting
cv2.putText(canvas, "HI, I'M", (75, 160), cv2.FONT_HERSHEY_DUPLEX, 0.7, (220, 220, 220), 1, cv2.LINE_AA)

# 3. Name: Ayesha Siddiqua
put_shadow_text(canvas, "Ayesha Siddiqua", (70, 235), cv2.FONT_HERSHEY_TRIPLEX, 1.85, (255, 255, 255), 2)

# 4. Role
cv2.putText(canvas, "Frontend Developer | Full Stack & Cloud", (75, 285), cv2.FONT_HERSHEY_DUPLEX, 0.75, (140, 240, 255), 1, cv2.LINE_AA)

# 5. Core Technologies
cv2.putText(canvas, "React  *  TypeScript  *  Python  *  Azure  *  Power BI", (75, 335), cv2.FONT_HERSHEY_DUPLEX, 0.65, (240, 240, 240), 1, cv2.LINE_AA)

# 6. Badges (Systems Limited, BSIT 3.72, 6+ Projects)
badges = ["Systems Limited (CADM)", "BSIT CGPA 3.72", "6+ Projects Shipped"]
bx = 75
by = 385
for b in badges:
    (tw, th), _ = cv2.getTextSize(b, cv2.FONT_HERSHEY_DUPLEX, 0.52, 1)
    overlay = canvas.copy()
    cv2.rectangle(overlay, (bx, by), (bx + tw + 24, by + 36), (255, 255, 255), -1)
    cv2.addWeighted(overlay, 0.15, canvas, 0.85, 0, canvas)
    cv2.rectangle(canvas, (bx, by), (bx + tw + 24, by + 36), (255, 255, 255), 1, cv2.LINE_AA)
    cv2.putText(canvas, b, (bx + 12, by + 24), cv2.FONT_HERSHEY_DUPLEX, 0.52, (255, 255, 255), 1, cv2.LINE_AA)
    bx += tw + 36

# 7. Button CTA
overlay = canvas.copy()
cv2.rectangle(overlay, (75, 465), (460, 525), (255, 255, 255), -1)
cv2.addWeighted(overlay, 0.95, canvas, 0.05, 0, canvas)
cv2.putText(canvas, "Explore Interactive 3D Hero ->", (96, 502), cv2.FONT_HERSHEY_DUPLEX, 0.66, (60, 45, 38), 2, cv2.LINE_AA)

# Save
cv2.imwrite('public/portfolio-thumbnail.jpg', canvas)
cv2.imwrite('public/portfolio-thumbnail.png', canvas)
cv2.imwrite('C:/Users/aish9/OneDrive/Desktop/portfolio-thumbnail.png', canvas)
cv2.imwrite('C:/Users/aish9/OneDrive/Desktop/portfolio-thumbnail.jpg', canvas)
print("Updated clean crisp thumbnail rendered successfully!")
