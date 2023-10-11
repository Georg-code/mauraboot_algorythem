import matplotlib.pyplot as plt
import numpy as np

def visualize(start, goal, boat, x, y, min_index, wind_direction_vector, new_heading, goal_vector, lake, path=None):
    lake_x, lake_y = zip(*lake)
    arrow_scale = 0.0025
    zoom=1.5

    # Calculate the x and y limits for the plot
    x_limits = [min(start[0], goal[0], boat[0], np.min(x)), max(start[0], goal[0], boat[0], np.max(x))]
    y_limits = [min(start[1], goal[1], boat[1], np.min(y)), max(start[1], goal[1], boat[1], np.max(y))]

    # Calculate the center point of the plot
    center_x = (x_limits[0] + x_limits[1]) / 2
    center_y = (y_limits[0] + y_limits[1]) / 2

    # Calculate new limits based on the zoom level
    x_range = (x_limits[1] - x_limits[0]) * zoom
    y_range = (y_limits[1] - y_limits[0]) * zoom
    new_x_limits = [center_x - x_range / 2, center_x + x_range / 2]
    new_y_limits = [center_y - y_range / 2, center_y + y_range / 2]

    plt.figure(figsize=(8, 8))
    plt.plot(start[0], start[1], 'go', markersize=10, label="Start")
    plt.plot(goal[0], goal[1], 'ro', markersize=10, label="Goal")
    plt.plot(boat[0], boat[1], 'bo', markersize=10, label="Boat")
    plt.plot(x, y, 'k--', label="Line between start and goal")
    plt.plot(x[min_index], y[min_index], 'ro',
             markersize=10, label="Closest point on line")
    plt.plot([boat[0], x[min_index]], [boat[1], y[min_index]], 'b--',)
    plt.axis('equal')

    # Visualize the lake as a polygon; it is an array of tuples of x and y coordinates of the lake, make it light blue
    plt.fill(lake_x, lake_y, color='lightblue', alpha=0.5, label="Lake")

    # Visualize wind direction arrow, scaled by arrow_scale, big at the goal location in blue
    plt.arrow(goal[0], goal[1], wind_direction_vector[0] * arrow_scale, wind_direction_vector[1] * arrow_scale,
              width=arrow_scale / 10, length_includes_head=True, label="Wind direction", fc='blue')

    # Visualize goal vector arrow, scaled by arrow_scale, big at the boat location in red
    plt.arrow(boat[0], boat[1], goal_vector[0] * arrow_scale, goal_vector[1] * arrow_scale,
              width=arrow_scale / 10, length_includes_head=True, label="Goal vector", fc='red')

    print(new_heading)
    # Visualize new heading vector arrow, scaled by arrow_scale, big at the boat location in green
    plt.arrow(boat[0], boat[1], new_heading[0] * arrow_scale, new_heading[1] * arrow_scale,
              width=arrow_scale / 10, length_includes_head=True, label="New heading", fc='green')

    # If new_heading = goal_vector, draw a green line from boat to goal
    if np.all(new_heading == goal_vector):
        plt.plot([boat[0], goal[0]], [boat[1], goal[1]], 'g--', label="Line between boat and goal")

    # draw a light gray line if the new_heading is not equal to the goal_vector in the direction of the new_heading with a alpha of 0.2
    else:
        plt.plot([boat[0], boat[0] + new_heading[0]], [boat[1], boat[1] + new_heading[1]], 'k--', alpha=0.3,
                 label="Line between boat and new heading")
      # draw a light green line from the boat to the goal with a alpha of 0.2
        plt.plot([boat[0], goal[0]], [boat[1], goal[1]], 'g--', alpha=0.1, label="Line between boat and goal")

    if path:
        path_x, path_y = zip(*path)
        plt.plot(path_x, path_y, 'y--', label="Path")
    plt.xlim(new_x_limits[0], new_x_limits[1])  # Set x-axis limits based on zoom
    plt.ylim(new_y_limits[0], new_y_limits[1])  # Set y-axis limits based on zoom
    plt.legend()
    plt.grid()
    plt.show()
