from typing import List, Optional
from pydantic import Field
from app.constants import RecipeType
from app.routers.swagger_models import DataBaseModel


class IngredientData(DataBaseModel):
    product_id: int
    amount: float


class IngredientDataIn(DataBaseModel):
    product_name: str
    recipe_id: int
    amount: float


class RecipeData(DataBaseModel):
    id: int
    name: str
    description: str
    type: Optional[RecipeType]
    ingredients: Optional[List[IngredientData]]


class RecipeDataIn(DataBaseModel):
    name: str
    description: str
    type: RecipeType = Field(default='Салаты')
