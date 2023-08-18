from sqlalchemy import Column, Integer, String, Float, ForeignKey

from app.models import Base, metadata
from app.models.product import Product


class Recipe(Base):
    __tablename__ = 'recipes'
    metadata = metadata
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    description = Column(String, nullable=False)


class RecipeProduct(Base):
    __tablename__ = 'recipes_products'
    metadata = metadata
    recipe_id = Column(Integer, ForeignKey('recipes.id'), primary_key=True)
    product_id = Column(Integer, ForeignKey('products.id'), primary_key=True)
    amount = Column(Float, nullable=False)
