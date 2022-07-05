from fastapi import FastAPI

from database.connect_to_db import DBConnect

app = FastAPI()


@app.on_event("startup")
async def startup_event():
    pass

db = DBConnect("sqlite:///test.db")

db.metadata.create_all(bind=db.engine)

