import sqlalchemy
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine
from fastapi import FastAPI

app = FastAPI()


@app.on_event("startup")
async def startup_event():
    pass


class DBConnect:
    def __init__(self, db_url: str):
        self.engine = create_engine(db_url, echo=True, future=True)
        self.metadata = sqlalchemy.schema.MetaData()
        self.Base = declarative_base(bind=self.engine)
        self.connect = self.engine.connect()
        session = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
        self.session = session()


db = DBConnect("sqlite:///test.db")

from database.models import *
db.metadata.create_all(bind=db.engine)
