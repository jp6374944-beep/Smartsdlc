# main.py - Entry point for the FastAPI backend and Streamlit frontend

import uvicorn
from fastapi import FastAPI
from smartsdlc.routers import requirements, codegen, testing, bugfix, docs, auth, chat

app = FastAPI(
    title="SmartSDLC API",
    description="API for the AI-driven SmartSDLC platform.",
    version="1.0.0"
)

# Include modular routers
app.include_router(auth.router, prefix="/auth")
app.include_router(requirements.router, prefix="/requirements")
app.include_router(codegen.router, prefix="/codegen")
app.include_router(testing.router, prefix="/testing")
app.include_router(bugfix.router, prefix="/bugfix")
app.include_router(docs.router, prefix="/docs")
app.include_router(chat.router, prefix="/chat")

if __name__ == "__main__":
    uvicorn.run("smartsdlc.main:app", host="0.0.0.0", port=8000, reload=True)