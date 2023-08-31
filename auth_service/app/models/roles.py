from sqlalchemy import Column, Integer, Enum

from app.constants import RolesNames
from app.models import Base, metadata


class Role(Base):
    __tablename__ = 'roles'
    metadata = metadata
    id = Column(Integer, primary_key=True)
    name = Column(Enum(RolesNames), nullable=False)
