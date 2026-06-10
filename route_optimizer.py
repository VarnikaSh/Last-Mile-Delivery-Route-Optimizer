import networkx as nx
from math import radians,sin,cos,sqrt,atan2

def distance(
        lat1, lon1, lat2, lon2
):
    R = 6371

    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)

    a = (
        sin(dlat/2)**2
        +
        cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon/2)**2
    )
    c = 2 * atan2(sqrt(a), sqrt(1-a))
    return R * c

def optimize_route(df):
    G = nx.Graph()

    for i in range(len(df)):
        G.add_node(i)

    for i in range(len(df)):
        for j in range(i+1, len(df)):
            d = distance(
                df.iloc[i]['latitude'], df.iloc[i]['longitude'],
                df.iloc[j]['latitude'], df.iloc[j]['longitude']
            )
            G.add_edge(i, j, weight=d)
    route = nx.approximation.traveling_salesman_problem(G, cycle=False)
    return route        