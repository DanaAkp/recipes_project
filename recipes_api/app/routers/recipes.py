from typing import List

from dependency_injector.wiring import inject, Provide
from fastapi import Depends, APIRouter

from app.dependencies import Container
from app.models.recipe import Recipe
from app.routers.swagger_models import RecipeDataIn, RecipeData, IngredientDataIn

recipe_router = APIRouter(
    prefix='/recipes',
    tags=['Recipes'],
    responses={
        200: {'description': 'Success'},
        401: {'description': 'Unauthorized'},
        400: {'description': 'Bad request'},
        404: {'description': 'Not found'},
    },
)


@recipe_router.get('/{recipe_id}', response_model=RecipeData)
async def get_recipe_by_id(recipe_id: int, service=Depends(Provide[Container.recipie_service])):
    result = await service.get_instance_by_id(recipe_id)
    return result


@recipe_router.post('', response_model=RecipeData)
@inject
async def create_recipe(
        data: RecipeDataIn,
        ingredients: List[IngredientDataIn] = None,
        service=Depends(Provide[Container.recipie_service]),
):
    result = await service.create_instance(kwargs=data.dict())
    return result
