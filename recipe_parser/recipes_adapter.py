from abc import ABC, abstractmethod
from typing import Any, Optional, List

import requests
from lxml import html


class AbstractRecipeParser(ABC):
    CATEGORIES: List[str]
    BASE_URL: str

    @staticmethod
    def get_html_tree_from_url(url: str) -> Optional[Any]:
        url = requests.get(url=url)
        tree = html.fromstring(url.text)
        return tree

    @abstractmethod
    def parse_category(self, category: str) -> List:
        pass

    @abstractmethod
    def get_recipe(self, url_for_recipe_page: str) -> dict:
        pass

    @abstractmethod
    def get_products(self, category: str) -> List:
        pass
