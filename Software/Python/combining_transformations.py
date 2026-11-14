import numpy as np

def transform(theta, length):
    theta = np.radians(theta)

    T = np.array([
        [np.cos(theta), -np.sin(theta), 0, length*np.cos(theta)],
        [np.sin(theta),  np.cos(theta), 0, length*np.sin(theta)],
        [0,              0,             1, 0],
        [0,              0,             0, 1]
    ])

    return T

# Link lengths
L1 = 100
L2 = 80

# Joint angles
theta1 = 30
theta2 = 45

# Individual transformations
T01 = transform(theta1, L1)
T12 = transform(theta2, L2)

# Combined transformation
T02 = T01 @ T12

# End-effector position
print(T02[:3, 3])