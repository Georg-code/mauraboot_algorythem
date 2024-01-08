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
import serial
import json


serial_port = '/dev/ttyUSB0'  # Adjust this to your Arduino's serial port
baud_rate = 9600

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
        
    
    
   
    return new_heading
      


def main():
    ser = serial.Serial(serial_port, baud_rate)
    try:
        while True:
        # Read a line from the serial port
            line = ser.readline().decode('utf-8').strip()

            try:
                
                if line == '':
                    continue

          
                data = json.loads(line)

                gps_lat = data['gps_lat']
                gps_lng = data['gps_lng']

                # make an np array of the gps data
                gps_data = np.array([gps_lat, gps_lng])

                # Do something with the data
                print(f'GPS Latitude: {gps_lat}, Longitude: {gps_lng}')

                boat_vector = normalize(c.GOAL - c.START)
                wind_direction_vector = normalize(vectorize_angle(c.WIND_DIRECTION))
                goal_vector = normalize(c.GOAL - gps_data)
                heading = run(boat_vector, gps_data, wind_direction_vector, goal_vector, 1, False)

            except json.JSONDecodeError as e:
                print(f"Error decoding JSON: {e}")

    except KeyboardInterrupt:
    # Close the serial connection on program exit
        ser.close()
        print("Serial connection closed.")



main()