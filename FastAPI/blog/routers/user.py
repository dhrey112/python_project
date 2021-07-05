from fastapi import  Depends, APIRouter
from .. import schemas, database
from sqlalchemy.orm import Session
from .. hashing import Hash
from .. repository import userRepo


router = APIRouter(
    prefix="/user",
    tags=["User"]
)

get_db = database.get_db

@router.post("/", response_model=schemas.ShowBlog)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return userRepo.create_user(request, db)

@router.get('/{id}', response_model=schemas.ShowUser)
def get_user(id: int, db: Session = Depends(get_db)):
    return userRepo.show_user(id, db)