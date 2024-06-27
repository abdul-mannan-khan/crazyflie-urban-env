import pybullet as p
import pybullet_data
import time

# Connect to PyBullet with a GUI
physicsClient = p.connect(p.GUI)

# Set the gravity for the simulation
p.setGravity(0, 0, -9.81)

# Add PyBullet's default URDF path
p.setAdditionalSearchPath(pybullet_data.getDataPath())

# Load a basic plane to serve as the ground
planeId = p.loadURDF("plane.urdf")

# Load the simple sphere URDF
sphereId = p.loadURDF("simple_sphere.urdf", [0, 0, 3], p.getQuaternionFromEuler([0, 0, 0]))

# Run the simulation
while True:
    p.stepSimulation()
    time.sleep(1/240)  # Simulate at 240 Hz

# Disconnect when done (not reachable in this infinite loop without a break condition)
p.disconnect()
