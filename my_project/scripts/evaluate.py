import gymnasium as gym
from stable_baselines3 import PPO
from custom_envs.flythrugate_aviary import FlyThruGateAviary
from gymnasium.envs.registration import register

# Import or define the shared constants
class shared_constants:
    AGGR_PHY_STEPS = 5

# Register the custom environment
register(
    id='FlyThruGateAviary-v0',
    entry_point='custom_envs.flythrugate_aviary:FlyThruGateAviary',
)

# Define the environment name
env_name = 'FlyThruGateAviary-v0'

# Parameters for the environment
aggregate_phy_steps = shared_constants.AGGR_PHY_STEPS
obs = "some_observation_parameter"
act = "some_action_parameter"

# Create the evaluation environment
eval_env = gym.make(env_name, aggregate_phy_steps=aggregate_phy_steps, obs=obs, act=act)

# Load the trained model
model = PPO.load("ppo_flythrugate_aviary")

# Evaluate the trained model
observation, info = eval_env.reset()
done = False

while not done:
    eval_env.render()  # Render the environment (optional)
    action, _states = model.predict(observation, deterministic=True)
    observation, reward, done, truncated, info = eval_env.step(action)

eval_env.close()  # Close the environment
