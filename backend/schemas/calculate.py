"""Defines schemas for JSON request and response shapes."""
from pydantic import BaseModel


class CalculationRequest(BaseModel):
    """Input parameters for calculation."""
    salary: str
    taxYear: str

class CalculationResponse(BaseModel):
    """Shape of JSON response for calculation."""
    gross_pay: str
    tax_free_allowance: str
    total_taxable: str
    total_tax_due: str
    national_insurance: str
    net_pay: str
    p20_tax_band: str
    p40_tax_band: str
    p45_tax_band: str
