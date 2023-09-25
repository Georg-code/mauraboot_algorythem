import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from helper import * 
from visualize import visualize
from heading import calculate_new_heading
from constants import constants as c
from animate import animate_boat_position
from map_geojson import lake




def main():

    print("GOAL: ", c.GOAL)
    print("START: ", c.START)
    print("BOAT: ", c.BOAT)
    print("WIND_DIRECTION: ", c.WIND_DIRECTION)

    boat_vector = normalize(c.GOAL - c.START)
    wind_direction_vector = normalize(vectorize_angle(c.WIND_DIRECTION))
    goal_vector = normalize(c.GOAL - c.BOAT)
    goal_heading = vectorize_angle(goal_vector)
    (x, y) = calculate_closest_point_on_line(c.BOAT, c.START, c.GOAL)[2:]
    min_index = calculate_closest_point_on_line(c.BOAT, c.START, c.GOAL)[1]

    new_heading = calculate_new_heading(
        boat_vector, wind_direction_vector, c.TACK_ANGLE, goal_vector, goal_heading)
    visualize(c.START, c.GOAL, c.BOAT, x, y, min_index,
              wind_direction_vector, new_heading, goal_vector, lake.LAKE)

    

if __name__ == "__main__":
    main()