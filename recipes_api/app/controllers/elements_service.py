from app.controllers.crud_service import CrudService


class ElementService(CrudService):
    def __init__(self, session):
        super().__init__(session)
