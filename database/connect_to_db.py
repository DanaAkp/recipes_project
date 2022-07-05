




# region example
# db = DBConnect("sqlite:///test.db")
# product = Table('product', db.metadata,
#                 Column('id', Integer, primary_key=True),
#                 Column('name', String, nullable=False, unique=True))
# db.metadata.create_all(db.engine)
#
# db.connect.execute(insert(product), [
#     {'name': 'jenrfwi'},
#     {'name': 'kjnvwr'},
#     {'name': 'jenwefrvwerfwi'},
#     {'name': 'jeneverfwi'},
#     {'name': 'aacesrfqe'},
#     {'name': 'fvvvfvfv'}
# ])
# print(db.connect.execute(product.select()).fetchall())
#
# print(db.connect.execute(product.select().where(product.c.name == 'fvvvfvfv')).first())
# print(db.connect.execute(product.select().where(product.c.name == 'fvvvfvfv')).fetchone())
# endregion
