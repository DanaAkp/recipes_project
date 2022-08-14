import logging
import traceback
from typing import List

from sqlalchemy import table, select, insert, and_, delete


def providing_sql(func):
    def wrapper_func(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except Exception as error:
            logging.error(f'Error: {error}, traceback: {traceback.format_exc()}')

    return wrapper_func


class DBService:
    def __init__(self, connect):
        self.connect = connect

    def get_all(self, entity: table):
        return self.connect.execute(entity.select()).fetchall()

    def get_or_create(self, filters, entity: table):
        pass

    def add(self, values: dict, entity: table) -> int:
        ins = entity.insert().values(values)
        r = self.connect.execute(ins)
        return r.rowcount

    def add_from_list(self, values: List[dict], entity: table) -> int:
        r = self.connect.execute(insert(entity), values)
        return r.rowcount

    def get_by_filters(self, entity: table, filters):
        s = select([entity]).where(and_(**filters))
        r = self.connect.execute(s)
        return r.fetchall()

    def remove_item(self, entity: table, filters: dict):
        d = delete(entity).where(**filters)
        r = self.connect.execute(d)
        return r.rowcount
