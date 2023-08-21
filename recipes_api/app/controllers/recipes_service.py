import logging
import traceback
from typing import List, Optional

from fastapi import HTTPException

from app.models.recipe import Recipe, RecipeProduct
from app.controllers.crud_service import CrudService


class RecipeService(CrudService):
    def __init__(self, session, model):
        super().__init__(session=session, model=model)

    async def add_products_to_recipes(self, recipe_id: int, products: List[dict]) -> Optional[Recipe]:
        if not (recipe := self.session.query(Recipe).one_or_none()):
            raise HTTPException(404, f'Not found recipe by id {recipe_id}.')
        instances = []
        for product in products:
            product_id = self.get_or_create(product.get('product_name'))
            instances.append(
                RecipeProduct(
                    recipe_id=recipe_id,
                    product_id=product_id,
                    amount=product.get('amount')
                )
            )
        try:
            self.session.add_all(instances)
            self.session.flush()
        except Exception as error:
            self.session.rollback()
            logging.error(f'Error: {error}, traceback: {traceback.format_exc()}')
            raise HTTPException(400, 'Failed to add products to recipe.')
        self.session.commit()
        return recipe

    async def delete_product_from_recipe(self, recipe_id: int, product_id: int) -> dict:
        if not self.session.query(Recipe).one_or_none():
            raise HTTPException(404, f'Not found recipe by id {recipe_id}.')

        if not (recipe_product := self.session.query(RecipeProduct)
                .filter(RecipeProduct.product_id == product_id)
                .filter(RecipeProduct.recipe_id == recipe_id).one_or_none()):
            raise HTTPException(404, f'Not found product by id {product_id} in this recipe.')
        try:
            self.session.delete(recipe_product)
            self.session.commit()
        except Exception as error:
            self.session.rollback()
            logging.error(f'Error: {error}, traceback: {traceback.format_exc()}')
            raise HTTPException(400, 'Failed to add products to recipe.')
        return {'success': True}

    async def change_amount_product(self, recipe_id: int, product_id: int, amount: float) -> Optional[Recipe]:
        if not (recipe := self.session.query(Recipe).one_or_none()):
            raise HTTPException(404, f'Not found recipe by id {recipe_id}.')

        if not (recipe_product := self.session.query(RecipeProduct)
                .filter(RecipeProduct.product_id == product_id)
                .filter(RecipeProduct.recipe_id == recipe_id).one_or_none()):
            raise HTTPException(404, f'Not found product by id {product_id} in this recipe.')
        try:
            recipe_product.amount = amount
            self.session.commit()
        except Exception as error:
            self.session.rollback()
            logging.error(f'Error: {error}, traceback: {traceback.format_exc()}')
            raise HTTPException(400, 'Failed to add products to recipe.')
        return recipe
