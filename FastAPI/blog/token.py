from datetime import datetime, timedelta
from jose import jwt, JWTError
import token
from . import schemas


ACCESS_TIME_EXPIRE_MINUTES = 30
SECRET_KEY = ""
ALGORITHM = "HS256"


def create(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(ACCESS_TIME_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt

def verify_token(token: str, credentials_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithm=ALGORITHM)
        email: str = payload.get("sub")
        
        if email is None:
            raise credentials_exception
            token_data = schemas.TokenData(email=email)

    except JWTError:
        raise credentials_exception
