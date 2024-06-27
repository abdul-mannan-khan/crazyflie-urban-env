import pybullet as p
import pybullet_data
import time


# Connect to PyBullet
physicsClient = p.connect(p.GUI)
p.setGravity(0, 0, -10)

# Set the path to where PyBullet URDFs are located
p.setAdditionalSearchPath(pybullet_data.getDataPath())

# Load the ground plane
planeId = p.loadURDF("plane.urdf")

# Load your city URDF
# Make sure the path to your URDF is correct; if it's in the same directory, just use the filename
cityId = p.loadURDF("city_with_flying_zones.urdf")

while True:
    p.stepSimulation()
    time.sleep(1./240.)


# Keep the simulation window open
input("Press Enter to exit...")

# Disconnect from PyBullet
p.disconnect()
