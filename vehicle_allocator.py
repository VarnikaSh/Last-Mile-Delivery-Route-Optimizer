import pandas as pd

VEHICLE_CAPACITY = 15

def allocate_vehicles(df):
    vehicles = []
    current_vehicle = []
    current_load = 0
    for _, row in df.iterrows():
        weight = row["package_weight"]
        if current_load + weight <= VEHICLE_CAPACITY:
            current_vehicle.append(row)
            current_load += weight
        else:
            vehicles.append(current_vehicle)
            current_vehicle = [row]
            current_load = weight
    if current_vehicle:
        vehicles.append(current_vehicle)
    return vehicles            