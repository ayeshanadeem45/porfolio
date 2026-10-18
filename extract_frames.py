"""
Step 2: Extract 64 frames for 360° head rotation + center.webp
Video: 240 frames @ 24fps = 10s
- The video shows 8 directional poses (clockwise/counter-clockwise) + neutral
- We need to map the 240 frames across 8 directions + center
- Typical layout: ~8 frames each direction + transitions = 30 frames per quadrant
- We'll extract 64 evenly-spaced frames from the rotational portion
  and the last segment as center/neutral

Strategy:
- Inspect first ~220 frames as the rotation loop
- Last ~20 frames (frame 220-239) as the CENTER neutral pose
- Extract 64 frames evenly from frames 0..219 for the 360° rotation
- Save center.webp from frame 229 (middle of neutral section)
"""
import cv2
import numpy as np
import os

VIDEO_PATH = "public/character.mp4"
OUTPUT_DIR = "public/frames"

os.makedirs(OUTPUT_DIR, exist_ok=True)

cap = cv2.VideoCapture(VIDEO_PATH)
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
fps = cap.get(cv2.CAP_PROP_FPS)

print(f"Total frames: {total_frames}, FPS: {fps}")

# ---- PHASE 1: Extract 64 rotation frames ----
# The video does a head rotation across ~8 directional poses
# Looking at 240 frames total: likely the first 216 frames (9 segments * 24 frames)
# are directional poses and last 24 frames are center neutral

# Let's map 64 frames uniformly from frame 0 to frame ~215
# (the rotational portion, before the neutral section)
# We'll determine cut point by visually inspecting - use frame ~216 as the transition

ROTATION_END = 215   # last frame of the rotation sequence
NEUTRAL_FRAME = 229  # middle of neutral section (frames ~216-239)

# 64 frames evenly spread across frames 0..ROTATION_END
num_frames = 64
frame_indices = [round(i * ROTATION_END / (num_frames - 1)) for i in range(num_frames)]

print(f"Extracting {num_frames} rotation frames...")
print(f"Frame indices: {frame_indices[:5]}...{frame_indices[-5:]}")

WEBP_QUALITY = 92
encode_params = [cv2.IMWRITE_WEBP_QUALITY, WEBP_QUALITY]

for i, frame_idx in enumerate(frame_indices):
    cap.set(cv2.CAP_PROP_POS_FRAMES, frame_idx)
    ret, frame = cap.read()
    if not ret:
        print(f"  WARN: Could not read frame {frame_idx}")
        continue
    out_path = os.path.join(OUTPUT_DIR, f"frame_{i:03d}.webp")
    cv2.imwrite(out_path, frame, encode_params)
    if i % 8 == 0:
        print(f"  Saved frame_{i:03d}.webp (video frame {frame_idx})")

# ---- PHASE 2: Extract center/neutral frame ----
cap.set(cv2.CAP_PROP_POS_FRAMES, NEUTRAL_FRAME)
ret, center_frame = cap.read()
if ret:
    center_path = "public/center.webp"
    cv2.imwrite(center_path, center_frame, encode_params)
    print(f"\nSaved center.webp from video frame {NEUTRAL_FRAME}")
else:
    print("WARN: Could not extract center frame")

cap.release()
print(f"\nDone! Extracted {num_frames} rotation frames + center.webp")
print(f"Output directory: {OUTPUT_DIR}/")
print(f"\nBackground color detected: #907467")
print("Use this color for page background and canvas background.")
