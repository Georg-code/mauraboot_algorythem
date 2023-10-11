import numpy as np
from visualize import visualize
from heading import calculate_new_heading
from constants import constants as c
from map_geojson import lake
from helper import * 

def generate_path(boat_vector, wind_direction_vector, goal_vector, step_size=0.001):
    '''generate a path for the boat to follow'''
    # generate a path for the boat to follow
    (x, y) = calculate_closest_point_on_line(c.BOAT, c.START, c.GOAL)[2:]
    min_index = calculate_closest_point_on_line(c.BOAT, c.START, c.GOAL)[1]
    path = []
    path.append(c.BOAT)
    new_heading = calculate_new_heading(
        boat_vector, wind_direction_vector, goal_vector)
    while np.linalg.norm(path[-1] - c.GOAL) > 0.001:
        new_heading = calculate_new_heading(
            boat_vector, wind_direction_vector, goal_vector)
        path.append(path[-1] + step_size * new_heading)
    print("path: ", path)
    visualize(c.START, c.GOAL, c.BOAT, x, y, min_index, wind_direction_vector, new_heading, goal_vector, lake.LAKE, path)