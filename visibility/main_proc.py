from maths import *
import pandas as pd

num_points = 12
radius = 10
beginning_point = (0, 0)
current_angle = 0
angle_rotation = 360 / num_points
current_point = 0

# Determining the angle between each of the vectors
angles = 360 / num_points

# Init the lat/lon dict
df_xy = pd.DataFrame({
    'x': [],
    'y': []
})


for i in range(num_points):


    # Determining what quadrant we are currently in
    current_quadrant = quadrant_update(quadrant_dict=quadrant_dict, current_angle=current_angle)

    x, y = vector_coordinates(current_quadrant=current_quadrant,
                       current_angle=current_angle,
                       beginning_point=beginning_point,
                       radius=radius,
                       quadrant_dict=quadrant_dict)

    df_xy = df_xy.append({'x': x, 'y': y}, ignore_index=True)

    # Updating our angle
    current_angle += angle_rotation

