from sqlalchemy.orm import Session
from . import models, schemas

def get_equipment(db: Session, equipment_id: int):
    return db.query(models.Equipment).filter(models.Equipment.id == equipment_id).first()

def get_equipments(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Equipment).offset(skip).limit(limit).all()

def create_equipment(db: Session, equipment: schemas.EquipmentCreate):
    db_equipment = models.Equipment(**equipment.dict())
    db.add(db_equipment)
    db.commit()
    db.refresh(db_equipment)
    return db_equipment
