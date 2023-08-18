from sqlalchemy import Column, Integer, String, Float
from app.models import Base, metadata


class Product(Base):
    __tablename__ = 'products'
    metadata = metadata
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    calories = Column(Float)
    fats = Column(Float)
    carbohydrates = Column(Float)
    proteins = Column(Float)
