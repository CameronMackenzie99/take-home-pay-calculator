from pydantic import BaseModel


class CalculationRequest(BaseModel):
    """Input parameters for calculation."""
    salary: int


class CalculationResponse(BaseModel):
    """Shape of JSON response for calculation."""
    gross_pay: str
    tax_free_allowance: str
    total_taxable: str
    total_tax_due: str
    net_pay: str
    _20_tax_band: str
    _40_tax_band: str
    _45_tax_band: str
