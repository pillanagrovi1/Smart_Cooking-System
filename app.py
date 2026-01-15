import streamlit as st
import json
import time
import os

VIDEO_FILE = "latest.mp4"
STAGES_FILE = "stages.json"

st.set_page_config(page_title="Cooking Playback", layout="centered")
st.title("🍳 Cooking Session Playback")

# -------------------------------
# Load stages
# -------------------------------
if not os.path.exists(STAGES_FILE):
    st.error("stages.json not found. Run the logger first.")
    st.stop()

with open(STAGES_FILE, "r") as f:
    segments = json.load(f)["segments"]

if not segments:
    st.error("No stages found.")
    st.stop()

total_duration = segments[-1]["end"]

# -------------------------------
# Session state
# -------------------------------
if "playing" not in st.session_state:
    st.session_state.playing = False

if "t" not in st.session_state:
    st.session_state.t = 0.0

# -------------------------------
# Controls
# -------------------------------
col1, col2 = st.columns(2)

with col1:
    if st.button("▶ Play"):
        st.session_state.playing = True

with col2:
    if st.button("⏸ Pause"):
        st.session_state.playing = False

# -------------------------------
# Video (Streamlit-native)
# -------------------------------
st.video(VIDEO_FILE)

# -------------------------------
# Playback clock
# -------------------------------
if st.session_state.playing:
    time.sleep(0.5)
    st.session_state.t += 0.5
    if st.session_state.t >= total_duration:
        st.session_state.playing = False
    st.rerun()

# -------------------------------
# Find current segment
# -------------------------------
current = None
for seg in segments:
    if seg["start"] <= st.session_state.t < seg["end"]:
        current = seg
        break

# -------------------------------
# UI display
# -------------------------------
st.markdown("---")

if current:
    remaining = current["end"] - st.session_state.t
    mins = int(remaining // 60)
    secs = int(remaining % 60)

    st.subheader(f"🔥 CURRENT MODE: {current['mode']}")
    st.write(f"⏱ Time remaining: **{mins:02d}:{secs:02d}**")
else:
    st.subheader("Session complete")

# -------------------------------
# Stage summary
# -------------------------------
st.markdown("---")
st.subheader("Stage Summary")

for seg in segments:
    dur = seg["end"] - seg["start"]
    mins = int(dur // 60)
    secs = int(dur % 60)
    st.write(f"{seg['mode']}: {mins:02d}:{secs:02d}")
