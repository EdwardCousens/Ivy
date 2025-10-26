import os
import requests
from fastapi import APIRouter, UploadFile
from fastapi.responses import JSONResponse

router = APIRouter(prefix="/transcribe")

WHISPER_API_KEY = os.getenv("WHISPER_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

@router.post("/")
async def transcribe_audio(file: UploadFile):
    # Step 1: Send audio to Whisper API
    whisper_url = "https://api.whisperapi.com/transcribe"
    headers = {"Authorization": f"Bearer {WHISPER_API_KEY}"}
    files = {"file": (file.filename, await file.read(), file.content_type)}

    whisper_response = requests.post(whisper_url, headers=headers, files=files)
    whisper_data = whisper_response.json()
    transcript_text = whisper_data.get("text", "")

    # Step 2: Send transcript to OpenAI GPT
    openai_url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "gpt-5-nano",
        "messages": [{"role": "user", "content": transcript_text}]
    }

    gpt_response = requests.post(openai_url, headers=headers, json=data)
    gpt_data = gpt_response.json()
    ai_reply = gpt_data.get("choices", [{}])[0].get("message", {}).get("content", "")

    return JSONResponse(content={
        "transcript": transcript_text,
        "response": ai_reply
    })
