from typing import List

from pydantic import BaseModel, validator, Field


class Ingredient(BaseModel):
    name: str
    test_field: int = Field(None, gt=15, lt=90, description='Число должно быть больше 15 и меньше 90')

    @validator('name')
    def check_name(cls, value):
        if '!' in value:
            raise ValueError('! не может быть в названии ингредиента')
        return value


class Recipe(BaseModel):
    ingredients: List[Ingredient]
