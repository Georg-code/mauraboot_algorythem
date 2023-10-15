import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from helper import * 
from visualize import visualize
from heading import calculate_new_heading
from constants import constants as c
from map_geojson import lake
from animate import generate_path
import time



def simulate():

    print("GOAL: ", c.GOAL)
    print("START: ", c.START)
    print("BOAT: ", c.BOAT)
    print("WIND_DIRECTION: ", c.WIND_DIRECTION)

    boat_vector = normalize(c.GOAL - c.START)
    wind_direction_vector = normalize(vectorize_angle(c.WIND_DIRECTION))
    goal_vector = normalize(c.GOAL - c.BOAT)
    (x, y) = calculate_closest_point_on_line(c.BOAT, c.START, c.GOAL)[2:]
    min_index = calculate_closest_point_on_line(c.BOAT, c.START, c.GOAL)[1]
   # generate_path(boat_vector, wind_direction_vector, goal_vector, 0.001)
    new_heading = calculate_new_heading(
        boat_vector, wind_direction_vector, goal_vector)
    visualize(c.START, c.GOAL, c.BOAT, x, y, min_index,
              wind_direction_vector, new_heading, goal_vector, lake.LAKE)
  

def run(boat_vector, boat_location, wind_direction_vector, goal_vector, interval, simulate=True):
   
    new_heading = calculate_new_heading(boat_vector, wind_direction_vector, goal_vector)
    if simulate:
        (x, y) = calculate_closest_point_on_line(boat_location, c.START, c.GOAL)[2:]
        min_index = calculate_closest_point_on_line(boat_location, c.START, c.GOAL)[1]
        print(boat_location)
        print(boat_vector)
        # add boat vector to boat location to get new boat location using nupy vector addition
        boat_location = boat_location + new_heading * 0.001
        goal_vector = normalize(c.GOAL - boat_location)
        visualize(c.START, c.GOAL, boat_location, x, y, min_index,
                  wind_direction_vector, new_heading, goal_vector, lake.LAKE)
        
    
    
   
    time.sleep(interval)
    run(boat_vector, c.BOAT, wind_direction_vector, goal_vector, 1, simulate)
      


def main():
    boat_vector = normalize(c.GOAL - c.START)
    wind_direction_vector = normalize(vectorize_angle(c.WIND_DIRECTION))
    goal_vector = normalize(c.GOAL - c.BOAT)
   # run(boat_vector, c.BOAT, wind_direction_vector, goal_vector, 1, True)
    simulate()



main()