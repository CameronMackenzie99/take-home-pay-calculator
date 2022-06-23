"""Utility functions for calculating monetary amounts over differnt time periods."""
from dataclasses import dataclass
from enum import Enum
from moneyed import Money

@dataclass
class MoneyPerPeriod:
    """Object for storing monetary amounts over different time periods. e.g. yearly wage."""
    week: Money
    month: Money
    year: Money

class Period(Enum):
    """Enum to store time periods."""
    WEEK = "week"
    MONTH = "month"
    YEAR = "year"

def get_time_period_amounts(period: Period, amt: Money) -> MoneyPerPeriod:
    """Returns object containing monetary amounts over a weekly,
    monthly and yearly period based on an input amount associated
    with one of those time periods."""
    match period:
        case Period.WEEK:
            year = amt * 52
            month = year / 12
            week = amt
        case Period.MONTH:
            year = amt * 12
            month = amt
            week = year / 52
        case Period.YEAR:
            year = amt
            month = amt / 12
            week = amt / 52

    return MoneyPerPeriod(week, month, year) #type: ignore (not dividing by "other" object)

get_time_period_amounts(Period.WEEK, Money(100, "GBP"))
get_time_period_amounts(Period.MONTH, Money(1500, "GBP"))
get_time_period_amounts(Period.YEAR, Money(55000, "GBP"))
