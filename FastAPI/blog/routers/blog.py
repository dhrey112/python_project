from fastapi import status, Response, HTTPException, Depends, APIRouter
from .. import schemas, models, database
from sqlalchemy.orm import Session
from typing import List


router = APIRouter()

get_db = database.get_db

@router.post('/blog/', status_code=status.HTTP_201_CREATED, tags=['blogs'])
def create(request: schemas.Blog, db: Session = Depends(get_db)):
    new_blog = models.Blog(title=request.title, body=request.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@router.delete('/blog/{id}', status_code=status.HTTP_204_NO_CONTENT, tags=['blogs'])
def destroy(id, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, message=f"Blog with id {id} not found")    
    
    blog.delete(synchronize_session=False)
    # db.query(models.Blog).filter(models.Blog.id == id).delete(synchronize_session=False)
    db.commit()
    return "Blog post removed successfully"



@router.put('/blog/{id}', status_code=status.HTTP_202_ACCEPTED, tags=['blogs'])
def update(id, request: schemas.Blog, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, message=f"Blog with id {id} not found")
        
    blog.update(request)
    db.commit()
    return "Blog updated successfully"


@router.get('/blog/', response_model=List[schemas.ShowBlog], tags=['blogs'])
def all(db: Session = Depends(get_db)):
    blogs = db.query(Blog).all()
    return blogs


@router.get('/blog/{id}', status.HTTP_200_OK, response_model=schemas.ShowBlog, tags=['blogs'])
def show(id, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with the id {id} is not available")
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return{"details": f"Blog with the id {id} is not available"}
    return blog
