import logging
import traceback

from fastapi import HTTPException
from sqlalchemy.orm import DeclarativeBase


class CrudService:
    def __init__(self, session, model):
        self.model = model
        self.session = session

    async def create_instance(self, kwargs):
        try:
            instance = self.model(**kwargs)
            self.session.add(instance)
            self.session.commit()
            return instance
        except Exception as error:
            self.session.rollback()
            logging.error(f'Error: {error}, traceback: {traceback.format_exc()}')
            raise HTTPException(400, 'Failed to create.')

    async def delete_instance(self, instance_id: int):
        if not (instance := self.session.query(self.model).get(id=instance_id)):
            raise HTTPException(404, f'Not found instance by id {instance_id}.')
        try:
            self.session.delete(instance)
            self.session.commit()
            return {'success': True}
        except Exception as error:
            self.session.rollback()
            logging.error(f'Error: {error}, traceback: {traceback.format_exc()}')
            raise HTTPException(400, f'Failed to delete by id {instance_id}.')

    async def update_instance(self, instance_id: int, **kwargs):
        if not (instance := self.session.query(self.model).filter(self.model.id == instance_id).one_or_none()):
            raise HTTPException(404, f'Not found instance by id {instance_id}.')
        try:
            for k, v in kwargs.items():
                setattr(instance, k, v)
                self.session.commit()
        except Exception as error:
            self.session.rollback()
            logging.error(f'Error: {error}, traceback: {traceback.format_exc()}')
            raise HTTPException(400, f'Failed to update instance by id {instance_id}.')

    async def get_instance_by_id(self, instance_id: int):
        if instance := self.session.query(self.model).filter(self.model.id == instance_id).one_or_none():
            return instance
        raise HTTPException(404, f'Not found instance by id {instance_id}.')

    async def get_all_instances(self):
        return self.session.query(self.model).all()

    async def get_or_create(self, model: DeclarativeBase, name: str):
        try:
            if instance := self.session.query(model).filter(model.name == name).one_or_none():
                return instance

        except Exception as error:
            self.session.rollback()
            logging.error(f'Error: {error}, traceback: {traceback.format_exc()}')
            raise HTTPException(400, f'Failed to create instance by name {name}.')
