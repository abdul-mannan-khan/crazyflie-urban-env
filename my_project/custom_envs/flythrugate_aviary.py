import gymnasium as gym
from gymnasium import spaces
import numpy as np

class FlyThruGateAviary(gym.Env):
    def __init__(self, aggregate_phy_steps, obs, act):
        super(FlyThruGateAviary, self).__init__()
        self.aggregate_phy_steps = aggregate_phy_steps
        self.obs = obs
        self.act = act
        # Define action and observation space
        self.action_space = spaces.Discrete(2)
        self.observation_space = spaces.Box(low=0, high=1, shape=(4,), dtype=np.float32)

    def reset(self):
        # Reset the state of the environment to an initial state
        return self.observation_space.sample(), {}

    def step(self, action):
        # Execute one time step within the environment
        observation = self.observation_space.sample()
        reward = 1.0
        done = False
        info = {}
        return observation, reward, done, False, info

    def render(self, mode='human'):
        # Render the environment to the screen
        pass

    def close(self):
        # Clean up any resources when the environment is closed
        pass
