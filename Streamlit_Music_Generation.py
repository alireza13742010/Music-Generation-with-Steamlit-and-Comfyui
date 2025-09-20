import streamlit as st
import requests
import json
import os
import time

# ComfyUI endpoints
COMFYUI_API_URL = "http://127.0.0.1:8188/prompt"
COMFYUI_HISTORY_URL = "http://127.0.0.1:8188/history"

# Path to ComfyUI's output folder (adjust if different)
COMFYUI_OUTPUT_DIR = r"/media/avidmech/data/ComfyUI/output/audio"

# Load your saved ComfyUI workflow JSON
with open("Ace_step_music_generation.json", "r") as f:
    workflow_nodes = json.load(f)

def generate_audio(lyrics, tags_prompt, cfg_value, sampler_choice):
    # Make a deep copy so we don't overwrite the original
    wf = json.loads(json.dumps(workflow_nodes))
    wf["6"]["inputs"]["lyrics"] = lyrics
    wf["6"]["inputs"]["tags"] = tags_prompt
    # 🔹 Update CFG and sampler in node 4 (KSampler)
    wf["4"]["inputs"]["cfg"] = cfg_value
    wf["4"]["inputs"]["sampler_name"] = sampler_choice

    payload = {"prompt": wf}

    try:
        r = requests.post(COMFYUI_API_URL, json=payload)
        if r.status_code != 200:
            return None, f"Error from ComfyUI: {r.status_code} {r.text}"

        try:
            result = r.json()
        except Exception as e:
            return None, f"Invalid JSON from ComfyUI: {e} | Raw: {r.text}"

        prompt_id = result.get("prompt_id")
        st.write("Prompt ID:", prompt_id)
        if not prompt_id:
            return None, "No prompt_id returned from ComfyUI."

        # Poll for completion
        audio_filename = None
        for _ in range(60):  # wait up to ~60 seconds
            status = requests.get(f"{COMFYUI_HISTORY_URL}/{prompt_id}")
            if status.status_code == 200:
                history = status.json()
                if prompt_id in history:
                    outputs = history[prompt_id]["outputs"]
                    if "10" in outputs:  # Node 10 is SaveAudioMP3
                        # Adjust key if your ComfyUI returns "files" instead of "audio"
                        if "audio" in outputs["10"]:
                            audio_filename = outputs["10"]["audio"][0]["filename"]
                        elif "files" in outputs["10"]:
                            audio_filename = outputs["10"]["files"][0]["filename"]
                        break
            time.sleep(1)

        if not audio_filename:
            return None, "Timed out waiting for audio file."

        # Build full local path
        local_audio_path = os.path.join(COMFYUI_OUTPUT_DIR, audio_filename)

        if not os.path.exists(local_audio_path):
            return None, f"Audio file not found locally: {local_audio_path}"

        return local_audio_path, "Audio generated successfully!"

    except Exception as e:
        return None, f"Error: {e}"


# ---------------- Streamlit UI ----------------
st.set_page_config(page_title="Lyrics & Tags to Audio via ComfyUI", page_icon="🎤")
st.title("🎤 Lyrics & Tags to Audio via ComfyUI (Local Read)")


lyrics_input = st.text_area("Enter lyrics", height=200)
tags_input = st.text_input("Enter style/tags prompt")

cfg_value = st.slider("CFG Scale", min_value=1.0, max_value=20.0, value=4.0, step=0.5)
sampler_choice = st.selectbox(
    "Sampler",
    ["euler", "euler_ancestral", "lms", "heun", "dpm_2", "dpm_2_ancestral", "res_multistep"],
    index=6  # default to res_multistep
)

if st.button("Generate Audio"):
    audio_path, status_msg = generate_audio(lyrics_input, tags_input, cfg_value, sampler_choice)
    st.write(status_msg)
    if audio_path and os.path.exists(audio_path):
        st.audio(audio_path, format="audio/mp3")

