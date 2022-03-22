import hashlib

from app.databases import get_db
from app.schemas import s_users as schema_s_users
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models import m_users as model_m_users

router = APIRouter(
    prefix='/users',
    tags=['USERS']
)

@router.post('/login', summary='User login')
async def login(request: schema_s_users.UserLoginRequest, db: Session = Depends(get_db)):
   return True
    

@router.post('/register', summary='User register')
async def register(request: schema_s_users.UserRegisterRequest, db: Session = Depends(get_db)):
    # Check user already registered
    check_user_exists = await model_m_users.Users.check_user_exists(request.email)
    new_user = await model_m_users.User.register_new_user(request.email, request.password, request.fullname)
    
    db.add(new_user)
    db.commit()
    return new_user
