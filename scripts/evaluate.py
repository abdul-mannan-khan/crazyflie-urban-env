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

# Create the evaluation environment
eval_env = gym.make(env_name, aggregate_phy_steps=aggregate_phy_steps, obs=obs, act=act)

# Load the trained model
model_path = "ppo_flythrugate_aviary.zip"
if not os.path.exists(model_path):
    model_path = "ppo_flythrugate_aviary"  # Fallback to directory format

model = PPO.load(model_path)

# Evaluate the trained model
observation, info = eval_env.reset()
done = False

while not done:
    eval_env.render()  # Render the environment (optional)
    action, _states = model.predict(observation, deterministic=True)
    observation, reward, done, truncated, info = eval_env.step(action)

eval_env.close()  # Close the environment
