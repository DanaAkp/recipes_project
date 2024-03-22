FROM python_container

WORKDIR /auth_service

COPY auth_service/app ./app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "5001"]