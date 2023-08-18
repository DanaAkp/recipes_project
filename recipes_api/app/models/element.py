from sqlalchemy import Column, Integer, String, Float, ForeignKey
from app.models import Base, metadata


class Element(Base):
    __tablename__ = 'elements'
    metadata = metadata
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)


class ElementProduct(Base):
    __tablename__ = 'elements_products'
    metadata = metadata
    element_id = Column(Integer, ForeignKey('elements.id'), primary_key=True)
    product_id = Column(Integer, ForeignKey('products.id'), primary_key=True)
    percents = Column(Float, nullable=False)
