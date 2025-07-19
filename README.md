# 🎙️ AI Podcast Generator

An automated podcast generator that creates a natural-sounding conversation between a host and a guest on any given topic using **OpenRouter LLM API** and generates speech using **pyttsx3 (offline TTS)**. The resulting audio files are stitched together into a single podcast `.mp3` using **FFmpeg**.
# 🔄 FastAPI Integration Branch

> **Branch**: `fastapi-integration`  
> **Status**: Development  
> **Parent**: `main`

## 🆕 What's Different?
- Added FastAPI backend (`/api` directory)
- Streamlit now calls the API instead of local scripts
- New endpoints for podcast generation

## 🛠️ Setup
```bash
# Install additional dependencies
pip install fastapi uvicorn

# Run both services
uvicorn api.main_api:app --reload & streamlit run app.py
---

## 📌 Features

* 🔮 Generates engaging HOST–GUEST dialogues using OpenRouter.ai (LLM)
* 🔊 Converts script to speech using `pyttsx3` (offline text-to-speech)
* 👥 Distinguishes HOST and GUEST with different voices
* 🎧 Combines all audio lines into a single podcast file using `ffmpeg`
* 💻 Fully offline audio generation – no ElevenLabs or gTTS needed
* 📄 Saves the podcast script for reuse or editing

---

## 📦 Requirements

Install dependencies using:

```bash
pip install -r requirements.txt
```

**Dependencies**:

* `requests`
* `python-dotenv`
* `pyttsx3`
* `ffmpeg` (System-level dependency — see below)

---

## 🛠️ FFmpeg Setup (Windows)

1. Download FFmpeg release build from:
   👉 [https://www.gyan.dev/ffmpeg/builds/](https://www.gyan.dev/ffmpeg/builds/)

2. Extract it (e.g., to `C:\ffmpeg`)

3. Add `C:\ffmpeg\bin` to **System Environment Variables → PATH**

4. Confirm installation:

```bash
ffmpeg -version
```

---

## 🧪 Usage

```bash
python podcast_generator.py --topic "The Rise of AI in Education"
```

Optional arguments:

```bash
--topic / -t                Topic of the podcast (Required)
--output_audio_file / -a    Output podcast file (default: podcast.mp3)
--output_script_file / -s   Script save path (default: podcast_script.txt)
--output_dir                Intermediate audio files directory (default: output)
```

---

## 🧬 Example Output

* `podcast_script.txt` – text version of the generated conversation
* `output/` – intermediate `.wav` files (one per line)
* `podcast.mp3` – final stitched podcast episode

---

## 🔐 Environment Setup

Create a `.env` file in the root directory with the following:

```
OPENROUTER_API_KEY=your_openrouter_api_key_here
```

> Get your free API key from: [https://openrouter.ai/](https://openrouter.ai/)

---

## ✨ Sample Output

```
🧠 Generating script using OpenRouter.ai API...
💾 Saving script to: podcast_script.txt
📄 Parsing script...
🔊 Generating audio using pyttsx3 (offline)...
✅ Saved: output/line_1_host.wav
✅ Saved: output/line_2_guest.wav
...
🎧 Combining audio using FFmpeg...
💾 Combined podcast saved to: podcast.mp3
✅ Podcast generation complete!
```

---

## 🛣️ Roadmap

* [ ] Add emotion and pitch control to voices
* [ ] Integrate OpenVoice for cloning voices
* [ ] Support background music or intro/outro tracks
* [ ] Generate episode artwork based on topic

---

## 🧠 Powered By

* [OpenRouter](https://openrouter.ai/) – for LLM-generated script
* [pyttsx3](https://github.com/nateshmbhat/pyttsx3) – for offline voice synthesis
* [FFmpeg](https://ffmpeg.org/) – for professional audio concatenation

---