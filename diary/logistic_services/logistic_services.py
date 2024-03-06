def calculate_rider_wage(delivery):
    rider_wage = 0
    amount_per_percel = 0
    if 0 < delivery < 50:
        amount_per_percel = 160
    elif delivery > 50 and delivery < 60:
        amount_per_percel = 200
    elif delivery > 60 and delivery < 70:
        amount_per_percel = 250
    else
        amount_per_percel = 500


