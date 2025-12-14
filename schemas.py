from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    password: str

class SweetCreate(BaseModel):
    name: str
    category: str
    price: float
    quantity: int

class Sweet(SweetCreate):
    id: int
    class Config:
        from_attributes = True