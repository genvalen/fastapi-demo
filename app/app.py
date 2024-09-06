from fastapi import FastAPI, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from sqlalchemy.orm import Session
import psycopg2
from psycopg2.extras import RealDictCursor
import time

from . import models
from .database import engine, get_db
from .password_generator import password_generator

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

class Credentials(BaseModel):
    password: str
    ip_address: str

while True:
    try:
        conn = psycopg2.connect(host='localhost', dbname='demo', user='postgres', \
            password="password", cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Database connection was successful.")
        break
    except Exception as error:
        print("the database connection failed.")
        print(f"The error was: {error}")
        time.sleep(2)

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")

@app.get("/v1/password/", response_class=HTMLResponse)
async def get_password(request: Request, db: Session = Depends(get_db)):
    password = password_generator()
    # new_password = models.Credentials(password=password, ip_address="192.158.1.38")
    # db.add(new_password)
    # db.commit()
    # db.refresh(new_password)
    return templates.TemplateResponse(request=request, name="password.html", context={"password": password})
