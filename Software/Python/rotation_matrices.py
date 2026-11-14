import numpy as np

def Rx(theta):
    return np.array([
        [1, 0, 0],
        [0, np.cos(theta), -np.sin(theta)],
        [0, np.sin(theta), np.cos(theta)]
    ])

def Ry(theta):
    return np.array([
        [np.cos(theta), 0, np.sin(theta)],
        [0, 1, 0],
        [-np.sin(theta), 0, np.cos(theta)]
    ])

def Rz(theta):
    return np.array([
        [np.cos(theta), -np.sin(theta), 0],
        [np.sin(theta), np.cos(theta), 0],
        [0, 0, 1]
    ])

# Point on the robot arm
p = np.array([100, 0, 0])

# Rotate 45 degrees around Z then 30 degrees around Y
theta1 = np.radians(45) #np.sin and np.cos take radians
theta2 = np.radians(30) 
R = Ry(theta2) @ Rz(theta1)

# Calculate new position
p_new = R @ p
print(p_new)
print(np.linalg.norm(p_new))