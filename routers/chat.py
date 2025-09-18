from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class ChatRequest(BaseModel):
    message: str

@router.post("/ask")
def ask_chatbot(req: ChatRequest):
    # Placeholder for AI chatbot integration
    return {"response": f"AI response to: {req.message}"}