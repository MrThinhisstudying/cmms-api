from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, crud, database
from app import auth, users
from app.database import engine
from app import models
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/equipment/", response_model=schemas.Equipment)
def create_equipment(equipment: schemas.EquipmentCreate, db: Session = Depends(get_db)):
    return crud.create_equipment(db=db, equipment=equipment)

@app.get("/equipment/", response_model=list[schemas.Equipment])
def read_equipments(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_equipments(db=db, skip=skip, limit=limit)

@app.get("/equipment/{equipment_id}", response_model=schemas.Equipment)
def read_equipment(equipment_id: int, db: Session = Depends(get_db)):
    db_equipment = crud.get_equipment(db, equipment_id=equipment_id)
    if db_equipment is None:
        raise HTTPException(status_code=404, detail="Equipment not found")
    return db_equipment
app.include_router(auth.router)
app.include_router(users.router)