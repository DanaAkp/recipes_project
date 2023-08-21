from typing import List

from dependency_injector.wiring import inject, Provide
from fastapi import Depends, APIRouter

from app.constants import UnitMeasure
from app.dependencies import Container
from app.routers.swagger_models import SuccessData
from app.routers.swagger_models.products import ProductData, ProductDataIn

product_router = APIRouter(
    prefix='/products',
    tags=['Products'],
    responses={
        200: {'description': 'Success'},
        401: {'description': 'Unauthorized'},
        400: {'description': 'Bad request'},
        404: {'description': 'Not found'},
    },
)


@product_router.get('/measure_units', response_model=List[str])
@inject
async def get_all_measure_units():
    return UnitMeasure.get_all_units()


@product_router.get('/{product_id}', response_model=ProductData)
@inject
async def get_product_by_id(
        product_id: int,
        service=Depends(Provide[Container.product_service])
):
    result = await service.get_instance_by_id(product_id)
    return result


@product_router.get('', response_model=List[ProductData])
@inject
async def get_all_products(service=Depends(Provide[Container.product_service])):
    result = await service.get_all_instances()
    return result


@product_router.post('', response_model=ProductData)
@inject
async def create_product(
        data: ProductDataIn,
        service=Depends(Provide[Container.product_service]),
):
    result = await service.create_instance(kwargs=data.dict())
    return result


@product_router.delete('/{product_id}', response_model=SuccessData)
@inject
async def delete_product(
        product_id: int,
        service=Depends(Provide[Container.product_service]),
):
    result = await service.delete_instance(product_id)
    return result


@product_router.put('/{product_id}', response_model=ProductData)
@inject
async def update_product(
        product_id: int,
        data: ProductDataIn,
        service=Depends(Provide[Container.product_service]),
):
    result = await service.update_instance(instance_id=product_id, kwargs=data.dict())
    return result
