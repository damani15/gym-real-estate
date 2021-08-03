import gym

from gym import error, spaces, utils
from gym.utils import seeding
from gym import Env
from gym.spaces import Discrete, Box
import numpy as np
import random

class RealEstateEnv(Env):
    def __init__(self):
        # Actions we can take, lower price, same price, increase price
        self.action_space = Discrete(3)
        # House prices array
        self.observation_space = Box(low=np.array([100000]), high=np.array([1100000]))
        # Set start price
        self.state = 450000 + random.randint(-100000,100000)
        # Set finding length
        self.finding_length = 180
        
        self.low_price = random.randint(300000, 500000)
        self.high_price = random.randint(self.low_price, (int)(self.low_price * 1.1))
        
    def step(self, action):
        # Apply action
        if action == 0:
            self.state -= 10000
        elif action == 2:
            self.state += 10000
        
        # Reduce house finding length by 1 second
        self.finding_length -= 1
        
        # Calculate reward
        if self.state >= self.low_price and self.state <= self.high_price: 
            reward = 1
        else:
            reward = -1
        
        # Check if finding time is over
        if self.finding_length <= 0: 
            done = True
        else:
            done = False
        
        # Apply price fluctuations
        # self.state += random.randint(-10000,25000)
        # Set placeholder for info
        info = {}
        
        # Return step information
        return self.state, reward, done, info

    def render(self):
        # Implement viz
        pass
    
    def reset(self):
        # Reset shower temperature
        self.state = 450000 + random.randint(-100000,100000)
        # Reset shower time
        self.finding_length = 180
        return self.state