# from recipe_parser import Calorizator
#
# recipe_links = Calorizator.parse_category(Calorizator.CATEGORIES[0])
#
# recipe = Calorizator.get_recipe(recipe_links[0])
from main import db
from database.models import Product

db.session.add(Product(name='Potato'))
db.session.commit()
db.session.query(Product).all()
print()
