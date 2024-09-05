from fastapi import FastAPI, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from . import models
from .database import engine, get_db
import psycopg2
from psycopg2.extras import RealDictCursor
import time

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
class Credentials(BaseModel):
    password: str
    ip_address: str


while True:
    try:
        conn = psycopg2.connect(host='localhost', dbname='fastapi', user='postgres', \
            password="password", cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Database connection was successful.")
        break
    except Exception as error:
        print("the database connection failed.")
        print(f"The error was: {error}")
        time.sleep(2)


@app.get("/v1/password/")
def generate_password(db: Session = Depends(get_db)):
    rand_password = "password"
    return rand_password
