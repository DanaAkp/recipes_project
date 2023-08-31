from sqlalchemy import Column, Integer, Enum, ForeignKey
from sqlalchemy.orm import relationship

from app.constants import PermissionsNames
from app.models import Base, metadata
from app.models.roles import Role


class Permission(Base):
    __tablename__ = 'permissions'
    metadata = metadata
    id = Column(Integer, primary_key=True)
    name = Column(Enum(PermissionsNames), nullable=False)


class PermissionRole(Base):
    __tablename__ = 'permissions_roles'
    metadata = metadata
    role_id = Column(Integer, ForeignKey('roles.id'), primary_key=True)
    permission_id = Column(Integer, ForeignKey('permissions.id'), primary_key=True)

    role = relationship(Role.__table__, back_populates='PermissionRole')
    permission = relationship(Permission.__table__, back_populates='PermissionRole')
