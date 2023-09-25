import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from helper import *
from heading import calculate_new_heading
from constants import constants as c
from visualize import visualize

def animate_boat_position():
    # Initialize the plot
    fig, ax = plt.subplots()
    
    # Initialize the boat's position
    boat_x, boat_y = c.BOAT

    # Create a function to update the boat's position in the animation
    def update(frame):
        nonlocal boat_x, boat_y

        # Calculate the new heading and update boat's position
        boat_vector = normalize(c.GOAL - np.array([boat_x, boat_y]))
        wind_direction_vector = normalize(vectorize_angle(c.WIND_DIRECTION))
        goal_vector = normalize(c.GOAL - np.array([boat_x, boat_y]))
        new_heading = calculate_new_heading(
            boat_vector, wind_direction_vector, c.TACK_ANGLE, goal_vector, vectorize_angle(goal_vector))

        # Update boat's position based on the new heading
        boat_x += new_heading[0] * 0.1  # Adjust the step size as needed
        boat_y += new_heading[1] * 0.1

        # Clear the previous frame
        ax.clear()

        # Visualize the updated positions
        visualize(c.START, c.GOAL, [boat_x, boat_y], None, None, None, wind_direction_vector, new_heading, goal_vector)

    # Create the animation
    ani = FuncAnimation(fig, update, frames=100, repeat=False, blit=False)
    plt.show()

if __name__ == "__main__":
    animate_boat_position()
