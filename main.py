from fastapi import FastAPI, HTTPException
from passlib.context import CryptContext
from pydantic import BaseModel

class Password(BaseModel):
    password: str

app = FastAPI()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@app.post("/hash/")
async def hash_password(password: Password):
    if len(password.password) < 8:
        raise HTTPException(status_code=400, detail="Password too short")

    security = verify(password.password)

    if security == "unsafe": raise HTTPException(status_code=400, detail="Password is not secure")

    return {
            "hashed_password": pwd_context.hash(password.password),
            "security": security
            }

def verify(password):
    security = 0
    upper = False 
    lower = False 
    number = False 
    
    for char in password:
        if char.isupper(): upper = True
        elif char.islower(): lower = True
        elif char.isdigit(): number = True
    
    if upper: security += 1
    if lower: security += 1
    if number: security += 1

    if security == 1: return "unsafe"
    if security == 2: return "moderately safe"
    if security == 3: return "secure password"