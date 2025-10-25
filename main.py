from fastapi import FastAPI, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from routes.transcribe import router as transcribe_router

app = FastAPI()

# Enable CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Voice AI Backend Running"}

# Add transcription routes
app.include_router(transcribe_router)
