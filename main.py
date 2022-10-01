from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Link(BaseModel):
    url: str

@app.post("/")
async def root(link: Link):
    print(link)
    return {"message": "Success"}