import enum
from sqlalchemy import Table, Column, Integer, String, ForeignKey, Float
from database.connect_to_db import DBConnect

db = DBConnect("sqlite:///test.db")


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


product = Table(
    'product',
    db.metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String, nullable=False, unique=True),
    Column('calories', Float),
    Column('fats', Float),
    Column('carbohydrates', Float),
    Column('proteins', Float),
)

recipe = Table(
    'recipe',
    db.metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String, nullable=False, unique=True)
)

element = Table(
    'element',
    db.metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String, nullable=False, unique=True)
)

recipe_product = Table(
    'recipe_product',
    db.metadata,
    Column('recipe_id', Integer, ForeignKey('recipe.id'), primary_key=True),
    Column('product_id', Integer, ForeignKey('product.id'), primary_key=True),
    Column('calories', Float),
    Column('fats', Float),
    Column('carbohydrates', Float),
    Column('proteins', Float),
    Column('description', String, nullable=False)
)

element_product = Table(
    'element_product',
    db.metadata,
    Column('element_id', Integer, ForeignKey('element.id'), primary_key=True),
    Column('product_id', Integer, ForeignKey('product.id'), primary_key=True),
    Column('percents', Float, nullable=False)
)

db.metadata.create_all(bind=db.engine)
