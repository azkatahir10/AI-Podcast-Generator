# 🎙️ AI Podcast Generator (FastAPI Version)

This project generates AI-powered podcast episodes by combining:

- 🎤 **Script Generation** using OpenAI/Grok
- 🗣️ **Text-to-Speech** conversion via Coqui TTS or ElevenLabs
- ⚙️ **FastAPI Backend** for triggering podcast generation
- 📦 Optional **Docker** containerization for deployment

---

## 📁 Project Structure

```

AI-Podcast-Generator-fastapi/
├── main.py                 # FastAPI backend
├── generator.py            # Podcast script & TTS logic
├── audio/                  # Output audio files
├── requirements.txt
├── Dockerfile
└── README.md

````

---

## 🚀 Features

- 🎧 Generate full podcast episodes in minutes
- 🤖 AI-generated content via language models
- 🧠 Choose between Coqui or ElevenLabs for voice output
- ⚡ FastAPI backend with REST endpoint
- 🐳 Optional Docker deployment

---

## 🛠️ Setup (Locally)

### 1. Clone the repository

```bash
git clone https://github.com/azkatahir10/AI-Podcast-Generator.git
cd AI-Podcast-Generator
git checkout docker
````

### 2. Create and activate a virtual environment

```bash
python -m venv venv
venv\Scripts\activate  # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the FastAPI server

```bash
uvicorn main:app --reload
```

Visit: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) to try the API.

---

## 🐳 Docker (Optional)

If Docker is available:

```bash
docker build -t my-podcast-api:v1.0 .
docker run -p 8000:8000 my-podcast-api:v1.0
```

---

## 🎯 API Endpoints

| Method | Endpoint    | Description            |
| ------ | ----------- | ---------------------- |
| POST   | `/generate` | Generate podcast audio |

Test easily via the Swagger UI at `/docs`.

---

## 🧠 AI Models Used

* OpenAI / Grok for content generation
* Coqui or ElevenLabs for realistic voice output

---

## 📂 Output

Generated `.mp3` files are saved in the `audio/` directory.

---

## 📌 Branch Info

You are currently on the **`docker`** branch — this branch includes Docker support and updated deployment features.

---

## 🤝 Contributing

Feel free to fork the repo, make changes, and open a pull request!

---

## 📄 License

MIT License © Azka Tahir

