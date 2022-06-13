import enum
from sqlalchemy import Table, Column, Integer, String, ForeignKey, Float

from connect_to_db import db


class RecipeType(enum.Enum):
    salads = 'Салаты'
    snacks = 'Закуски'
    soups = 'Вторые блюда'
    sandwiches = 'Бутерброды'
    garnish = 'Вторые блюда'
    sauces = 'Соусы'
    desserts = 'Десерты'
    cakes = 'Выпечка'
    drinks = 'Напитки'


product = Table('product', db.metadata,
                Column('id', Integer, primary_key=True),
                Column('name', String, nullable=False, unique=True))

recipe = Table('recipe', db.metadata,
               Column('id', Integer, primary_key=True),
               Column('name', String, nullable=False, unique=True))

elements = Table('recipe', db.metadata,
                 Column('id', Integer, primary_key=True),
                 Column('name', String, nullable=False, unique=True))

recipe_product = Table('recipe', db.metadata,
                       Column('recipe_id', Integer, ForeignKey('recipe.id'), primary_key=True),
                       Column('product_id', Integer, ForeignKey('recipe.id'), primary_key=True),
                       Column('calories'), Float,
                       Column('fats', Float),
                       Column('carbohydrates', Float),
                       Column('description', String, nullable=False)
                       )

elements_products = Table('recipe', db.metadata,
                          Column('element_id', Integer, primary_key=True),
                          Column('product_id', Integer, primary_key=True),
                          Column('percents', Float, nullable=False))
