from dependency_injector import providers, containers
from fastapi import Security
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from app.controllers.products_service import ProductService
from app.controllers.recipes_service import RecipeService
from app.controllers.elements_service import ElementService

from app.models.recipe import Recipe


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()
    security: HTTPAuthorizationCredentials = Security(HTTPBearer())

    recipie_service = providers.Singleton(RecipeService, session=config.session, model=Recipe)
    product_service = providers.Singleton(ProductService, session=config.session)
    element_service = providers.Singleton(ElementService, session=config.session)
