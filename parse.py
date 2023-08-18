from app.recipe_parser import Calorizator

recipe_links = Calorizator.parse_category(Calorizator.CATEGORIES[0])

recipe = Calorizator.get_recipe(recipe_links[0])
print(recipe)

# from app.main import db_service, product
#
# prod_objs = recipe.get('products')
# for prod in prod_objs:
#     db_service.get_or_create(dict(name=prod.get('mera')), entity=product)
#
# buf = db_service.get_all(product)
