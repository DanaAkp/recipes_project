from typing import List, Optional
from pydantic import BaseModel


class DataBaseModel(BaseModel):
    class Config:
        orm_mode = True


class IngredientData(DataBaseModel):
    product_id: int
    amount: float


class IngredientDataIn(DataBaseModel):
    product_id: int
    recipe_id: Optional[int]
    amount: float


class RecipeData(DataBaseModel):
    id: int
    name: str
    description: str
    ingredients: Optional[List[IngredientData]]


class RecipeDataIn(DataBaseModel):
    name: str
    description: str
