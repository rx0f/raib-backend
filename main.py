from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["https://kerberos.netlify.app/"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Link(BaseModel):
    url: str

@app.post("/")
async def root(link: Link):
    print(link)
    return {"message": "Success"}

@app.head("/")
async def head():
    print("head request received correctly")
    return {"message:" "Success"}

@app.options("")
async def options():
    print("options request received correctly")
    return {"message": "Success"}