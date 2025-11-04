from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import crud, schemas
from ..database import SessionLocal

router = APIRouter(prefix="/portfolio", tags=["Portfolio"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.PortfolioResponse)
def create_portfolio_item(
    portfolio_item: schemas.PortfolioCreate, 
    user_id: int, 
    db: Session = Depends(get_db)
):
    return crud.create_portfolio(db=db, portfolio=portfolio_item, user_id=user_id)

@router.get("/user/{user_id}", response_model=List[schemas.PortfolioResponse])
def read_user_portfolio(user_id: int, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    portfolio_items = crud.get_portfolios_by_user(db, user_id=user_id, skip=skip, limit=limit)
    if not portfolio_items:
        raise HTTPException(status_code=404, detail="No portfolio found for this user")
    return portfolio_items
