from fastapi import FastAPI
from . import route

"""
    To run  the program use the following command $: hypercorn app.user_login_service.main:app --reload

"""

app = FastAPI()

app.include_router(route.router)

@app.get("/")
async def root():
    return "Login Micro-Service"
