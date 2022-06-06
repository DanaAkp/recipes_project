from typing import Any, List, Optional

import requests
from lxml import html


URL = 'https://calorizator.ru'


def get_html_tree_from_url(url: str) -> Optional[Any]:
    url = requests.get(url=url)
    tree = html.fromstring(url.text)
    return tree


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
    s = ''
    for number, step in zip(range(len(recipe_tree)), recipe_tree):
        s += f'{number + 1}. {step.text_content()}\n'
    return s


if __name__ == '__main__':
    categories = ['salads', 'sandwiches', 'soups', 'garnish', 'sauces', 'desserts', 'cakes', 'drinks', 'snacks']
    url = '/recipes/87004'
    tree = get_html_tree_from_url(f'{URL}/{url}')

    # buf = tree.xpath("//h1[@id='page-title']")
    # name_recipe = buf[0].text

    # buf = tree.xpath("//div[@class='field field-type-text recipes-ingredients']/div/div/ul/li")
    # ingredients = [buf[0].text]
    # print()

    buf = tree.xpath("//div[@class='field field-type-text field-field-recipe-kpfc']")
    print()

    buf = tree.xpath("//div[@class='recipes-portions']")
