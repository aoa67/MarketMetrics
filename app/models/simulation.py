from pydantic import BaseModel, Field
from typing import Optional


class SimulationRequest(BaseModel):
    assetSymbol: str = Field(..., example="AAPL")
    initialAmount: float = Field(..., gt=0, example=1000.0)
    startDate: str = Field(..., example="2023-01-01")
    endDate: str = Field(..., example="2023-12-31")
    strategy: str = Field("buy_and_hold", example="buy_and_hold")
    frequency: Optional[str] = Field("daily", example="daily")


class SimulationResult(BaseModel):
    assetSymbol: str
    initialAmount: float
    finalValue: float
    totalReturnPct: float
    maxDrawdownPct: float
