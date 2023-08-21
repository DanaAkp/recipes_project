from sqlalchemy import Column, Integer, String, Float, Enum
from app.models import Base, metadata
from app.constants import UnitMeasure


class Product(Base):
    __tablename__ = 'products'
    metadata = metadata
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    calories = Column(Float)
    fats = Column(Float)
    carbohydrates = Column(Float)
    proteins = Column(Float)
    unit_measure = Column(Enum(UnitMeasure), nullable=False)
    units_measure_nutrition_facts = Column(Integer, nullable=False)
