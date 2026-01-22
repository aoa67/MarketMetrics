from app.models.simulation import SimulationRequest, SimulationResult


def run_simulation(req: SimulationRequest) -> SimulationResult:
    final_value = req.initialAmount
    profit = final_value - req.initialAmount
    total_return_pct = 0.0

    return SimulationResult(
        assetSymbol=req.assetSymbol,
        startDate=req.startDate,
        endDate=req.endDate,
        initialAmount=req.initialAmount,
        finalValue=final_value,
        profit=profit,
        totalReturnPct=total_return_pct,
    )
