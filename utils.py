import math

__all__ = [
    "single_payment_compound_amount_factor",
    "single_payment_present_worth_factor",
    "uniform_series_compound_amount_factor",
    "uniform_series_present_worth_factor",
    "sinking_fund_factor",
    "capital_recovery_factor",
    "nominal_to_effective_annual_rate",
    "effective_annual_to_nominal_periodic_rate",
]
__author__ = "Christian Cahig"

def single_payment_compound_amount_factor(
    interest_rate : float,
    num_periods : int,
) -> float:
    assert 0.0 < interest_rate < 1.0
    assert num_periods >= 1
    if not isinstance(interest_rate, float): interest_rate = float(interest_rate)
    if not isinstance(num_periods, int): num_periods = int(num_periods)

    return math.pow(1.0 + interest_rate, num_periods)

def single_payment_present_worth_factor(
    interest_rate : float,
    num_periods : int,
) -> float:
    assert 0.0 < interest_rate < 1.0
    assert num_periods >= 1
    if not isinstance(interest_rate, float): interest_rate = float(interest_rate)
    if not isinstance(num_periods, int): num_periods = int(num_periods)

    return math.pow(1.0 + interest_rate, -num_periods)

def uniform_series_compound_amount_factor(
    interest_rate : float,
    num_periods : int,
) -> float:
    assert 0.0 < interest_rate < 1.0
    assert num_periods >= 1
    if not isinstance(interest_rate, float): interest_rate = float(interest_rate)
    if not isinstance(num_periods, int): num_periods = int(num_periods)

    return (math.pow(1.0 + interest_rate, num_periods) - 1.0) / interest_rate

def uniform_series_present_worth_factor(
    interest_rate : float,
    num_periods : int,
) -> float:
    assert 0.0 < interest_rate < 1.0
    assert num_periods >= 1
    if not isinstance(interest_rate, float): interest_rate = float(interest_rate)
    if not isinstance(num_periods, int): num_periods = int(num_periods)

    _temp = math.pow(1.0 + interest_rate, num_periods)
    return (_temp - 1.0) / (interest_rate * _temp)

def sinking_fund_factor(
    interest_rate : float,
    num_periods : int,
) -> float:
    assert 0.0 < interest_rate < 1.0
    assert num_periods >= 1
    if not isinstance(interest_rate, float): interest_rate = float(interest_rate)
    if not isinstance(num_periods, int): num_periods = int(num_periods)
    
    return interest_rate / (math.pow(1.0 + interest_rate, num_periods) - 1.0)

def capital_recovery_factor(
    interest_rate : float,
    num_periods : int,
) -> float:
    assert 0.0 < interest_rate < 1.0
    assert num_periods >= 1
    if not isinstance(interest_rate, float): interest_rate = float(interest_rate)
    if not isinstance(num_periods, int): num_periods = int(num_periods)

    return interest_rate / (1.0 - math.pow(1.0 + interest_rate, -num_periods))

def nominal_to_effective_annual_rate(
    nominal_yearly_interest_rate : float,
    num_compounding_periods_per_year : int,
) -> float:
    assert 0.0 < nominal_yearly_interest_rate < 1.0
    assert num_compounding_periods_per_year >= 1
    if not isinstance(nominal_yearly_interest_rate, float):
        nominal_yearly_interest_rate = float(nominal_yearly_interest_rate)
    if not isinstance(num_compounding_periods_per_year, int):
        num_compounding_periods_per_year = int(num_compounding_periods_per_year)
    
    return math.pow(
        1.0 + (nominal_yearly_interest_rate / num_compounding_periods_per_year),
        num_compounding_periods_per_year
    ) - 1.0

def effective_annual_to_nominal_periodic_rate(
    effective_annual_rate : float,
    num_compounding_periods_per_year : int,
) -> float:
    return math.pow(effective_annual_rate + 1.0, 1.0 / num_compounding_periods_per_year) - 1.0

if __name__ == "__main__": pass
