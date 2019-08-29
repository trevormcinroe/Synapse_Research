import numpy as np
import math

quadrant_dict = {
    1: (0, 90),
    2: (270, 360),
    3: (180, 270),
    4: (90, 180)
}

def quadrant_update(quadrant_dict, current_angle):
    """

    Args:
        quadrant_dict:
        current_angle:

    Returns:

    """

    if current_angle > 360:
        raise ValueError('You have left the circle, my fiend.')

    quadrant = 1


    while not (current_angle >= quadrant_dict[quadrant][0] and
               current_angle <= quadrant_dict[quadrant][1]):
        quadrant += 1

    return quadrant


def vector_coordinates(current_quadrant,
                       current_angle,
                       beginning_point,
                       radius,
                       quadrant_dict):
    """

    Args:
        current_quadrant:
        current_angle:
        beginning_point:
        radius:
        quadrant_dict:

    Returns:

    """

    # Need an explicit catch for the cases where the current angle is
    # EXACTLY on the x or y axis
    if current_angle == 0:
        x = beginning_point[0]
        y = beginning_point[1] + radius
        return x, y

    if current_angle == 90:
        x = beginning_point[0] + radius
        y = beginning_point[1]

        return x, y

    if current_angle == 180:
        x = beginning_point[0]
        y = beginning_point[1] - radius

        return x, y

    if current_angle == 270:
        x = beginning_point[0] - radius
        y = beginning_point[1]

        return x, y

    # Calculating the angle between the vector and the closest axis
    angle_calc = quadrant_dict[current_quadrant][1] - current_angle

    # Calculating x
    x = radius * math.cos(math.radians(angle_calc))

    # Calculating y
    y = radius * math.sin(math.radians(angle_calc))

    # Now, based on the quadrant that we are currently in, we need to add
    # +/- signs to the vectors appropriately
    if current_quadrant == 1:

        return x, y

    if current_quadrant == 2:

        return -x, y

    if current_quadrant == 3:

        return -x, -y

    if current_quadrant == 4:

        return x, -y
