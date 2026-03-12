from fastapi import FastAPI
from app.router import products

app = FastAPI()

app.include_router(products.router)

@app.get('/')
def home():
    return {"message" : "CRUD prectice"}


# for running command --> uvicorn app.main:app --reload    (folder.file:object)