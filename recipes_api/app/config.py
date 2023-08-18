import os

DATABASE_USER_NAME = os.environ.get('DATABASE_USER_NAME', 'postgres')
DATABASE_USER_PASSWORD = os.environ.get('DATABASE_USER_PASSWORD', 'postgres')
DATABASE_NAME = os.environ.get('DATABASE_NAME', 'recipes')
DATABASE_PORT = int(os.environ.get('DATABASE_PORT', 5433))
DATABASE_HOST = os.environ.get('DATABASE_HOST', 'localhost')
DATABASE_URL = f"postgresql://" \
               f"{DATABASE_USER_NAME}:{DATABASE_USER_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"

JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY', 'secret')
ALGORITHM = os.environ.get('ALGORITHM', 'HS256')
