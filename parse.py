from typing import Any, List, Optional

import requests
from lxml import html


URL = 'https://calorizator.ru'

#
def get_html_tree_from_url(url: str) -> Optional[Any]:
    url = requests.get(url=url)
    tree = html.fromstring(url.text)
    return tree

#
def parse_category(category: str) -> List:
    tree = get_html_tree_from_url(f'{URL}/recipes/category/{category}')
    list_recipes_tree = tree.xpath("//td[@class='views-field views-field-title active']")

    recipe_links = []
    for i in list_recipes_tree:
        buf_a = i.xpath('a')
        recipe_links.append(buf_a[0].get('href'))
    return recipe_links


def parse_recipe(recipe_link: str) -> str:
    url = f'{URL}{recipe_link}'
    tree = get_html_tree_from_url(url)
    recipe_tree = tree.xpath("//div[@itemprop='recipeInstructions']//div/div/ol//li")
    recipe_steps = ''
    for number, step in zip(range(len(recipe_tree)), recipe_tree):
        recipe_steps += f'{number + 1}. {step.text_content()}\n'

    # buf = tree.xpath("//h1[@id='page-title']")
    # name_recipe = buf[0].text

    # buf = tree.xpath("//div[@class='field field-type-text recipes-ingredients']/div/div/ul/li")
    # ingredients = [i.text for i in buf]
    # print()

    buf = tree.xpath("//div[@class='field field-type-text field-field-recipe-kpfc']//p")
    print()
    calories_recipe = buf[1].text_content()  # 'Калории: 101.1 ккал.'
    protein_recipe = buf[2].text_content()  # 'Белки: 4.1 гр.'
    fat_recipe = buf[3].text_content()  # 'Жиры: 4.3 гр.'
    carbohydrates_recipe = buf[4].text_content()  # 'Углеводы: 12 гр.'

    buf = tree.xpath("//div[@class='recipes-portions']//span")
    portions = buf[0].text_content()

    buf = tree.xpath("//div[@class='field field-type-text field-field-recipe-table']//tbody//tr")
    for i in buf:
        tr = list(filter(lambda x: x != '', i.text_content().split('\n')))  # [' нут', '100 гр', '100', '19', '6', '61', '364']
        mera = tr[0]
        weight = tr[0]
        protein_product = tr[0]
        fat_product = tr[0]
        carbohydrates_product = tr[0]
        calories_product = tr[0]

    buf = tree.xpath("//div[@class='field field-type-text field-field-recipe-table']//tfoot//tr")
    total = list(filter(lambda x: x != '', buf[0].text_content().split('\n')))  # ['Итого', '\xa0', '618', '25.4', '26.4', '73.9', '625.1']
    one_portion = list(filter(lambda x: x != '', buf[1].text_content().split('\n')))  # ['1 порция', '\xa0', '77', '3.2', '3.3', '9.2', '78.1']
    one_hundred_grams = list(filter(lambda x: x != '', buf[2].text_content().split('\n')))  # ['100 грамм', '\xa0', '100', '4.1', '4.3', '12', '101.1']

    return recipe_steps


if __name__ == '__main__':
    categories = ['salads', 'sandwiches', 'soups', 'garnish', 'sauces', 'desserts', 'cakes', 'drinks', 'snacks']
    url = '/recipes/87004'
    tree = get_html_tree_from_url(f'{URL}/{url}')
