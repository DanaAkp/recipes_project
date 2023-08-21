from fastapi import FastAPI
from sqlalchemy.orm.session import sessionmaker

from app.models import engine, metadata
from app.dependencies import container

app = FastAPI(title='RecipesAPI')

metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)

container.wire(modules=["app.routers"])
container.config.session.from_value(Session())

from app.routers import product_router, recipe_router  # noqa


app.include_router(product_router)
app.include_router(recipe_router)
