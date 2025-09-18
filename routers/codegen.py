from fastapi import APIRouter
from pydantic import BaseModel
from smartsdlc.services.ai import generate_code

router = APIRouter()

class CodeGenRequest(BaseModel):
    prompt: str

@router.post("/generate")
def code_generation(req: CodeGenRequest):
    code = generate_code(req.prompt)
    return {"code": code}