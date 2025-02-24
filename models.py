from pydantic import BaseModel
from datetime import date

class Receivable(BaseModel):
    id: str  
    company_name: str
    amount: float 
    due_date: date 
    status: str 
