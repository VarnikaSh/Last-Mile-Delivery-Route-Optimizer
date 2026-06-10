import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
from route_optimizer import optimize_route
from vehicle_allocator import allocate_vehicles
from traffic_model import predict_traffic
from risk_engine import calculate_risk  

st.set_page_config(
    layout="wide",
)
st.title(
    "🚚 Last Mile Route Optimizer"
)
df = pd.read_csv("deliveries.csv")
traffic = predict_traffic()
vehicles = allocate_vehicles(df)
st.success(
    f"Traffic Status: {traffic}"
)
col1,col2,col3 = st.columns(3)
with col1:
    st.metric(
        "Deliveries",
        len(df)
    )
with col2:
    st.metric(
        "Vehicles Used",
        len(vehicles)
    )    
with col3:
    st.metric(
        "Traffic",
        traffic
    )
m = folium.Map(
    location=[
        df.latitude.mean(),
        df.longitude.mean()
    ],
    zoom_start=12
)            
for _, row in df.iterrows():
    risk = calculate_risk(
        traffic,
        row["package_weight"],
        row["priority"]
    )
    folium.Marker(
        [
            row["latitude"],
            row["longitude"]
        ],
        popup=f"""
        Delivery {row['delivery_id']}
        Risk: {risk}
        """
    ).add_to(m)
st_folium(
    m, 
    width=1200,
    height=500
)        
st.subheader(
    "Vehicle Allocation"
)
for i, vehicle in enumerate(vehicles):
    st.write(
        f"Vehicle {i+1}"
    )
    temp = pd.DataFrame(vehicle)
    st.dataframe(
        temp
    )  
st.subheader(
    "Optimized Route"
)
route = optimize_route(df)
st.write(route)
st.subheader(
    "Delivery Analytics"
)
risk_scores = []
for _, row in df.iterrows():
    risk_scores.append(
        calculate_risk(
            traffic,
            row["package_weight"],
            row["priority"]
        )
    ) 
analytics = pd.DataFrame({
    "Delivery ID": df["delivery_id"],
    "Risk Score": risk_scores
})
st.dataframe(
    analytics
)                   