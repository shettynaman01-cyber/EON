
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import httpx

app = FastAPI(
    title="EON AI",
    description="Personal Artificial Intelligence System",
    version="1.0.0"
)

OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL_NAME = "qwen3:4b"

SYSTEM_PROMPT = """
You are EON, a personal artificial intelligence assistant.

Your name is EON. Always introduce yourself as EON,
not as Qwen or another underlying AI model.

You are helpful, intelligent, friendly, and professional.
You help users with learning, reasoning, research,
problem-solving, and programming.

Give clear, accurate, and easy-to-understand answers.
"""


class ChatRequest(BaseModel):
    message: str


@app.get("/")
def home():
    return {
        "message": "EON is online!",
        "status": "running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "assistant": "EON"
    }


@app.post("/chat")
async def chat(request: ChatRequest):

    try:
        async with httpx.AsyncClient(timeout=180.0) as client:
            response = await client.post(
                OLLAMA_URL,
                json={
                    "model": MODEL_NAME,
                    "messages": [
                        {
                            "role": "system",
                            "content": SYSTEM_PROMPT
                        },
                        {
                            "role": "user",
                            "content": request.message
                        }
                    ],
                    "stream": False
                }
            )

            response.raise_for_status()
            result = response.json()

            return {
                "assistant": "EON",
                "reply": result["message"]["content"]
            }

    except httpx.ConnectError:
        raise HTTPException(
            status_code=503,
            detail="Ollama is not running."
        )

    except httpx.HTTPError:
        raise HTTPException(
            status_code=502,
            detail="Could not get a response from the AI model."
        )
