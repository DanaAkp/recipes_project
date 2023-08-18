from app.models.recipe import Recipe, RecipeProduct
from app.controllers.crud_service import CrudService


class RecipeService(CrudService):
    def __init__(self, session, model):
        super().__init__(session=session, model=model)

    async def add_product_recipes(self, recipe_id: int, product_id: int):
        pass

    async def delete_product_from_recipe(self, recipe_id: int, product_id: int):
        pass

    async def change_amount_product(self, recipe_id: int, product_id: int, amount: float):
        pass
