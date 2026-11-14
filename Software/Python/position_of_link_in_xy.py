import math

L = 20 # this is the length of the link
theta_degrees = 30 # this is the "joint angle"  or angle of rotation

theta = math.radians(theta_degrees)

x = L * math.cos(theta)
y = L * math.sin(theta)

print(f"x = {x}")
print(f"y = {y}")