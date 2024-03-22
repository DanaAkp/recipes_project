from dependency_injector import providers, containers
from fastapi import Security
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from app.controllers import RoleService, UserService, PermissionService


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()
    security: HTTPAuthorizationCredentials = Security(HTTPBearer())

    permission_service = providers.Singleton(PermissionService, session=config.session)
    role_service = providers.Singleton(
        RoleService,
        session=config.session,
        permission_service=permission_service
    )
    user_service = providers.Singleton(
        UserService,
        session=config.session,
        permission_service=permission_service
    )
