"""Defines dataclass for CalcResult for calc method."""
from dataclasses import dataclass
from typing import List, Tuple, Optional

@dataclass
class CalcResult:
    """Properties of result of computing take home pay to be displayed to user."""
    gross_pay: int
    tax_free_allowance: int
    total_taxable: int
    total_tax_due: int
    tax_due: List[Tuple[int, int]]
    net_pay: int
    national_insurance: Optional[int] = None
    stu_loan_payment: Optional[int] = None
    