from fastapi import FastAPI

from connect_to_db import DBConnect

app = FastAPI()


@app.on_event("startup")
async def startup_event():
    pass

db = DBConnect("sqlite:///test.db")

from models import product, recipe_product, element_product, recipe

db.metadata.create_all(bind=db.engine)

