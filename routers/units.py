from fastapi import Depends, APIRouter
from database import get_db
from sqlalchemy.orm import Session
from models_original import Unit

router = APIRouter(prefix="/units", tags=["Units"])

@router.get("/")
def get_all_units(db: Session = Depends(get_db)):
    return db.query(Unit).all()

@router.get("/{faction}")
def get_faction_units(faction: str, db: Session = Depends(get_db)):
    return db.query(Unit).filter(Unit.faction == faction).all()