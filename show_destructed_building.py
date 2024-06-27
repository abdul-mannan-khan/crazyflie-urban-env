import pybullet as p
import pybullet_data
import time

# Connect to PyBullet
p.connect(p.GUI)

# Set the path to the URDF file
urdf_path = "destructed_building.urdf"

# Load the plane
p.setAdditionalSearchPath(pybullet_data.getDataPath())  # To load plane.urdf
p.loadURDF("plane.urdf")

# Load the URDF file
p.loadURDF(urdf_path)

# Set gravity
p.setGravity(0, 0, -9.81)

# Run the simulation for a few seconds
for _ in range(240):
    p.stepSimulation()
    time.sleep(1./240.)

# Keep the simulation window open
input("Press Enter to exit...")
h
# Disconnect from PyBullet
p.disconnect()
