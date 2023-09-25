import numpy as np
from helper import *
from constants import constants as c

def calculate_new_heading(boat_vector, wind_direction_vector, tack_angle, goal_vector, goal_heading):
    tack_vector = np.array([np.cos(tack_angle), np.sin(tack_angle)])
    print("goal_vector: ", goal_vector)
    angle = singed_angle(boat_vector, goal_vector)
    dot_product = np.dot(wind_direction_vector, boat_vector)
    min_dist = calculate_closest_point_on_line(c.BOAT, c.START, c.GOAL)[0]
    new_heading = goal_vector
    if np.any(dot_product < -0.8):
        print("im wind")
        if min_dist > 0.5:
            print("distance bigger than 0.5")
        #     if angle >= 0:
        #        # Loop until new heading has a dot prduct of bigger than -0.8 with wind direction with a step of 0.1
        #         n = 0
        #         while np.dot(wind_direction_vector, new_heading) > -0.92:
        #             n += 0.1
        #             new_heading = np.add(boat_vector, n * np.array([-goal_vector[1], goal_vector[0]]))
        #         print ("n: ", n)
                
        #     elif angle < 0:
        #         n = 1
        #         while np.dot(wind_direction_vector, new_heading) < -0.8:
        #             n -= 0.1
        #             new_heading = np.subtract(boat_vector, n * np.array([-goal_vector[1], goal_vector[0]]))
        # else:
        #     print("angle: ", angle)
        #     if angle >= 0:
        #         # Loop until new heading has a dot prduct of bigger than -0.8 with wind direction with a step of 0.1
        #          n = 0
        #          while np.dot(wind_direction_vector, new_heading) > -0.92:
        #               n += 0.1
        #               new_heading = np.add(boat_vector, n * np.array([-goal_vector[1], goal_vector[0]]))
        #          print ("n: ", n)
        #     elif angle < 0:
        #         n = 1
        #         while np.dot(wind_direction_vector, new_heading) < -0.8:
        #             n -= 0.1
        #             new_heading = np.subtract(boat_vector, n * np.array([-goal_vector[1], goal_vector[0]]))

        
    
        
    return normalize(new_heading)