from fastapi import FastAPI
from . import route

"""
    To run  the program use the following command $: uvicorn app.account_registration_service.main:app --port 8003 --reload
    
"""

app = FastAPI()

app.include_router(route.router)

@app.get("/")
async def root():
    return "Account Registration Micro-Service"
