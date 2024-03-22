from typing import List

from pydantic import BaseModel


class DataBaseModel(BaseModel):
    class Config:
        orm_mode = True


class SuccessData(DataBaseModel):
    success: bool


class UserDataIn(DataBaseModel):
    name: str
    surname: str
    email: str
    is_block: bool
    password: str


class RoleData(DataBaseModel):
    id: int
    name: str


class UserData(DataBaseModel):
    id: int
    name: str
    surname: str
    email: str
    is_block: bool
    roles: List[RoleData]


class TokenData(DataBaseModel):
    access_token: str
    refresh_token: str
    token_type: str


class LoginDataIn(DataBaseModel):
    email: str
    password: str

