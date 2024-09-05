from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Credentials(BaseModel):
    password: str
    ip_address: str

@app.get("/v1/password/")
def generate_password():
    rand_password = "password"
    return rand_password
