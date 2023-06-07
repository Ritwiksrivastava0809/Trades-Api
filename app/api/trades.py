from fastapi import APIRouter, HTTPException
from typing import List, Optional
from datetime import datetime

from app.models.trade import Trade, TradeCreate

router = APIRouter()


trades = []  # Temporary list to store trades


@router.post("/", response_model=Trade)
def create_trade(trade: TradeCreate):
    trade_id = len(trades) + 1
    trade_data = trade.dict()
    trade_data["trade_id"] = trade_id
    trade_data["trade_datetime"] = datetime.now()
    trades.append(trade_data)
    return trade_data


@router.get("/", response_model=List[Trade])
def get_trades():
    return trades


@router.get("/search", response_model=List[Trade])
def search_trades(
    search: Optional[str] = None,
    asset_class: Optional[str] = None,
    start: Optional[datetime] = None,
    end: Optional[datetime] = None,
    min_price: Optional[float] = None,
    max_price: Optional[float] = None,
    trade_type: Optional[str] = None
):
    filtered_trades = trades

    if search:
        filtered_trades = [
            trade for trade in filtered_trades if search.lower() in str(trade).lower()
        ]

    if asset_class:
        filtered_trades = [
            trade for trade in filtered_trades if trade.get("asset_class") == asset_class
        ]

    if start:
        filtered_trades = [
            trade for trade in filtered_trades if trade.get("trade_datetime") >= start
        ]

    if end:
        filtered_trades = [
            trade for trade in filtered_trades if trade.get("trade_datetime") <= end
        ]

    if min_price:
        filtered_trades = [
            trade for trade in filtered_trades if trade.get("price") >= min_price
        ]

    if max_price:
        filtered_trades = [
            trade for trade in filtered_trades if trade.get("price") <= max_price
        ]

    if trade_type:
        filtered_trades = [
            trade for trade in filtered_trades if trade.get("buy_sell_indicator") == trade_type
        ]

    return filtered_trades
