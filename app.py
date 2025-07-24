import streamlit as st
import requests
from pathlib import Path

# UI settings
st.set_page_config(page_title="AI Podcast Generator", layout="centered")
st.title("🎙️ AI Podcast Generator (API Version)")
st.markdown("""
This app uses a FastAPI backend to generate podcasts with AI.
- Generates scripts using OpenRouter
- Converts text to speech using pyttsx3
- Returns the final podcast as an MP3
""")

# Input fields
topic = st.text_input("📌 Enter Podcast Topic", value="The Rise of AI in Education")
audio_name = st.text_input("🎧 Output Audio Filename", value="podcast.mp3")
api_url = st.text_input("🌐 FastAPI Backend URL", value="http://127.0.0.1:8000")

if st.button("🚀 Generate Podcast"):
    with st.spinner("Generating podcast. Please wait..."):
        try:
            # Call FastAPI backend
            response = requests.post(
                f"{api_url}/generate_podcast",
                json={
                    "topic": topic,
                    "output_audio_file": audio_name,
                }
            )
            response.raise_for_status()  # Raise error for bad status codes
            result = response.json()

            st.success("✅ Podcast generation complete!")
            
            # Display script
            script_file = result.get("script_file", "podcast_script.txt")
            if Path(script_file).exists():
                st.subheader("📜 Script")
                with open(script_file, "r", encoding="utf-8") as f:
                    st.text(f.read())

            # Play and download audio
            audio_file = result.get("audio_file", audio_name)
            if Path(audio_file).exists():
                st.subheader("🔊 Preview Podcast")
                with open(audio_file, "rb") as f:
                    st.audio(f.read(), format="audio/mp3")
                    st.download_button(
                        "⬇️ Download Podcast",
                        data=f.read(),
                        file_name=audio_file,
                        mime="audio/mp3"
                    )

        except requests.exceptions.RequestException as e:
            st.error(f"❌ API Error: {str(e)}")
        except Exception as e:
            st.error(f"❌ Error: {str(e)}")