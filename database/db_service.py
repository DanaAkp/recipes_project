import logging
import traceback


def providing_sql(func):
    def wrapper_func(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except Exception as error:
            logging.error(f'Error: {error}, traceback: {traceback.format_exc()}')

    return wrapper_func


class DBService:
    @classmethod
    @providing_sql
    def get_or_create_by_unique(cls, entity, **fields):
        pass

    @classmethod
    @providing_sql
    def get_by_filter(cls, entity, **fields):
        pass
