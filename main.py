from fastapi import FastAPI

from database.connect_to_db import DBConnect
from database.db_service import DBService

app = FastAPI()


@app.on_event("startup")
async def startup_event():
    pass

from database.models import db, RecipeType, recipe, product, recipe_product, element_product

db_service = DBService(db.connect)
