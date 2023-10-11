import numpy as np
from helper import *
from constants import constants as c

def calculate_new_heading(boat_vector, wind_direction_vector, goal_vector):
    dot_product = np.dot(wind_direction_vector, boat_vector)

    new_heading = goal_vector
    if np.any(dot_product < -0.8):
        if np.dot(wind_direction_vector, goal_vector) > -0.8:
            new_heading = goal_vector
            return normalize(new_heading)
        n = 0
        while np.dot(wind_direction_vector, new_heading) < -0.8 and n < 1:         
            n += 0.1
            new_heading1 = np.add(goal_vector, n * np.array([goal_vector[1], -goal_vector[0]]))
            new_heading2 = np.add(goal_vector, n * np.array([-goal_vector[1], goal_vector[0]]))

            # find which heading is closer to the goal using the dot product
            if np.dot(new_heading1, goal_vector) > np.dot(new_heading2, goal_vector):
                new_heading = new_heading1
            else:
                new_heading = new_heading2
        return normalize(new_heading)





"""         if True:
            print("angle: ", angle)
            if angle <= 0:
                print("angle <= 0")
                n = 0
                while np.dot(wind_direction_vector, new_heading) < -0.8 and n < 1:
                   
                    n += 0.1
                    # turn new heading until dot product is bigger than -0.8
                    new_heading = np.add(goal_vector, n * np.array([goal_vector[1], -goal_vector[0]]))
                print("n: ", n)
                return normalize(new_heading)
            
            else:
                print("anfle > 0")
                n = 0
                while np.dot(wind_direction_vector, new_heading) < -0.8 and n < 1:
                    n += 0.1
                    # turn new heading until dot product is bigger than -0.8
                    new_heading = np.add(goal_vector, n * np.array([-goal_vector[1], goal_vector[0]]))
                print("n: ", n)
        
                return normalize(new_heading) """

        
   # return normalize(new_heading)





    #  if angle >= 0:
              #      pass
        #        # Loop until new heading has a dot prduct of bigger than -0.8 with wind direction with a step of 0.1
        #         n = 0
        #         while np.dot(wind_direction_vector, new_heading) > -0.92:
        #             n += 0.1
        #             new_heading = np.add(boat_vector, n * np.array([-goal_vector[1], goal_vector[0]]))
        #         print ("n: ", n)
                
        #     elif angle < 0:
        #         n = 1
        #         while np.dot(wind_direction_vector, new_heading) < -0.8:
        #             n -= 0.1
        #             new_heading = np.subtract(boat_vector, n * np.array([-goal_vector[1], goal_vector[0]]))
        # else:
        #     print("angle: ", angle)
        #     if angle >= 0:
        #         # Loop until new heading has a dot prduct of bigger than -0.8 with wind direction with a step of 0.1
        #          n = 0
        #          while np.dot(wind_direction_vector, new_heading) > -0.92:
        #               n += 0.1
        #               new_heading = np.add(boat_vector, n * np.array([-goal_vector[1], goal_vector[0]]))
        #          print ("n: ", n)
        #     elif angle < 0:
        #         n = 1
        #         while np.dot(wind_direction_vector, new_heading) < -0.8:
        #             n -= 0.1
        #             new_heading = np.subtract(boat_vector, n * np.array([-goal_vector[1], goal_vector[0]]))
