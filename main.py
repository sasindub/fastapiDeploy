from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from model.predict_model import predict_demand

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}
