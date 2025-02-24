from fastapi import FastAPI
from models import Receivable
from typing import List
from datetime import date

app = FastAPI()

# Temporary in-memory database (for now)
receivables_db = []

@app.get("/")
def read_root():
    return {"message": "Welcome to FinTrack!"}

@app.post("/receivables/", response_model=Receivable)
def create_receivable(receivable: Receivable):
    receivables_db.append(receivable)
    return receivable

@app.get("/receivables/", response_model=List[Receivable])
def list_receivables():
    return receivables_db

