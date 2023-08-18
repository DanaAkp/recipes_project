import sqlalchemy as db
from sqlalchemy.orm import DeclarativeBase

from app.config import DATABASE_URL

engine = db.create_engine(DATABASE_URL)
metadata = db.schema.MetaData()


class Base(DeclarativeBase):
    pass
