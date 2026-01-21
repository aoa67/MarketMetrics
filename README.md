# MarketMetrics

MarketMetrics is a FastAPI-based backend service that provides financial market insights, including investment simulations and real-time top gainers and losers data. The API integrates with the Alpha Vantage API to fetch market data and exposes clean, documented endpoints for use in web or mobile applications.

## Features
- Health check endpoint for service monitoring
- Investment simulation endpoint for analysing hypothetical returns
- Market movers endpoint showing top gainers and losers
- Clean modular architecture (routers, services, models)
- Fully documented API via Swagger (OpenAPI)

## Tech Stack
- Python 3.9
- FastAPI
- Pydantic
- Uvicorn
- Alpha Vantage API

## Getting Started
1. Clone the repository
2. Create and activate a virtual environment
3. Install dependencies using `requirements.txt`
4. Set environment variables (Alpha Vantage API key)
5. Run the server using Uvicorn

## Running Locally

1. Create and activate a virtual environment
2. Install dependencies:
   pip install -r requirements.txt
3. Create a `.env` file using `.env.example`
4. Start the server:
   uvicorn app.main:app --reload

## API Documentation

When running the application locally, interactive API documentation is available at:

http://127.0.0.1:8000/docs

This is powered by FastAPI’s built-in Swagger UI.
