import gym
import numpy as np
from stable_baselines3 import DQN
from stable_baselines3.common.vec_env import DummyVecEnv
from env import Maze

env = Maze()
env = DummyVecEnv([lambda: Maze()])

model = DQN('MlpPolicy', env, verbose=1)
model.learn(total_timesteps=100000)

obs = env.reset()
for i in range(500):
  action, _states = model.predict(obs)
  obs, rewards, dones, info = env.step(action)
  if dones:
    print(rewards)
    print(dones)

model.save("dqn_maze")
