import numpy as np

def vectorize_angle(angle):
    # turn an angle into a normalized vector
    return normalize(np.array([np.cos(angle), np.sin(angle)]))
    

def vector_to_angle(vector):
    # turn a normalized vector into an angle
    vector = normalize(vector)
    return np.arctan2(vector[1], vector[0])


def normalize(vector):
    # normalize vector
    return vector / np.linalg.norm(vector)


def calculate_heading(vector):
    return np.arctan2(vector[1], vector[0])


def calculate_angle(vector1, vector2):
    return np.arctan2(vector2[1], vector2[0]) - np.arctan2(vector1[1], vector1[0])


def calculate_closest_point_on_line(point, line_start, line_end):
    def calculate_distance(point1, point2):
        return np.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)
    x = np.linspace(line_start[0], line_end[0], 100)
    y = np.linspace(line_start[1], line_end[1], 100)
    min_dist = np.inf
    min_index = 0
    for i in range(len(x)):
        dist = calculate_distance(point, (x[i], y[i]))
        if dist < min_dist:
            min_dist = dist
            min_index = i
    return min_dist, min_index, x, y


def singed_angle(vector1, vector2):
    return np.arctan2(vector2[1], vector2[0]) - np.arctan2(vector1[1], vector1[0])
