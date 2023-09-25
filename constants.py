import numpy as np
from map_geojson import lake

def constants():


#    GOAL = np.array([9.0, 9.0])
 #   START = np.array([1.0, 1.0])
    BOAT = np.array([8.7, 47.24])
    WIND_DIRECTION = np.deg2rad(0)
    TACK_ANGLE = np.deg2rad(25)

    constants.GOAL = lake.GOAL
    constants.START = lake.START
    constants.BOAT = lake.BOAT
    constants.WIND_DIRECTION = WIND_DIRECTION
    constants.TACK_ANGLE = TACK_ANGLE
    
    return constants

constants = constants()
