from datetime import datetime
from typing import List, Optional

from pydantic.main import BaseModel


class UserLoginRequest(BaseModel):
    email: str
    password: str
    
    
class UserRegisterRequest(BaseModel):
    fullname: str
    email: str
    password: str
    