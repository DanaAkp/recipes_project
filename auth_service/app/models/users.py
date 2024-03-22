from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship

from app.models import Base, metadata
from app.models.roles import Role


class User(Base):
    __tablename__ = 'users'
    metadata = metadata
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    hash_password = Column(String, nullable=False)
    is_block = Column(Boolean, default=False)

    # relationship
    role_id = Column(Integer, ForeignKey('role.id'), nullable=False)
    roles = relationship(Role, back_populates='users')
