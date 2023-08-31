from enum import Enum


class RolesNames(Enum):
    admin = 1
    user = 2
    writer = 3


class PermissionsNames(Enum):
    create_recipes = 1
    edit_recipes = 2
    delete_recipes = 3

    create_products = 4
    edit_products = 5
    delete_products = 6

    block_user = 7
    unblock_user = 8
    delete_user = 9
    get_users = 10

    get_products = 11
    get_recipes = 12


