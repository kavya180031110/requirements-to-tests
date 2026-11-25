import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from services.summary import summarize

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=os.getenv("ALLOWED_ORIGINS", "http://localhost:5173").split(","),
    allow_methods=["POST"],
    allow_headers=["Content-Type"],
)

class SummaryRequest(BaseModel):
    requirement: str

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/summary")
def summary(body: ummaryRequest)
    try:
        return {"result": summarize(body.requirement)}
    except Exception as e: 
        print("AI ERROR:", repr(e))
        raise HTTPException(status_code=502, detail="AI call failed")