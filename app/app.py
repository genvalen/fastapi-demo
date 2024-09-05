from fastapi import FastAPI, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from . import models
from .database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
class Credentials(BaseModel):
    password: str
    ip_address: str

@app.get("/v1/password/")
def generate_password(db: Session = Depends(get_db)):
    rand_password = "password"
    return rand_password
