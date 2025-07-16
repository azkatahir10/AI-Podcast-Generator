import streamlit as st
import os
import shutil
from podcast_generator import main as generate_podcast_script

# UI settings
st.set_page_config(page_title="AI Podcast Generator", layout="centered")
st.title("🎙️ AI Podcast Generator")
st.markdown("""
Generate a podcast with AI-generated dialogue and offline voice cloning (pyttsx3).

- Uses OpenRouter API to generate a script
- Converts lines to audio (Host & Guest)
- Combines them into a final .mp3
""")

# Input
topic = st.text_input("📌 Enter Podcast Topic", value="The Rise of AI in Education")
audio_name = st.text_input("🎧 Output Audio Filename (optional)", value="podcast.mp3")

if st.button("🚀 Generate Podcast"):
    with st.spinner("Generating podcast. Please wait..."):
        # Clean previous output
        if os.path.exists("output"):
            shutil.rmtree("output")

        command = f'python podcast_generator.py --topic "{topic}" --output_audio_file "{audio_name}"'
        result = os.system(command)

    if result != 0:
        st.error("❌ Podcast generation failed. Check console for error details.")
    else:
        st.success("✅ Podcast generation complete!")

        # Display script
        if os.path.exists("podcast_script.txt"):
            st.subheader("📜 Script")
            with open("podcast_script.txt", "r", encoding="utf-8") as f:
                st.text(f.read())

        # Play and offer download
        if os.path.exists(audio_name):
            st.subheader("🔊 Preview Podcast")
            with open(audio_name, "rb") as audio_file:
                st.audio(audio_file.read(), format="audio/mp3")
                st.download_button("⬇️ Download Podcast", audio_file, file_name=audio_name)
