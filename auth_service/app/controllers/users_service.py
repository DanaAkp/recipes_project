import logging
import traceback
from datetime import datetime, timedelta
from typing import Optional, Union

from jose import JWTError, jwt
from fastapi import HTTPException
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from sqlalchemy.orm import Session

from app import config
from app.constants import PermissionsNames
from app.controllers.access_service import PermissionService
from app.models.users import User


class UserService:
    NOT_FOUND_ERROR_MASSAGE = 'Not found user by id {}'
    SECRET_KEY = config.JWT_SECRET_KEY
    ALGORITHM = config.ALGORITHM
    ACCESS_TOKEN_EXPIRE_MINUTES = config.ACCESS_TOKEN_EXPIRE_MINUTES
    REFRESH_TOKEN_EXPIRE_HOURS = config.REFRESH_TOKEN_EXPIRE_HOURS

    pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
    oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')

    def __init__(self, session: Session, permission_service: PermissionService):
        self.session = session
        self.permission_service = permission_service

    async def get_password_hash(self, password: str) -> str:
        return self.pwd_context.hash(password)

    async def verify_password(self, plain_password, hashed_password):
        return self.pwd_context.verify(plain_password, hashed_password)

    async def create_user(self, email: str, name: str, surname: str, password: str, current_user: User) -> Optional[User]:
        try:
            user = User(
                email=email,
                name=name,
                surname=surname,
                hash_password=await self.get_password_hash(password)
            )
            self.session.add(user)
            self.session.commit()
            return user
        except Exception as error:
            self.session.rollback()
            logging.error(f'Error: {error}, traceback: {traceback.format_exc()}')
            raise HTTPException(400, 'Failed to create user.')

    async def block_user(self, user_id: int, current_user: User) -> dict:
        raise NotImplementedError('Method not implemented.')

    async def unblock_user(self, user_id: int, current_user: User) -> dict:
        raise NotImplementedError('Method not implemented.')

    async def edit_user(self, user_id: int, email: str, name: str, surname: str, password: str, current_user: User) -> Optional[User]:
        if not (user := self.session.query(User).filter(User.id == user_id).one_or_none()):
            raise HTTPException(404, self.NOT_FOUND_ERROR_MASSAGE.format(user_id))
        try:
            user.email = email
            user.name = name
            user.surname = surname
            user.surname = await self.get_password_hash(password)
            self.session.commit()
            return user
        except Exception as error:
            self.session.rollback()
            logging.error(f'Error: {error}, traceback: {traceback.format_exc()}')
            raise HTTPException(400, 'Failed to create user.')

    async def logout(self, user_id: Union[str, int]) -> dict:
        raise NotImplementedError('Method not implemented.')

    async def login(self, email: str, password: str) -> dict:
        user = self.session.query(User).filter(User.email == email).one_or_none()
        if not (user and await self.verify_password(password, user.hash_password)):
            raise HTTPException(400, 'Invalid login data.')

        access_token = self.create_access_token(user.id)
        refresh_token = self.create_refresh_token(user.id)
        return {'access_token': access_token, 'refresh_token': refresh_token,
                'token_type': 'bearer'}

    async def create_access_token(self, user_id: Union[int, str]) -> str:
        user = self.session.query(User).filter(User.id == int(user_id)).one_or_none()
        to_encode = {
            'user_id': str(user.id),
            'role_id': str(user.role.id),
            'full_name': f'{user.name} {user.surname}',
            'scope': 'access_token',
            'exp': datetime.utcnow() + timedelta(minutes=self.ACCESS_TOKEN_EXPIRE_MINUTES)
        }
        encoded_jwt = jwt.encode(to_encode, self.SECRET_KEY, algorithm=self.ALGORITHM)
        return encoded_jwt

    async def create_refresh_token(self, user_id: int) -> str:
        to_encode = {
            'user_id': str(user_id),
            'scope': 'refresh_token',
            'exp': datetime.utcnow() + timedelta(hours=self.REFRESH_TOKEN_EXPIRE_HOURS)
        }
        encoded_jwt = jwt.encode(to_encode, self.SECRET_KEY, algorithm=self.ALGORITHM)
        return encoded_jwt

    async def get_current_user(self, access_token: str) -> Optional[User]:
        try:
            payload = jwt.decode(access_token, self.SECRET_KEY, algorithms=self.ALGORITHM)
            if payload.get('scope') == 'access_token':
                return payload.get('user_id')
            raise JWTError()
        except jwt.ExpiredSignatureError:
            raise HTTPException(400, 'Your access token is expired.')
        except JWTError:
            raise HTTPException(401, 'Invalid access token.')

    async def refresh(self, refresh_token: str) -> dict:
        try:
            payload = jwt.decode(refresh_token, self.SECRET_KEY, algorithms=self.ALGORITHM)
            if payload.get('scope') == 'refresh_token':
                access_token = self.create_access_token(payload.get('user_id'))
                return {'access_token': access_token}
            raise JWTError()
        except jwt.ExpiredSignatureError:
            raise HTTPException(400, 'Your refresh token is expired.')
        except JWTError:
            raise HTTPException(401, 'Invalid refresh token.')

    async def get_all_users(self) -> list:
        raise NotImplementedError('Method not implemented.')

    async def get_user_by_id(self, user_id: Union[int, str]) -> User:
        raise NotImplementedError('Method not implemented.')

