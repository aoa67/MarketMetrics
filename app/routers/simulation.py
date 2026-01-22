from fastapi import APIRouter, Depends

from app.core.dependencies import get_current_user
from app.models.simulation import SimulationRequest, SimulationResult
from app.services.simulation_service import run_simulation

router = APIRouter(
    prefix="/simulate",
    tags=["Simulation"],
)


@router.post("/", response_model=SimulationResult)
def simulate(
    payload: SimulationRequest,
    user: dict = Depends(get_current_user),
):
    """
    Run an investment simulation for the authenticated user.
    """
    result = run_simulation(payload)
    return result
