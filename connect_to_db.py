from typing import List

import sqlalchemy
from sqlalchemy import Column, Table, insert, table
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine


class DBConnect:
    def __init__(self, db_url: str):
        self.engine = create_engine(db_url, echo=True, future=True)
        self.metadata = sqlalchemy.schema.MetaData()
        self.metadata.create_all(bind=self.engine)
        self.Base = declarative_base(bind=self.engine)
        self.connect = self.engine.connect()

    def get_all(self, entity: table):
        return self.connect.execute(entity.select()).fetchall()

    def add(self, values: dict, entity: table) -> int:
        ins = entity.insert().values(values)
        r = self.connect.execute(ins)
        return r.rowcount

    def add_from_list(self, values: List[dict], entity: table) -> int:
        r = self.connect.execute(insert(entity), values)
        return r.rowcount


# region example
db = DBConnect("sqlite:///test.db")
product = Table('product', db.metadata,
                Column('id', Integer, primary_key=True),
                Column('name', String, nullable=False, unique=True))
db.metadata.create_all(db.engine)

db.connect.execute(insert(product), [
    {'name': 'jenrfwi'},
    {'name': 'kjnvwr'},
    {'name': 'jenwefrvwerfwi'},
    {'name': 'jeneverfwi'},
    {'name': 'aacesrfqe'},
    {'name': 'fvvvfvfv'}
])
print(db.connect.execute(product.select()).fetchall())

print(db.connect.execute(product.select().where(product.c.name == 'fvvvfvfv')).first())
print(db.connect.execute(product.select().where(product.c.name == 'fvvvfvfv')).fetchone())
# endregion
