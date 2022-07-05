import enum
from sqlalchemy import Table, Column, Integer, String, ForeignKey, Float

from main import db


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


class Product(db.Base):
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)


db.metadata.create_all(bind=db.engine)
db.session.add(Product(name='Potato'))
db.session.commit()
db.session.query(Product).all()
print()


# product = Table(
#     'product', db.metadata,
#     Column('id', Integer, primary_key=True),
#     Column('name', String, nullable=False, unique=True)
# )
#
# recipe = Table(
#     'recipe',
#     db.metadata,
#     Column('id', Integer, primary_key=True),
#     Column('name', String, nullable=False, unique=True)
# )
#
# element = Table(
#     'element', db.metadata,
#     Column('id', Integer, primary_key=True),
#     Column('name', String, nullable=False, unique=True)
# )
#
# recipe_product = Table(
#     'recipe_product', db.metadata,
#     Column('recipe_id', Integer, ForeignKey('recipe.id'), primary_key=True),
#     Column('product_id', Integer, ForeignKey('product.id'), primary_key=True),
#     Column('calories', Float),
#     Column('fats', Float),
#     Column('carbohydrates', Float),
#     Column('description', String, nullable=False)
# )
#
# element_product = Table(
#     'element_product', db.metadata,
#     Column('element_id', Integer, ForeignKey('element.id'), primary_key=True),
#     Column('product_id', Integer, ForeignKey('product.id'), primary_key=True),
#     Column('percents', Float, nullable=False)
# )
