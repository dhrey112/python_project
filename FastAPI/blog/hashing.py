from passlib.context import CryptContext

pwd_cxt = CryptContext(schemas=["bcrypt"], deprecated="auto")

class Hash():
    def __init__(self, password: str):
        self.password = password

    def bcrypt(self):
        return pwd_cxt.hash(self.password)