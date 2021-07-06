from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from .. import schemas, models, database
router = APIRouter(
    prefix="/login",
    tags=['Authentication']
)


@router.post('/')
def login(request: schemas.Login, db: Session = Depends(database.get_db)):
    user = db.query(models.)
    return login
    