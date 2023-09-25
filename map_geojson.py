import geopandas as gpd
import pandas as pd
import numpy as np

def lake():
    goal_point = None
    start_point = None  
    lake_poly = None

    gdf = gpd.read_file('map.geojson')
    filtered_goal = gdf[gdf['type'] == 'goal']
    if not filtered_goal.empty:
        goal_point = filtered_goal.geometry.iloc[0]
    else:
        print("Error: No goal point found")

    filtered_start = gdf[gdf['type'] == 'start']
    if not filtered_start.empty:
        start_point = filtered_start.geometry.iloc[0]
      
    else:
        print("Error: No start point found")

    filtered_boat = gdf[gdf['type'] == 'boat']
    if not filtered_boat.empty:
        boat_point = filtered_boat.geometry.iloc[0]
      
    else:
        print("Error: No boat point found")

    # get Lake polygon
    filtered_lake = gdf[gdf['type'] == 'lake']
    if not filtered_lake.empty:
        lake_poly = filtered_lake.geometry.iloc[0]
        lake_poly = lake_poly.exterior.coords[:]
       
    else:
        print("Error: No lake found")

    
    

    # Convert the Point geometries to NumPy arrays
    if goal_point:
        lake.GOAL = np.array(goal_point.coords[0])
    if start_point:
        lake.START = np.array(start_point.coords[0])
    if boat_point:
        lake.BOAT = np.array(boat_point.coords[0])

    lake.LAKE = lake_poly

    return lake

lake = lake()
