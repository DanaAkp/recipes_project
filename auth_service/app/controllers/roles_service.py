from sqlalchemy.orm import Session

from app.controllers.access_service import PermissionService
from app.constants import PermissionsNames
from app.models.roles import Role
from app.models.users import User


class RoleService:
    def __init__(self, session: Session, permission_service: PermissionService):
        self.session = session
        self.permission_service = permission_service

    async def add_role_to_user(self, user_id: int, role_id: int) -> dict:
        raise NotImplementedError('Method not implemented.')

    async def delete_role_from_user(self, user_id: int, role_id: int) -> dict:
        raise NotImplementedError('Method not implemented.')

