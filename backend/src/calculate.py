"""Defines dataclass for CalcResult for calc method."""
from dataclasses import dataclass
from decimal import Decimal
from typing import List, Optional, Tuple

from moneyed import Money


@dataclass
class CalcResult:
    """Properties of result of computing take home pay to be displayed to user."""
    gross_pay: Money
    tax_free_allowance: Money
    total_taxable: Money
    total_tax_due: Money
    tax_due: List[Tuple[Money, Decimal]]
    national_insurance: Money
    net_pay: Money
    stu_loan_payment: Optional[Money] = None
    