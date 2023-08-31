from sqlalchemy.orm import Session

from app.constants import PermissionsNames
from app.models.permissions import PermissionRole


class PermissionService:
    def __init__(self, session: Session):
        self.session = session

    async def check_access_for_user_role(self, role_id: int, permission: PermissionsNames) -> bool:
        if self.session.query(PermissionRole). \
                filter(PermissionRole.role_id == role_id). \
                filter(PermissionRole.permission_id == permission.value).one_or_none():
            return True
        return False
