import numpy as np

def vectorize_angle(angle):
    '''turn an angle into a normalized vector'''
    # turn an angle into a normalized vector
    return normalize(np.array([np.cos(angle), np.sin(angle)]))
    

def vector_to_angle(vector):
    '''turn a normalized vector into an angle'''
    # turn a normalized vector into an angle
    vector = normalize(vector)
    return np.arctan2(vector[1], vector[0])


def normalize(vector):
    '''normalize a vector'''
    # normalize vector
    return vector / np.linalg.norm(vector)


def calculate_heading(vector):
    '''calculate the heading of a vector'''
    return np.arctan2(vector[1], vector[0])


def calculate_angle(vector1, vector2):
    '''calculate the angle between two vectors'''
    dot_product = np.dot(vector1, vector2)
    magnitude1 = np.linalg.norm(vector1)
    magnitude2 = np.linalg.norm(vector2)



def calculate_closest_point_on_line(point, line_start, line_end):
    '''calculate the closest point on a line to a given point'''

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


def singed_angle(v1, v2):
        '''calculate the signed angle between two vectors'''
        dot_product = np.dot(v1, v2)
        v1_magnitude = np.linalg.norm(v1)
        v2_magnitude = np.linalg.norm(v2)
    
        cos_theta = dot_product / (v1_magnitude * v2_magnitude)
        angle_rad = np.arccos(np.clip(cos_theta, -1.0, 1.0))
    
        # Calculate the sign of the angle using the cross product
        cross_product = np.cross(v1, v2)
        if cross_product < 0:
            angle_rad = -angle_rad
    
     # Convert radians to degrees
        angle_deg = np.degrees(angle_rad)
    
        return angle_deg
