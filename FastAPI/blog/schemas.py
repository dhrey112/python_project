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
    