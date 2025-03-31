from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi import Request
from fastapi.middleware import Middleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from typing import Optional
import os
from utils.colab_parser import ColabParser
from utils.llm_handler import LLMHandler
import json

app = FastAPI(middleware=[
    Middleware(TrustedHostMiddleware, allowed_hosts=["*"])
])


app = FastAPI()

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize components
colab_parser = ColabParser()
llm_handler = LLMHandler()

# Predefined assignment URLs
ASSIGNMENT_URLS = {
    "ga1": "https://colab.research.google.com/drive/18DEwIHf8oLrAUsVP5r0Y3XYqjw2mCpQB",
    "ga2": "https://colab.research.google.com/drive/1Q1A7RjbOejme_ZAsJCLbUyY1hN6mKrZB",
    "ga3": "https://colab.research.google.com/drive/1iqhz1htAdqUsQn6n4W5OuXdR7fquMz0k",
    "ga4": "https://colab.research.google.com/drive/13473Dl2L99f0lfbC33cyAgOTX-LXybMz",
    "ga5": "https://colab.research.google.com/drive/1wO8bk82odsA-_rMaukhj2qsp3KAjkwtO"
}

@app.post("/api/")
async def answer_question(
    question: str = Form(...),
    assignment_number: str = Form(...),
    file: Optional[UploadFile] = File(None)
):
    try:
        # Determine which assignment we're working with
        if assignment_number not in ASSIGNMENT_URLS:
            raise HTTPException(status_code=400, detail="Invalid assignment number")
        
        colab_url = ASSIGNMENT_URLS[assignment_number]
        
        # Get relevant content from the Colab notebook
        notebook_content = colab_parser.get_notebook_content(colab_url)
        
        # Process the question with LLM
        answer = llm_handler.get_answer(question, notebook_content)
        
        return {"answer": answer}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
async def health_check():
    return {"status": "healthy"}
