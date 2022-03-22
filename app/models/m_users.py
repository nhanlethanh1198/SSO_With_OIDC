from datetime import datetime
from sqlalchemy import String, Integer, DateTime, Column, ForeignKey
from app.databases import Base
from typing import Optional

# User table
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False, index=True)
    fullname = Column(String, nullable=False)
    email = Column(String, nullable=True)
    password = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.now())
    updated_at = Column(DateTime, nullable=False, default=datetime.now())
    
    @classmethod
    async def get_by_email(cls, email:str):
        return cls.query.filter_by(email=email).first()
    
    
    async def get_by_user_id(cls, user_id):
        return cls.query.filter_by(id=user_id).first()
    
    
    async def user_login(cls, email: str, password: str):
        return cls.query.filter_by(email=email, password=password).first()
    
    
    async def check_user_exists(self, email: str):
        return self.query.filter_by(email=email).first()
    
    
    async def register_new_user(self, email: str, password: str, fullname: str):
        self.email = email
        self.password = password
        self.fullname = fullname
        
        return await self.save()