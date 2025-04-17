from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from modules.stream import StreamCapture
from modules.hash import EntropyGenerator

app = FastAPI()

# Autoriser les requêtes depuis ton frontend local
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # autorise toutes les origines (à restreindre si besoin)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class StreamRequest(BaseModel):
    url: str

@app.post("/generate")
async def generate_entropy(request: StreamRequest):
    try:
        stream = StreamCapture(request.url)
        frame = stream.capture_frame()
        entropy = EntropyGenerator.hash_frame(frame)
        return {"entropy": entropy}
    except Exception as e:
        return {"error": str(e)}
