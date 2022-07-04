from typing import List

from recipe_parser.recipes_adapter import AbstractRecipeParser


class Calorizator(AbstractRecipeParser):
    CATEGORIES = ['salads', 'sandwiches', 'soups', 'garnish', 'sauces', 'desserts', 'cakes', 'drinks', 'snacks']
    BASE_URL = 'https://calorizator.ru'

    @classmethod
    def parse_category(cls, category: str) -> List:
        tree = cls.get_html_tree_from_url(f'{cls.BASE_URL}/recipes/category/{category}')
        list_recipes_tree = tree.xpath("//td[@class='views-field views-field-title active']")

        recipe_links = []
        for i in list_recipes_tree:
            buf_a = i.xpath('a')
            recipe_links.append(buf_a[0].get('href'))
        return recipe_links

    @classmethod
    def get_recipe(cls, url_for_recipe_page: str) -> dict:
        url = f'{cls.BASE_URL}{url_for_recipe_page}'
        tree = cls.get_html_tree_from_url(url)
        recipe_tree = tree.xpath("//div[@itemprop='recipeInstructions']//div/div/ol//li")
        recipe_steps = ''
        for number, step in enumerate(recipe_tree):
            recipe_steps += f'{number + 1}. {step.text_content()}\n'

        buf = tree.xpath("//h1[@id='page-title']")
        name_recipe = buf[0].text

        buf = tree.xpath("//div[@class='field field-type-text recipes-ingredients']/div/div/ul/li")
        ingredients = [i.text for i in buf]

        buf = tree.xpath("//div[@class='recipes-portions']//span")
        portions = buf[0].text_content()

        buf = tree.xpath("//div[@class='field field-type-text field-field-recipe-table']//tbody//tr")
        products = []
        for i in buf:
            tr = list(filter(lambda x: x != '',
                             i.text_content().split('\n')))
            mera = tr[0]
            weight = tr[1]
            protein_product = tr[2]
            fat_product = tr[3]
            carbohydrates_product = tr[4]
            calories_product = tr[5]
            products.append(dict(mera=mera, weight=weight, protein_product=protein_product, fat_product=fat_product,
                                 carbohydrates_product=carbohydrates_product, calories_product=calories_product))

        buf = tree.xpath("//div[@class='field field-type-text field-field-recipe-table']//tfoot//tr")
        filter_lambda = lambda x: x not in ('', '\xa0')
        total = list(filter(filter_lambda, buf[0].text_content().split('\n')))
        one_portion = list(filter(filter_lambda, buf[1].text_content().split('\n')))
        one_hundred_grams = list(filter(filter_lambda, buf[2].text_content().split('\n')))

        return dict(
            total=total,
            one_hundred_grams=one_hundred_grams,
            one_portion=one_portion,
            name_recipe=name_recipe,
            recipe_steps=recipe_steps,
            products=products,
            portions=portions,
            ingredients=ingredients
        )
