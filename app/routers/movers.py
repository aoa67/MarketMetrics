from __future__ import annotations

from typing import Any, Dict, List

from fastapi import APIRouter, HTTPException

from app.models.movers import Mover, MoversResponse
from app.services.alpha_vantage import AlphaVantageError, fetch_top_movers

router = APIRouter()


def _to_float(value: Any) -> float:
    try:
        return float(value)
    except Exception:
        return None  # type: ignore


def _to_int(value: Any) -> int:
    try:
        return int(float(value))
    except Exception:
        return None  # type: ignore


def _parse_movers(items: List[Dict[str, Any]]) -> List[Mover]:
    result: List[Mover] = []
    for item in items:
        result.append(
            Mover(
                symbol=item.get("ticker") or item.get("symbol") or "",
                name=item.get("name"),
                price=_to_float(item.get("price")),
                change_amount=_to_float(item.get("change_amount")),
                change_percent=item.get("change_percentage") or item.get("change_percent"),
                volume=_to_int(item.get("volume")),
            )
        )
    # Filter out any empty symbols
    return [m for m in result if m.symbol]


@router.get("/movers", response_model=MoversResponse, tags=["Movers"])
async def get_movers():
    try:
        data = await fetch_top_movers()
        gainers_raw = data.get("top_gainers") or []
        losers_raw = data.get("top_losers") or []
        return MoversResponse(
            gainers=_parse_movers(gainers_raw),
            losers=_parse_movers(losers_raw),
        )
    except AlphaVantageError as e:
        raise HTTPException(status_code=502, detail=f"Alpha Vantage error: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Server error: {str(e)}")
from fastapi import APIRouter, HTTPException
from app.models.movers import MoversResponse, Mover
from app.services.market_data_service import get_top_movers_alpha_vantage

router = APIRouter()

@router.get("/", response_model=MoversResponse)
def movers():
    try:
        data = get_top_movers_alpha_vantage()

        # Alpha Vantage typically returns keys like "top_gainers" / "top_losers"
        top_gainers = data.get("top_gainers", [])
        top_losers = data.get("top_losers", [])

        gainers = [
            Mover(
                symbol=item.get("ticker"),
                price=float(item["price"]) if item.get("price") else None,
                change=float(item["change_amount"]) if item.get("change_amount") else None,
                changePercent=float(item["change_percentage"].replace("%", "")) if item.get("change_percentage") else None,
            )
            for item in top_gainers
        ]

        losers = [
            Mover(
                symbol=item.get("ticker"),
                price=float(item["price"]) if item.get("price") else None,
                change=float(item["change_amount"]) if item.get("change_amount") else None,
                changePercent=float(item["change_percentage"].replace("%", "")) if item.get("change_percentage") else None,
            )
            for item in top_losers
        ]

        return MoversResponse(gainers=gainers, losers=losers, source="alpha_vantage")

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

