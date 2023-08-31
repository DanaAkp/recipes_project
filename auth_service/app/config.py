import os

DATABASE_USER_NAME = os.environ.get('DATABASE_USER_NAME', 'postgres')
DATABASE_USER_PASSWORD = os.environ.get('DATABASE_USER_PASSWORD', 'postgres')
DATABASE_NAME = os.environ.get('DATABASE_NAME_AUTH', 'recipes')
DATABASE_PORT = int(os.environ.get('DATABASE_PORT', 5432))
DATABASE_HOST = os.environ.get('DATABASE_HOST', 'localhost')
DATABASE_URL = f"postgresql://" \
               f"{DATABASE_USER_NAME}:{DATABASE_USER_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"

ADMIN_USER_LOGIN = os.environ.get('ADMIN_USER_LOGIN', 'admin')
ADMIN_USER_PASSWORD = os.environ.get('ADMIN_USER_LOGIN', 'admin')

JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY', 'secret')
ALGORITHM = os.environ.get('ALGORITHM', 'HS256')
ACCESS_TOKEN_EXPIRE_MINUTES = 45
REFRESH_TOKEN_EXPIRE_HOURS = 10
