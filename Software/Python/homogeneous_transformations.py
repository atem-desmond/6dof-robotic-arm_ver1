import numpy as np

# Rotation around Z by 90 degrees
theta = np.radians(90)

Rz = np.array([
    [np.cos(theta), -np.sin(theta), 0],
    [np.sin(theta),  np.cos(theta), 0],
    [0,              0,             1]
])

# Translation
p = np.array([50, 30, 0])

# Construct homogeneous transformation
T = np.eye(4) # np.eye returns a 2D array with 1s in diagonal and 0 else where. 4 is the number of rows


T[:3, :3] = Rz # A 3×3 section
T[:3, 3] = p

# Original point
P = np.array([100, 0, 0, 1])

# Transform point
P_new = T @ P

print(P_new)