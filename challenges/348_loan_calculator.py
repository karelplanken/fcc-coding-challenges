# Daily Coding challenge #348 (2026-07-24) - freeCodeCamp.org
# Loan Calculator
# Given a loan amount, annual interest rate percentage, and fixed monthly payment,
# return an array of remaining balances after each monthly payment until the loan is
# paid off.

# - Each month, interest is calculated on the remaining balance using the monthly
#   interest rate: (annual rate / 100) / 12, then the monthly payment is subtracted.
# - Return each remaining balance rounded to the nearest dollar.
# - Include the loan amount in the returned array. The first element in the array will
#   always be the loan amount, and the last element of the array will always be 0.
from decimal import ROUND_HALF_UP, Decimal

from pytest import mark


def get_loan_schedule(
    loan_amount: float, annual_rate: float, monthly_payment: float
) -> list[int]:
    """Returns remaining balances after each monthly payment until the loan is paid off.

    Calculations are done using Decimal for precision, and the final balances are
    rounded to the nearest dollar.

    Args:
        loan_amount: loan amount (principal) in dollars
        annual_rate: annual interest rate percentage
        monthly_payment: fixed monthly payment in dollars

    Returns:
        list[int]: remaining balances after each monthly payment

    Raises:
        ValueError: if loan_amount is not positive
        ValueError: if annual_rate is negative
        ValueError: if monthly_payment is not positive
        ValueError: if loan will never be repaid
    """
    if loan_amount <= 0:
        raise ValueError('loan_amount must be positive')
    if annual_rate < 0:
        raise ValueError('annual_rate must be non-negative')
    if monthly_payment <= 0:
        raise ValueError('monthly_payment must be positive')

    annual_rate_fraction = Decimal(str(annual_rate)) / Decimal('100')
    monthly_rate = annual_rate_fraction / Decimal('12')

    balance = Decimal(str(loan_amount))
    monthly_payment_dec = Decimal(str(monthly_payment))

    if monthly_payment_dec <= balance * monthly_rate:
        raise ValueError('loan will never be repaid')

    monthly_balances = [balance]

    while balance > 0:
        balance = balance * (1 + monthly_rate) - monthly_payment_dec

        monthly_balances.append(max(balance, Decimal('0')))

    return [
        int(balance.quantize(Decimal('1'), rounding=ROUND_HALF_UP))
        for balance in monthly_balances
    ]


# Alternative approach: calculate the balance after k months using the formula:
# def month_balance(
#     principal: Decimal, rate: Decimal, payment: Decimal, k: int
# ) -> Decimal:
#     # B_k = P*(1+r)^k - M * ((1+r)^k - 1) / r
#     if rate == 0:
#         return principal - payment * k
#     growth = (1 + rate) ** k
#     return principal * growth - payment * (growth - 1) / rate

tests: list[tuple[float, float, float, list[float]]] = [
    (1000, 0, 200, [1000, 800, 600, 400, 200, 0]),
    (1000, 5, 200, [1000, 804, 608, 410, 212, 13, 0]),
    (10, 50, 1, [10, 9, 9, 8, 8, 7, 6, 5, 5, 4, 3, 2, 1, 0, 0]),
    (
        5500,
        8,
        400,
        [
            5500,
            5137,
            4771,
            4403,
            4032,
            3659,
            3283,
            2905,
            2525,
            2141,
            1756,
            1367,
            977,
            583,
            187,
            0,
        ],
    ),
    (
        50000,
        5.2,
        1650,
        [
            50000,
            48567,
            47127,
            45681,
            44229,
            42771,
            41306,
            39835,
            38358,
            36874,
            35384,
            33887,
            32384,
            30874,
            29358,
            27835,
            26306,
            24770,
            23227,
            21678,
            20122,
            18559,
            16990,
            15413,
            13830,
            12240,
            10643,
            9039,
            7428,
            5810,
            4186,
            2554,
            915,
            0,
        ],
    ),
]


@mark.parametrize('loan_amount, annual_rate, monthly_payment, expected', tests)
def test_get_loan_schedule(
    loan_amount: float,
    annual_rate: float,
    monthly_payment: float,
    expected: list[float],
) -> None:
    assert get_loan_schedule(loan_amount, annual_rate, monthly_payment) == expected


if __name__ == '__main__':
    loan_amount, annual_rate, monthly_payment, expected = tests[0]
    print(get_loan_schedule(loan_amount, annual_rate, monthly_payment))
