import argparse
import os
import time
import requests
from dotenv import load_dotenv
import pyttsx3
import subprocess

# Load environment variables
load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
if not OPENROUTER_API_KEY:
    raise ValueError("Missing OPENROUTER_API_KEY in .env")

MODEL_NAME = "mistralai/mistral-7b-instruct"

def generate_script(topic):
    print("🧠 Generating script using OpenRouter.ai API...")
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "HTTP-Referer": "localhost",
        "X-Title": "AI Podcast Generator"
    }
    prompt = f"""
You are a podcast script writer.
Create a compelling, conversational podcast script on the topic: \"{topic}\".

Rules:
- Only use lines starting with HOST: or GUEST:
- Use natural dialogue between the host and guest
- Start with HOST: and alternate between HOST and GUEST
- At least 10 turns each from HOST and GUEST (minimum 20 lines total)
- Format ONLY like:
HOST: Welcome!
GUEST: Thanks for inviting me!
... and so on

No extra commentary. No narration. Only the script.
"""

    data = {
        "model": MODEL_NAME,
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data)
    if response.status_code != 200:
        raise RuntimeError(f"OpenRouter API Error: {response.text}")

    return response.json()['choices'][0]['message']['content']

def parse_script(script):
    print("📄 Parsing script...")
    lines = script.strip().splitlines()
    parsed = []
    for line in lines:
        if line.strip().startswith("HOST:"):
            parsed.append(("host", line.split("HOST:")[1].strip()))
        elif line.strip().startswith("GUEST:"):
            parsed.append(("guest", line.split("GUEST:")[1].strip()))
    if len(parsed) < 6:
        raise ValueError(f"Script parsing failed: Expected at least 6 lines, but got {len(parsed)}.\nScript received:\n{script}")
    return parsed

def generate_audio_pyttsx3(parsed_script, output_dir):
    print("🔊 Generating audio using pyttsx3 (offline)...")
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')

    host_voice = voices[0].id
    guest_voice = voices[1].id if len(voices) > 1 else voices[0].id

    audio_files = []
    for i, (speaker, text) in enumerate(parsed_script):
        filename = os.path.join(output_dir, f"line_{i+1}_{speaker}.wav")
        engine.setProperty('voice', host_voice if speaker == "host" else guest_voice)
        engine.save_to_file(text, filename)
        audio_files.append(filename)
        print(f"✅ Saved: {filename}")

    engine.runAndWait()
    return audio_files

def combine_audio_files(audio_files, output_audio_file):
    print("🎧 Combining audio using FFmpeg...")
    list_file = "temp_files.txt"
    with open(list_file, "w", encoding="utf-8") as f:
        for file in audio_files:
            f.write(f"file '{os.path.abspath(file)}'\n")

    cmd = f'ffmpeg -y -f concat -safe 0 -i "{list_file}" -vn -ar 44100 -ac 2 -b:a 192k "{output_audio_file}"'
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)

    if result.returncode != 0:
        print("❌ FFmpeg failed to combine audio.")
        print(result.stderr)
    else:
        print(f"💾 Combined podcast saved to: {output_audio_file}")

    os.remove(list_file)

def save_script(script, output_script_file):
    print(f"💾 Saving script to: {output_script_file}")
    try:
        with open(output_script_file, "w", encoding="utf-8") as f:
            f.write(script)
    except Exception as e:
        raise IOError(f"Failed to save script: {str(e)}")

def main():
    parser = argparse.ArgumentParser(description="🎙️ AI Podcast Generator (OpenRouter + pyttsx3 Edition)")
    parser.add_argument("--topic", "-t", required=True, help="Topic for the podcast")
    parser.add_argument("--output_audio_file", "-a", default="podcast.mp3", help="Output audio file name")
    parser.add_argument("--output_script_file", "-s", default="podcast_script.txt", help="Output script file name")
    parser.add_argument("--output_dir", default="output", help="Directory to store intermediate WAVs")

    args = parser.parse_args()
    os.makedirs(args.output_dir, exist_ok=True)

    try:
        script = generate_script(args.topic)
        save_script(script, args.output_script_file)
        parsed = parse_script(script)
        audio_files = generate_audio_pyttsx3(parsed, args.output_dir)
        combine_audio_files(audio_files, args.output_audio_file)
        print("\n✅ Podcast generation complete!")
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")

if __name__ == "__main__":
    main()
