from recipe_parser import Calorizator

recipe_links = Calorizator.parse_category(Calorizator.CATEGORIES[0])

Calorizator.get_recipe(recipe_links[0])
