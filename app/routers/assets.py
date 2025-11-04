from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, schemas, models
from ..database import SessionLocal

router = APIRouter(prefix="/assets", tags=["Assets"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.AssetResponse)
def create_asset(asset: schemas.AssetCreate, db: Session = Depends(get_db)):
    db_asset = crud.get_asset_by_ticker(db, ticker=asset.ticker)
    if db_asset:
        raise HTTPException(status_code=400, detail="Ticker already exists")
    return crud.create_asset(db=db, asset=asset)

@router.get("/", response_model=list[schemas.AssetResponse])
def read_assets(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_assets(db, skip=skip, limit=limit)
