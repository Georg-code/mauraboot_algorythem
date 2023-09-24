import numpy as np

def constants():
    GOAL = np.array([9.0, 9.0])
    START = np.array([1.0, 1.0])
    BOAT = np.array([8.0, 2.0])
    WIND_DIRECTION = np.deg2rad(225)
    TACK_ANGLE = np.deg2rad(25)

    constants.GOAL = GOAL
    constants.START = START
    constants.BOAT = BOAT
    constants.WIND_DIRECTION = WIND_DIRECTION
    constants.TACK_ANGLE = TACK_ANGLE
    
    return constants

constants = constants()
