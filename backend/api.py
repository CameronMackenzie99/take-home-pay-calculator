"""Instatiates the FastAPI app and defines endpoint for calculation requests."""
from fastapi import FastAPI
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
    return main(calculation_request.salary, calculation_request.taxYear)
