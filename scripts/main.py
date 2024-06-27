import pybullet as p
import pybullet_data
import time
import random

# Connect to PyBullet with a GUI
physicsClient = p.connect(p.GUI)
p.setGravity(0, 0, -9.81)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
planeId = p.loadURDF("plane.urdf")

# Number of each type of cylinder
num_cylinders_per_color = 3  # This will create three of each color

# Paths to individual URDFs repeated for each color
cylinders = ["/urdf/red_cylinder.urdf"] * num_cylinders_per_color + \
            ["/urdf/orange_cylinder.urdf"] * num_cylinders_per_color + \
            ["/urdf/green_cylinder.urdf"] * num_cylinders_per_color

# Generate random positions for each cylinder
positions = [[random.uniform(-5, 5), random.uniform(-5, 5), 3] for _ in range(len(cylinders))]

# Load each cylinder at a random position
for urdf, pos in zip(cylinders, positions):
    p.loadURDF(urdf, basePosition=pos, useFixedBase=False)

# Run the simulation loop
while True:
    p.stepSimulation()
    time.sleep(1/240)

# Disconnect when done
p.disconnect()
