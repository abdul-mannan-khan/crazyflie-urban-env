# PyBullet Simulation Environment for Crazyflie Drones

## Overview
This project creates a PyBullet simulation environment designed specifically for testing and evaluating the performance of Crazyflie drones within various predefined zones. The simulation environment uses URDF (Unified Robot Description Format) files to define the physical attributes of obstacles and zones with which the Crazyflie drone interacts. The environment is ideal for developing and testing drone navigation and control algorithms in a controlled yet challenging virtual setting.

### Zone Definitions
- **Red Cylinders:** Represent no-fly zones. Any drone entering this zone will "die," simulating a crash or severe failure scenario.
- **Orange Cylinders:** Indicate not-liked flying zones. Drones entering these zones will be heavily penalized, representing areas that are risky or costly to navigate.
- **Green Cylinders:** Denote allowed flying zones. Drones navigating within these areas will be given positive rewards, encouraging operation within these parameters.

## Installation Requirements
To run the simulation environment, you need to install several dependencies. Ensure you have Python installed on your system, and then install the following packages:

### Dependencies:
- `gymnasium`: A toolkit for developing and comparing reinforcement learning algorithms.
- `stable-baselines3`: A set of reliable implementations of reinforcement learning algorithms in PyTorch.
- `numpy`: A fundamental package for scientific computing with Python.
- `pybullet`: An easy-to-use Python module for physics simulation, robotics, and machine learning.
- `gym-pybullet-drones`: A PyBullet-based gym environment for single and multi-agent reinforcement learning in drone systems.
- `pkg_resources`: A runtime library dependency management functionality, part of `setuptools`.

You can install these packages using pip3 after creating conda environment for Python 3.10:

```bash
pip install gymnasium stable-baselines3 numpy pybullet gym-pybullet-drones
