# Music-Generation-with-Steamlit-and-Comfyui
This Streamlit app lets you enter lyrics, style tags, CFG scale, and sampler settings, sends them to a ComfyUI workflow to generate music, and then displays the resulting audio in a styled interface with a custom background and output box.


# 🖼️ ComfyUI + Gradio Image Editing Interface

This repository provides a streamlined integration between ComfyUI and Streamlit to create an elegant web-based interface for AI‑powered music and audio generation.
The included Python script wraps a ComfyUI audio workflow in a modern, user‑friendly Streamlit front‑end, enabling you to enter custom lyrics, style/tags, adjust CFG scale, choose a sampler, and generate high‑quality audio directly from your browser. The app also features a custom background, styled input boxes, and a dedicated output section for the generated track.

---

Loads and configures your saved ComfyUI audio generation workflow JSON.

Dynamically updates:

Lyrics input

Tags / Style prompt

CFG scale (guidance strength)

Sampler selection
## ✨ Features

- **ComfyUI Workflow Integration**:
  - Loads and configures the following:
    - ****Model**:**Ace Step
- **Web UI Powered by Streamlit**:
  - background can be chnaged and customized.
  - Sliders for **Sampler** and **CFG scale**.
- **Automatic Output Detection**: Returns the newest generated audio after processing.

---
## Application
<p align="center">
  <img width="687" height="874" alt="Music_generation_aplication_ui" src="https://github.com/user-attachments/assets/d8eb6fcc-4546-4291-8e6f-4452368a3523" />
</p>

# Generated Audio
├── rock, hip - hop, orchestral, bass, drums, electric guitar, piano, synthesizer, violin, viola, cello, fast, energetic, motivational, inspirational, empowering


[ComfyUI_00001_.mp3](https://github.com/user-attachments/files/22440391/ComfyUI_00001_.mp3)

├── Cuban music, salsa, son, Afro-Cuban, traditional Cuban


[ComfyUI_00003_.mp3](https://github.com/user-attachments/files/22440403/ComfyUI_00003_.mp3)



## 🚀 Getting Started
### 1️⃣ Prerequisites
- Python 3.9+
- [ComfyUI](https://github.com/comfyanonymous/ComfyUI) installed and configured
- `pip install gradio pillow numpy pandas` 
-  Ensure you have the following models in your ComfyUI models/ folder:
-  ACE-Step






