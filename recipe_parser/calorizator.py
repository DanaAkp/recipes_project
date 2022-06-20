from typing import List

from recipes_adapter import AbstractRecipeParser


class Calorizator(AbstractRecipeParser):
    CATEGORIES = ['salads', 'sandwiches', 'soups', 'garnish', 'sauces', 'desserts', 'cakes', 'drinks', 'snacks']
    BASE_URL = 'https://calorizator.ru'

    def parse_category(self, category: str) -> List:
        tree = self.get_html_tree_from_url(f'{self.BASE_URL}/recipes/category/{category}')
        list_recipes_tree = tree.xpath("//td[@class='views-field views-field-title active']")

        recipe_links = []
        for i in list_recipes_tree:
            buf_a = i.xpath('a')
            recipe_links.append(buf_a[0].get('href'))
        return recipe_links

    def get_recipe(self, url_for_recipe_page: str) -> dict:
        url = f'{self.BASE_URL}{url_for_recipe_page}'
        tree = self.get_html_tree_from_url(url)
        recipe_tree = tree.xpath("//div[@itemprop='recipeInstructions']//div/div/ol//li")
        recipe_steps = ''
        for number, step in enumerate(recipe_tree):
            recipe_steps += f'{number + 1}. {step.text_content()}\n'

        buf = tree.xpath("//h1[@id='page-title']")
        name_recipe = buf[0].text

        buf = tree.xpath("//div[@class='field field-type-text recipes-ingredients']/div/div/ul/li")
        ingredients = [i.text for i in buf]

        buf = tree.xpath("//div[@class='field field-type-text field-field-recipe-kpfc']//p")
        calories_recipe = buf[1].text_content()  # 'Калории: 101.1 ккал.'
        protein_recipe = buf[2].text_content()  # 'Белки: 4.1 гр.'
        fat_recipe = buf[3].text_content()  # 'Жиры: 4.3 гр.'
        carbohydrates_recipe = buf[4].text_content()  # 'Углеводы: 12 гр.'

        buf = tree.xpath("//div[@class='recipes-portions']//span")
        portions = buf[0].text_content()

        buf = tree.xpath("//div[@class='field field-type-text field-field-recipe-table']//tbody//tr")
        products = []
        for i in buf:
            tr = list(filter(lambda x: x != '',
                             i.text_content().split('\n')))
            mera = tr[0]
            weight = tr[0]
            protein_product = tr[0]
            fat_product = tr[0]
            carbohydrates_product = tr[0]
            calories_product = tr[0]
            products.append(dict(mera=mera, weight=weight, protein_product=protein_product, fat_product=fat_product,
                                 carbohydrates_product=carbohydrates_product, calories_product=calories_product))

        buf = tree.xpath("//div[@class='field field-type-text field-field-recipe-table']//tfoot//tr")
        total = list(filter(lambda x: x != '', buf[0].text_content().split('\n')))
        one_portion = list(filter(lambda x: x != '', buf[1].text_content().split('\n')))
        one_hundred_grams = list(filter(lambda x: x != '', buf[2].text_content().split('\n')))

        return dict(
            total=total, one_hundred_grams=one_hundred_grams, one_portion=one_portion,
            name_recipe=name_recipe, recipe_steps=recipe_steps, products=products, portions=portions,
            calories_recipe=calories_recipe, protein_recipe=protein_recipe, fat_recipe=fat_recipe,
            carbohydrates_recipe=carbohydrates_recipe, ingredients=ingredients
        )
