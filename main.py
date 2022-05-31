from fastapi import FastAPI, Form, Query, Path, Body
from schemas import Ingredient, Recipe

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.post('/ingredients', response_model=Ingredient)
def create_ingredient(item: Ingredient):
    return item


@app.post('/recipes')
def create_recipes(item: Recipe):
    return item


@app.get('/ingredients')
def get_ingredient(q: str = Query(..., max_length=5, min_length=1, description='test query.')):
    return q


@app.get('/ingredient/{id}')
def get_ingredient_by_id(id: int = Path(..., gt=1, le=20)):
    return {'id': id}


@app.post('/test_body')
def post_body(test_body: int = Body(..., embed=True)):
    return {'body': test_body}
