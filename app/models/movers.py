from typing import List, Optional
from pydantic import BaseModel


class Mover(BaseModel):
    symbol: str
    name: Optional[str] = None
    price: Optional[float] = None
    change_amount: Optional[float] = None
    change_percent: Optional[str] = None
    volume: Optional[int] = None


class MoversResponse(BaseModel):
    gainers: List[Mover]
    losers: List[Mover]
    source: str = "alpha_vantage"
