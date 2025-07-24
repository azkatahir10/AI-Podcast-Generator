from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Optional
import os
from dotenv import load_dotenv
from podcast_generator import generate_script, parse_script, generate_audio_pyttsx3, combine_audio_files, save_script

# Load environment variables
load_dotenv()

app = FastAPI(
    title="AI Podcast Generator API",
    description="API for generating AI-powered podcasts with script generation and voice synthesis",
    version="1.0.0"
)

class PodcastRequest(BaseModel):
    topic: str
    output_audio_file: Optional[str] = "podcast.mp3"
    output_script_file: Optional[str] = "podcast_script.txt"
    output_dir: Optional[str] = "output"

class PodcastResponse(BaseModel):
    success: bool
    message: str
    audio_file: Optional[str] = None
    script_file: Optional[str] = None

@app.post("/generate_podcast", response_model=PodcastResponse)
async def generate_podcast(request: PodcastRequest):
    try:
        # Clean previous output if exists
        if os.path.exists(request.output_dir):
            for file in os.listdir(request.output_dir):
                os.remove(os.path.join(request.output_dir, file))
            os.rmdir(request.output_dir)
        
        # Create output directory
        os.makedirs(request.output_dir, exist_ok=True)

        # Generate script
        script = generate_script(request.topic)
        save_script(script, request.output_script_file)
        
        # Parse and generate audio
        parsed = parse_script(script)
        audio_files = generate_audio_pyttsx3(parsed, request.output_dir)
        combine_audio_files(audio_files, request.output_audio_file)

        return PodcastResponse(
            success=True,
            message="Podcast generated successfully",
            audio_file=request.output_audio_file,
            script_file=request.output_script_file
        )
    
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )

@app.get("/")
async def root():
    return {"message": "AI Podcast Generator API - Use /generate_podcast endpoint to create podcasts"}