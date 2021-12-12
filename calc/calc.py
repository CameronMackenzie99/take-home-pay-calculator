from dataclasses import dataclass
from typing import Protocol
@dataclass
class CalcResult:
    gross_pay: int
    tax_free_allowance: int
    total_taxable: int
    total_tax_due: int
    tax_due: list[tuple[int, int]]
    stu_loan_payment: int
    national_insurance: int
    net_pay: int

class Calc(Protocol):
    def calc(self, salary: int) -> CalcResult:
        ...