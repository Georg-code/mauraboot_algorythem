import matplotlib.pyplot as plt
import numpy as np

def visualize(start, goal, boat, x, y, min_index, wind_direction_vector, new_heading, goal_vector):
    print("new_heading: ", new_heading)

    plt.figure(figsize=(8, 8))
    plt.plot(start[0], start[1], 'go', markersize=10, label="Start")
    plt.plot(goal[0], goal[1], 'ro', markersize=10, label="Goal")
    plt.plot(boat[0], boat[1], 'bo', markersize=10, label="Boat")
    plt.plot(x, y, 'k--', label="Line between start and goal")
    plt.plot(x[min_index], y[min_index], 'ro',
             markersize=10, label="Closest point on line")
    plt.plot([boat[0], x[min_index]], [boat[1], y[min_index]], 'b--',)

    # visualize wind direction arrow big at the goal location in blue
    plt.arrow(goal[0], goal[1], wind_direction_vector[0], wind_direction_vector[1],
                width=0.05, length_includes_head=True, label="Wind direction",  fc='blue')
    
    # visualize goal vector arrow big at the goal location in red
    plt.arrow(boat[0], boat[1], goal_vector[0], goal_vector[1],
                width=0.05, length_includes_head=True, label="Goal vector",  fc='red')
    
     # visualize new heading vector arrow big at the boat location in green
    plt.arrow(boat[0], boat[1], new_heading[0], new_heading[1],
                width=0.05, length_includes_head=True, label="New heading",  fc='green')


    plt.xlim(0, 10)
    plt.ylim(0, 10)
    plt.legend()
    plt.grid()
    plt.show()