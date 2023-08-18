from fastapi import HTTPException
from jose import jwt, JWTError, ExpiredSignatureError

from config import JWT_SECRET_KEY, ALGORITHM


async def decode_jwt(token):
    try:
        payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=[ALGORITHM])
        if not (username := payload.get("username")):
            raise JWTError()

        return username  # todo
    except ExpiredSignatureError:
        raise HTTPException(400, 'Token is expired.')
    except JWTError:
        raise HTTPException(400, 'Invalid token.')
