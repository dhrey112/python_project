from fastapi import FastAPI
from fastapi.params import Depends
from . import schemas, models
from .database import *
from sqlalchemy.orm import Session
from .models import Blog

app = FastAPI()

models.Base.metadata.create_all(engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post('/blog/')
def create(request: schemas.Blog, db: Session = Depends(get_db)):
    new_blog = Blog(title=request.title, body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@app.get('/blog/')
def all(db: Session = Depends(get_db)):
    blogs = db.query(Blog).all()
    return blogs