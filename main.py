from typing import List
from urllib.request import Request
from fastapi import FastAPI, Response, status
from pydantic import BaseModel
import uvicorn
import traceback

# Init priority instances
app = FastAPI()

class RequestText(BaseModel):
    text:List[str]
    
@app.get("/")
async def index():
    return "Hello from sentiment prediction endpoint"

@app.post("/")
async def predict(req: RequestText, response: Response):
    try:
        texts = req.text

        # Create a list of the prediction and the output

        return {
        }
    except Exception as e:
        traceback.print_exc()
        response.status_code = 500
        return {"message" : "Internal Server Error"} 
    
port = 8001
print(f"Listening to http://0.0.0.0:{port}")
uvicorn.run(app, host='0.0.0.0',port=port)