import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from helper import * 
from visualize import visualize
from heading import calculate_new_heading
from constants import constants as c
from map_geojson import lake
import time
import serial
import json


serial_port = '/dev/tty0'  # Adjust this to your Arduino's serial port
baud_rate = 9600


  

def run(boat_vector, wind_direction_vector, goal_vector):
    new_heading = calculate_new_heading(boat_vector, wind_direction_vector, goal_vector)
   
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
                optimal_heading = run(boat_vector, wind_direction_vector, goal_vector)
                actual_heading = vectorize_angle(data['compass_azimuth'])
                print(f'Optimal Heading: {optimal_heading}')
                print(f'Actual Heading: {actual_heading}')
            

                

        


            




            except json.JSONDecodeError as e:
                print(f"Error decoding JSON: {e}")

    except KeyboardInterrupt:
    # Close the serial connection on program exit
        ser.close()
        print("Serial connection closed.")



main()