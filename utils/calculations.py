import math


def calculate_emi(principal, annual_rate, years):

    monthly_rate = annual_rate / (12 * 100)

    months = years * 12

    if monthly_rate == 0:

        emi = principal / months

    else:

        emi = principal * monthly_rate * ((1 + monthly_rate) ** months)

        emi /= ((1 + monthly_rate) ** months - 1)

    total_payment = emi * months

    total_interest = total_payment - principal

    return round(emi, 2), round(total_interest, 2), round(total_payment, 2)


def calculate_sip(monthly_investment, annual_rate, years):

    monthly_rate = annual_rate / 1200

    months = years * 12

    future_value = monthly_investment * (
        (((1 + monthly_rate) ** months) - 1)
        / monthly_rate
    ) * (1 + monthly_rate)

    invested = monthly_investment * months

    wealth = future_value - invested

    return (
        round(invested, 2),
        round(wealth, 2),
        round(future_value, 2),
    )


def savings_goal(goal, current, monthly):

    if monthly <= 0:
        return 0

    remaining = goal - current

    if remaining <= 0:
        return 0

    months = math.ceil(remaining / monthly)

    return months


def budget_summary(income, expenses):

    savings = income - expenses

    if income == 0:

        savings_percent = 0

    else:

        savings_percent = (savings / income) * 100

    return (
        round(savings, 2),
        round(savings_percent, 2)
    )