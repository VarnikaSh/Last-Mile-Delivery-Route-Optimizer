# Last-Mile Delivery Route Optimizer
An AI-powered logistics optimization platform that improves delivery efficiency using graph algorithms, vehicle capacity planning, traffic intelligence, and risk analytics.

## Overview
Last-mile delivery is one of the most expensive and complex stages of the supply chain. This project optimizes delivery routes while considering real-world constraints such as vehicle capacity, traffic conditions, package priorities, and delivery risks.  
The system uses graph-based route optimization and analytics to help logistics companies reduce delivery time and operational costs.

## Features
- Multi-stop route optimization
- Vehicle capacity allocation
- Traffic-aware delivery planning
- Delivery risk scoring
- Priority package handling
- Interactive map visualization
- Delivery analytics dashboard
- Multi-vehicle scheduling

 ## Tech Stack
 - Python
 - Streamlit
 - Networkx
 - Pandas
 - NumPy
 - Folium
 - Streamlit-Folium
 - Scikit-Learn
 - Xgboost

## Project Structure
Last_Mile_Route_Optimizer/  
|  
|--app.py  
|--route_optimizer.py  
|--traffic_model.py  
|--risk_engine.py  
|--vehicle_allocator.py  
|--deliveries.csv  
|--requirements.txt  
|--README.md

## Installation
### Clone the repository:
git clone https://github.com/VarnikaSh/Last-Mile-Delivery-Route-Optimizer.git  
cd last-mile-route-optimizer  
### Install dependencies:
pip install -r requirements.txt

## Run the Application
streamlit run app.py  
The dashboard will open in your browser automatically.

## System Workflow
1. Load delivery loactions and package data.
2. Allocate deliveries to vehicles based on capacity.
3. Predict traffic conditions.
4. Generate optimized delivery routes.
5. Calculate delivery risk scores.
6. Display routes and analytics on an interactive dashboard.

## Dashboard Features
- Total Deliveries
- Vehicles Utilized
- Current Trffic Status
- Route Optimization Results
- Vehicle Allocation Tables
- Risk Score Analytics
- Interactive Delivery Map

## Future Improvements
- Real-time GPS tracking
- Live traffic API integration
- ETA prediction using Machine Learning
- Reinforcement Learning route optimization
- Carbon emission optimization
- Warehouse assignment optimization
- Multi-city delivery simulation

## Live Demo
[Click Here to try the app](https://last-mile-delivery-route-optimizer-hbqwxmxfkshb9rnzrhq8da.streamlit.app/)

## Author
Varnika Shukla
