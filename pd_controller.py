import numpy as np

def pd_controller(current_heading, new_heading, current_rudder_pos):
    Kp = 0.5  # Proportional gain
    Kd = 0.2  # Derivative gain

    # Calculate the error vector (heading error)
    heading_error = new_heading - current_heading

    # Calculate the derivative of the error (rate of change of heading error)
    # Assuming you have a function to get the time step (dt), e.g., dt = get_time_step()
    # Derivative (d) is approximated as (error - previous_error) / dt
    previous_error = pd_controller.previous_error if hasattr(pd_controller, 'previous_error') else 0
    dt = 0.1  # You should adjust the time step as per your simulation or control system
    d_error = (heading_error - previous_error) / dt

    # Calculate the control output (change in rudder position)
    control_output = Kp * heading_error + Kd * d_error

    # Calculate the new rudder position
    new_rudder_pos = current_rudder_pos - control_output

    # Ensure the rudder position is within the valid range (0.0 to 1.0)
    new_rudder_pos = max(0.0, min(1.0, new_rudder_pos))

    # Update the previous error for the next iteration
    pd_controller.previous_error = heading_error

    return new_rudder_pos


