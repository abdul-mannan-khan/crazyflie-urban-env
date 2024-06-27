import pybullet as p
import pybullet_data
import time
import random
import math
import os

def is_valid_position(new_pos, existing_positions, min_distance):
    """Check if the new position is at least min_distance away from all existing positions."""
    x_new, y_new, _ = new_pos
    for pos in existing_positions:
        x_existing, y_existing, _ = pos
        distance = math.sqrt((x_new - x_existing)**2 + (y_new - y_existing)**2)
        if distance < min_distance:
            return False
    return True

# Connect to PyBullet with a GUI
physicsClient = p.connect(p.GUI)
p.setGravity(0, 0, -9.81)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
planeId = p.loadURDF("plane.urdf")

# Number of each type of cylinder
num_cylinders_per_color = 3  # This will create three of each color

# Paths to individual URDFs repeated for each color
cylinders = ["urdf/red_cylinder.urdf"] * num_cylinders_per_color + \
            ["urdf/orange_cylinder.urdf"] * num_cylinders_per_color + \
            ["urdf/green_cylinder.urdf"] * num_cylinders_per_color

# Minimum distance between any two cylinders
min_distance = 5
max_attempts = 100  # Maximum number of attempts to place each cylinder

# Generate random positions for each cylinder
z_release = 5.0
positions = []
for i in range(len(cylinders)):
    attempts = 0
    while attempts < max_attempts:
        new_pos = [random.uniform(-10, 10), random.uniform(-10, 10), z_release]  # Increased range
        if is_valid_position(new_pos, positions, min_distance):
            positions.append(new_pos)
            break
        attempts += 1
    if attempts == max_attempts:
        print("Failed to place all cylinders without violating distance constraints.")
        break

# Load each cylinder at a random position
for urdf, pos in zip(cylinders, positions):
    if not os.path.exists(urdf):
        print(f"File not found: {urdf}")
    else:
        p.loadURDF(urdf, basePosition=pos, useFixedBase=False)

# Run the simulation loop
while True:
    p.stepSimulation()
    time.sleep(1/240)

# Disconnect when done
p.disconnect()
