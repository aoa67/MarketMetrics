from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import health, simulation, movers

app = FastAPI(title="Market Metrics API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health.router, tags=["Health"])
app.include_router(simulation.router, prefix="/simulate", tags=["Simulation"])

app.include_router(movers.router, prefix="/movers", tags=["Movers"])
