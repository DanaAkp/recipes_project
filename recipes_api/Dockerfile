FROM req:latest

WORKDIR /recipes_api

COPY recipes_api/app ./app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]