from fastapi import APIRouter, UploadFile, File
from smartsdlc.services.ai import extract_requirements

router = APIRouter()

@router.post("/extract")
async def extract_from_pdf(pdf: UploadFile = File(...)):
    """Extract structured requirements from PDF using AI."""
    contents = await pdf.read()
    requirements = extract_requirements(contents)
    return {"requirements": requirements}