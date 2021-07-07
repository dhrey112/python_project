from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from .. import schemas, models, database, token
from ..hashing import Hash

router = APIRouter(
    prefix="/login",
    tags=['Authentication']
)


@router.post('/')
def login(request: OAuth2PasswordRequestForm - Depends(), db: Session = Depends(database.get_db)):
    user = db.query(models.User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid User credential")
    
    if not Hash.verify(user.password, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid User password")

    # generate a jwt token
    access_token = token.create_access_token(data={"sub": user.email})

    return {"access_token": access_token, "token_type": "bearer"}
    