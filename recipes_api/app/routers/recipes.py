from typing import List

from dependency_injector.wiring import inject, Provide
from fastapi import Depends, APIRouter

from app.dependencies import Container
from app.routers.swagger_models import SuccessData
from app.routers.swagger_models.recipes import RecipeDataIn, RecipeData, IngredientDataIn
from app.constants import RecipeType

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


@recipe_router.get('/types', response_model=List[str])
async def get_all_types_of_recipes():
    return RecipeType.get_all_types()


@recipe_router.get('/{recipe_id}', response_model=RecipeData)
@inject
async def get_recipe_by_id(
        recipe_id: int,
        service=Depends(Provide[Container.recipie_service])
):
    result = await service.get_instance_by_id(recipe_id)
    return result


@recipe_router.get('', response_model=List[RecipeData])
@inject
async def get_all_recipes(service=Depends(Provide[Container.recipie_service])):
    result = await service.get_all_instances()
    return result


@recipe_router.post('', response_model=RecipeData)
@inject
async def create_recipe(
        data: RecipeDataIn,
        ingredients: List[IngredientDataIn] = None,
        service=Depends(Provide[Container.recipie_service]),
):
    result = await service.create_instance(kwargs=data.dict())
    if ingredients:
        await service.add_products_to_recipes(result.id, ingredients)
    return result


@recipe_router.delete('/{recipe_id}', response_model=SuccessData)
@inject
async def delete_recipe(
        recipe_id: int,
        service=Depends(Provide[Container.recipie_service]),
):
    result = await service.delete_instance(recipe_id)
    return result


@recipe_router.put('/{recipe_id}', response_model=RecipeData)
@inject
async def update_recipe(
        recipe_id: int,
        data: RecipeDataIn,
        ingredients: List[IngredientDataIn] = None,
        service=Depends(Provide[Container.recipie_service]),
):
    result = await service.update_instance(instance_id=recipe_id, kwargs=data.dict())
    if ingredients:
        await service.add_products_to_recipes(result.id, ingredients)
    return result


@recipe_router.post('/{recipe_id}/products', response_model=RecipeData)
@inject
async def add_products_to_recipe(
        recipe_id: int,
        ingredients: List[IngredientDataIn],
        service=Depends(Provide[Container.recipie_service]),
):
    result = await service.add_products_to_recipes(recipe_id, ingredients)
    return result


@recipe_router.delete('/{recipe_id}/products/{product_id}', response_model=SuccessData)
@inject
async def delete_product_from_recipe(
        recipe_id: int,
        product_id: int,
        service=Depends(Provide[Container.recipie_service]),
):
    result = await service.delete_product_from_recipe(recipe_id, product_id)
    return result


@recipe_router.patch('/{recipe_id}/products/{product_id}', response_model=SuccessData)
@inject
async def change_amount_product_from_recipe(
        recipe_id: int,
        product_id: int,
        amount: float,
        service=Depends(Provide[Container.recipie_service]),
):
    result = await service.change_amount_product(recipe_id, product_id, amount)
    return result


