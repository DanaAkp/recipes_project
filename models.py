import sqlalchemy
import databases
from sqlalchemy import Table, Column, Integer, String

DATABASE_URL = "sqlite:///test.db"

# database = databases.Database(DATABASE_URL)

metadata = sqlalchemy.MetaData()

product = Table(
    "product",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String),
    Column("calories", Integer),
)


engine = sqlalchemy.create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)


metadata.create_all(engine)

print(product.query.all())
