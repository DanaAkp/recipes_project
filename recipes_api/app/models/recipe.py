from sqlalchemy import Column, Integer, String, Float, ForeignKey, Enum
from sqlalchemy.orm import relationship

from app.models import Base, metadata
from app.models.product import Product
from app.constants import RecipeType


class Recipe(Base):
    __tablename__ = 'recipes'
    metadata = metadata
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    description = Column(String, nullable=False)
    type = Column(Enum(RecipeType))

    ingredients = relationship('RecipeProduct', backref='recipes', uselist=True)


class RecipeProduct(Base):
    __tablename__ = 'recipes_products'
    metadata = metadata
    recipe_id = Column(Integer, ForeignKey('recipes.id'), primary_key=True)
    product_id = Column(Integer, ForeignKey('products.id'), primary_key=True)
    amount = Column(Float, nullable=False)

    product = relationship(Product, backref='recipes_products')
    recipe = relationship(Recipe, backref='recipes_products')
