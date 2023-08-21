from app.controllers.crud_service import CrudService


class ProductService(CrudService):
    def __init__(self, session, model):
        super().__init__(session, model)
