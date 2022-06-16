"""Instatiates the FastAPI app and defines endpoint for calculation requests."""
import re
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from src.main import main
from schemas.calculate import CalculationRequest

app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
    )


@app.get('/')
async def root():
    """Test endpoint."""
    return {"message": "Hello World"}

@app.post("/")
async def req(calculation_request: CalculationRequest):
    """Endpoint for calculation request."""
    print(calculation_request)
    if int(calculation_request.salary) < 0:
        raise HTTPException(status_code=400, detail="Invalid salary, must be a positive value")
    if not re.match("^(19[5-9]\d|20[0-9]\d|2050)\/([0-9]\d)$", calculation_request.taxYear):
        raise HTTPException(status_code=400, detail="Invalid date format, must be YYYY/YY")
    if len(calculation_request.taxYear) == 7 and int(calculation_request.taxYear[5:7]) - int(calculation_request.taxYear[2:4]) != 1:
        raise HTTPException(status_code=400, detail="Invalid date range, must be one year separation e.g. 2022/23")
    return main(calculation_request.salary, calculation_request.taxYear)
