from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
from typing import List
import models, schemas, auth, database

app = FastAPI()

# Allow Frontend to talk to Backend
app.add_middleware(
    CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"],
)

models.Base.metadata.create_all(bind=database.engine)

@app.post("/api/auth/register")
def register(user: schemas.UserCreate, db: Session = Depends(database.get_db)):
    hashed_pw = auth.get_password_hash(user.password)
    new_user = models.User(username=user.username, hashed_password=hashed_pw, is_admin=True)
    db.add(new_user)
    db.commit()
    return {"msg": "User created"}

@app.post("/api/auth/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.username == form_data.username).first()
    if not user or not auth.verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Incorrect login")
    token = auth.create_access_token(data={"sub": user.username})
    return {"access_token": token, "token_type": "bearer"}

@app.get("/api/sweets/search", response_model=List[schemas.Sweet])
def search_sweets(q: str = "", db: Session = Depends(database.get_db)):
    return db.query(models.Sweet).filter(models.Sweet.name.contains(q)).all()

@app.post("/api/sweets")
def add_sweet(sweet: schemas.SweetCreate, user: models.User = Depends(auth.get_current_user), db: Session = Depends(database.get_db)):
    db_sweet = models.Sweet(**sweet.dict())
    db.add(db_sweet)
    db.commit()
    return db_sweet

@app.post("/api/sweets/{id}/purchase")
def purchase(id: int, user: models.User = Depends(auth.get_current_user), db: Session = Depends(database.get_db)):
    sweet = db.query(models.Sweet).filter(models.Sweet.id == id).first()
    if not sweet or sweet.quantity < 1:
        raise HTTPException(status_code=400, detail="Out of stock")
    sweet.quantity -= 1
    db.commit()
    return {"msg": "Purchased"}