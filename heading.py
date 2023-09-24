import numpy as np
from helper import *
from constants import constants as c

def calculate_new_heading(boat_vector, wind_direction_vector, tack_angle, goal_vector, goal_heading):
    tack_vector = vectorize_angle(tack_angle)
    print("goal_vector: ", goal_vector)
    angle = singed_angle(boat_vector, goal_vector)
    dot_product = np.dot(wind_direction_vector, boat_vector)
    min_dist = calculate_closest_point_on_line(c.BOAT, c.START, c.GOAL)[0]
    if np.any(dot_product < -0.8):


        if min_dist > 0.5:
            if angle > 0:
                new_heading = np.subtract(goal_vector, tack_vector)
                
            elif angle < 0:
                new_heading = np.add(goal_vector, tack_vector)
        
    return normalize(new_heading)