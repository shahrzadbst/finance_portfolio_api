from pydantic import BaseModel
from typing import Optional, List
import datetime


# ---------- User ----------
class UserBase(BaseModel):
    username: str


class UserCreate(UserBase):
    password: str


class UserResponse(UserBase):
    id: int

    class Config:
        orm_mode = True


# ---------- Asset ----------
class AssetBase(BaseModel):
    ticker: str
    name: str
    type: str   # stock or ETF
    sector: Optional[str]


class AssetCreate(AssetBase):
    pass


class AssetResponse(AssetBase):
    id: int

    class Config:
        orm_mode = True


# ---------- Portfolio ----------
class PortfolioBase(BaseModel):
    asset_id: int
    quantity: float
    purchase_price: float


class PortfolioCreate(PortfolioBase):
    pass


class PortfolioResponse(PortfolioBase):
    id: int
    purchase_date: datetime.datetime
    asset: AssetResponse

    class Config:
        orm_mode = True
