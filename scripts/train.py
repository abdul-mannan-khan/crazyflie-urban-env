import sys
import os

# Add the project directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import gymnasium as gym
from stable_baselines3 import PPO
from custom_envs.flythrugate_aviary import FlyThruGateAviary

# Import or define the shared constants
class shared_constants:
    AGGR_PHY_STEPS = 5

# Define the environment name
env_name = 'FlyThruGateAviary-v0'

# Parameters for the environment
aggregate_phy_steps = shared_constants.AGGR_PHY_STEPS
obs = "some_observation_parameter"
act = "some_action_parameter"

# Create the training environment
train_env = gym.make(env_name, aggregate_phy_steps=aggregate_phy_steps, obs=obs, act=act)

# Create the PPO model
model = PPO("MlpPolicy", train_env, verbose=1)

# Train the model
model.learn(total_timesteps=10000)

# Save the model
model.save("ppo_flythrugate_aviary")
