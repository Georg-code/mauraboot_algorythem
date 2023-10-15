import numpy as np

def pd_controller(current_heading, new_heading, current_rudder_pos):
    Kp = 0.5  
    Kd = 0.2 

    heading_error = new_heading - current_heading

    previous_error = pd_controller.previous_error if hasattr(pd_controller, 'previous_error') else 0
    dt = 0.1 
    d_error = (heading_error - previous_error) / dt

    control_output = Kp * heading_error + Kd * d_error
    new_rudder_pos = current_rudder_pos - control_output

    new_rudder_pos = max(0.0, min(1.0, new_rudder_pos))

    # Update the previous error for the next iteration
    pd_controller.previous_error = heading_error

    return new_rudder_pos


