def calculate_rider_wage(delivery):
    if delivery < 0:
        raise ValueError("Delivery cannot be negative")

    rider_wage = 0
    base_pay = 5000
    amount_per_percel = 0

    if 0 < delivery < 50:
        amount_per_percel = 160
    elif delivery > 50 and delivery < 60:
        amount_per_percel = 200
    elif delivery > 60 and delivery < 70:
        amount_per_percel = 250
    else:
        amount_per_percel = 500
    rider_wage = amount_per_percel * delivery + base_pay
    return rider_wage

