def calculate_risk(
        traffic,
        weight,
        priority
):
    risk = 0
    if traffic == "High":
        risk += 50
    elif traffic == "Medium":
        risk += 25
    if weight > 6:
        risk += 20
    if priority == "High":
        risk += 30
    return min(risk, 100)  # Ensure risk does not exceed 100        