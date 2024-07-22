from enum import Enum


class RecipeType(Enum):
    salads = 'Салаты'
    snacks = 'Закуски'
    soups = 'Вторые блюда'
    sandwiches = 'Бутерброды'
    garnish = 'Вторые блюда'
    sauces = 'Соусы'
    desserts = 'Десерты'
    cakes = 'Выпечка'
    drinks = 'Напитки'

    @classmethod
    def get_all_types(cls):
        return [type_.value for type_ in cls]


class UnitMeasure(Enum):
    gram = 'грамм'
    millilitre = 'миллилитр'

    @classmethod
    def get_all_units(cls):
        return [type_.value for type_ in cls]
