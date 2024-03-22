from typing import List

from dependency_injector.wiring import inject, Provide
from fastapi import Depends, APIRouter

from app.dependencies import Container
from app.routers.swagger_models import (
    SuccessData,
    LoginDataIn,
    TokenData,
    UserData,
    UserDataIn
)

users_router = APIRouter(
    prefix='/users',
    tags=['Users'],
    responses={
        200: {'description': 'Success'},
        401: {'description': 'Unauthorized'},
        400: {'description': 'Bad request'},
        404: {'description': 'Not found'},
    },
)


@users_router.post('/login', response_model=TokenData)
@inject
async def login(
        data: LoginDataIn,
        service=Depends(Provide[Container.user_service])
):
    result = await service.login(**data.dict())
    return result


@users_router.post('/logout', response_model=UserData)
@inject
async def logout(
        user_id: int,
        service=Depends(Provide[Container.user_service])
):
    result = await service.logout(user_id)
    return result


@users_router.get('/{user_id}', response_model=UserData)
@inject
async def get_user_by_id(
        user_id: int,
        service=Depends(Provide[Container.user_service])
):
    result = await service.get_instance_by_id(user_id)
    return result


@users_router.get('', response_model=List[UserData])
@inject
async def get_all_users(service=Depends(Provide[Container.user_service])):
    result = await service.get_all_users()
    return result


@users_router.post('', response_model=UserData)
@inject
async def create_user(
        data: UserDataIn,
        service=Depends(Provide[Container.user_service]),
):
    result = await service.create_user(kwargs=data.dict())
    return result


@users_router.put('/{user_id}', response_model=UserData)
@inject
async def edit_user(
        data: UserDataIn,
        service=Depends(Provide[Container.user_service]),
):
    result = await service.edit_user(kwargs=data.dict())
    return result


@users_router.delete('/{user_id}', response_model=SuccessData)
@inject
async def delete_user(
        data: UserDataIn,
        service=Depends(Provide[Container.user_service]),
):
    result = await service.create_user(kwargs=data.dict())
    return result
