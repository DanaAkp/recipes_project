from recipe_parser import Calorizator

recipe_links = Calorizator.parse_category(Calorizator.CATEGORIES[0])

recipe = Calorizator.get_recipe(recipe_links[0])
print(recipe)

from main import db_service, product

prod_objs = recipe.get('products')
values = []
for prod in prod_objs:
    values.append(dict(name=prod.get('mera')))
db_service.add_from_list(values=values, entity=product)

buf = db_service.get_all(product)
