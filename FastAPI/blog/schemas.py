from pydantic import BaseModel


class Blog(BaseModel):
    title: str
    body: str

class show_blog(BaseModel):
    title: str
    body: str

    class Config():
        orm_mode = True


class User(BaseModel):
    username: str
    email: str
    password: str

class show_user(BaseModel):
    username: str
    email: str

    class Config():
        orm_mode = True