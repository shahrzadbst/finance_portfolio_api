from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from .database import Base
import datetime

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)

    portfolios = relationship("Portfolio", back_populates="owner")

class Asset(Base):
    __tablename__ = "assets"

    id = Column(Integer, primary_key=True, index=True)
    ticker = Column(String, unique=True, index=True, nullable=False)  # e.g. AAPL, VOO
    name = Column(String, nullable=False)  # e.g. Apple Inc, Vanguard S&P 500 ETF
    type = Column(String, nullable=False)  # "stock" or "ETF"
    sector = Column(String, nullable=True)

    portfolios = relationship("Portfolio", back_populates="asset")

class Portfolio(Base):
    __tablename__ = "portfolios"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    asset_id = Column(Integer, ForeignKey("assets.id"), nullable=False)
    quantity = Column(Float, nullable=False)
    purchase_price = Column(Float, nullable=False)
    purchase_date = Column(DateTime, default=datetime.datetime.utcnow)

    owner = relationship("User", back_populates="portfolios")
    asset = relationship("Asset", back_populates="portfolios")
