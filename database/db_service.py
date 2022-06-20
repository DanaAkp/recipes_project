import logging
import traceback


def providing_sql(func):
    def wrapper_func(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except Exception as error:
            logging.error(f'Error: {error}, traceback: {traceback.format_exc()}')
    return wrapper_func
