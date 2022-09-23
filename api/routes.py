import os

from datetime import datetime, timedelta

from typing import List, Optional

from fastapi import Depends, FastAPI, HTTPException, UploadFile, status
from fastapi.responses import FileResponse, RedirectResponse
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from .db import crud, models, schemas
from .db.database import SessionLocal, engine

from passlib.context import CryptContext
from jose import JWTError, jwt

from dotenv import load_dotenv

from . import responses

def setup_routes(app: FastAPI) -> None:
    load_dotenv()

    SECRET_KEY = os.environ.get("SECRET_KEY")
    ALGORITHM = os.environ.get("ALGORITHM")
    ACCESS_TOKEN_EXPIRE_MINUTES = int(os.environ.get("ACCESS_TOKEN_EXPIRE_MINUTES"))

    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/token")

    # Dependencies
    def get_db():
        db = SessionLocal()
        try:
            yield db
        finally:
            db.close()

    def verify_password(plain_password, hashed_password):
        return pwd_context.verify(plain_password, hashed_password)

    def get_password_hash(password):
        return pwd_context.hash(password)

    def authenticate_user(username: str, password: str, db: Session = Depends(get_db)):
        user = crud.get_user_by_username(db, username=username)
        if not user:
            return False
        if not verify_password(password, user.hashed_password):
            return False
        return user

    def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=15)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt

    async def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            username: str = payload.get("sub")
            if username is None:
                raise credentials_exception
            token_data = schemas.TokenData(username=username)
        except JWTError:
            raise credentials_exception
        user = crud.get_user_by_username(db, username=token_data.username)
        if user is None:
            raise credentials_exception
        return user

    @app.post("/api/token", response_model=schemas.Token, responses={**responses.UNAUTORIZED},tags=["auth"])
    async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
        user = authenticate_user(form_data.username, form_data.password, db)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
                headers={"WWW-Authenticate": "Bearer"},
            )
        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(
            data={"sub": user.username}, expires_delta=access_token_expires
        )
        return {"access_token": access_token, "token_type": "bearer"}

    @app.post("/api/users/", response_model=schemas.User, responses={**responses.USER_ALREADY_REGISTERED}, tags=["users"])
    def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
        db_user = crud.get_user_by_username(db, username=user.username)
        if db_user:
            raise HTTPException(status_code=400, detail="Username already registered")
        user.password = get_password_hash(user.password)
        return crud.create_user(db=db, user=user)


    @app.get("/api/users/", response_model=List[schemas.User], tags=["users"])
    def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
        users = crud.get_users(db, skip=skip, limit=limit)
        return users

    @app.get("/api/users/me", response_model=schemas.User, responses={**responses.UNAUTORIZED}, tags=["users"])
    async def read_current_user(current_user: schemas.User = Depends(get_current_user)):
        return current_user

    @app.put("/api/users/me", response_model=schemas.User, responses={**responses.UNAUTORIZED}, tags=["users"])
    async def update_user_info(user: schemas.UserUpdate, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
        crud.update_user(db, user, current_user)
