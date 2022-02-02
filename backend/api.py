"""Instantiates FastAPI app, and defines routers."""
from fastapi import FastAPI

from src.main import main
from schemas.calculate import CalculationRequest

app = FastAPI()


@app.get('/')
async def root():
    """Returns hello world as a JSON string."""
    return {"message": "Hello World"}

@app.post("/")
async def send_calculation_result(calculation_request: CalculationRequest):
    """Uses the received JSON object to calculate the
    result and sends as a response.
    """
    return main(calculation_request.salary)
