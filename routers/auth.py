from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.post("/login")
def login(username: str, password: str):
    # Dummy authentication check
    if username == "admin" and password == "password":
        return {"token": "example-token"}
    raise HTTPException(status_code=401, detail="Invalid credentials")