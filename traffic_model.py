import numpy as np

def predict_traffic():
    value = np.random.randint(0, 100)
    if value < 40:
        return "Low"
    elif value < 80:
        return "Medium"
    else:
        return "High"