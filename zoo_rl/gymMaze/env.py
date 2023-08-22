import gym 
from numpy import random
import time

class Maze(gym.Env):
    def __init__(self) -> None:
        super().__init__()
        # 0: up, 1: right, 2: down, 3: left
        self.action_space = gym.spaces.Discrete(4)
        # 0 ~ 15
        self.observation_space = gym.spaces.Box(low=0, high=3, shape=(2,), dtype=int)
        # state: [x, y]
        self.state = [0,0]
        self.step_num = 0
        self.max_step = 1000
        self.reward = 0
        self.done = False
        self.info = {}
        self.map = [
            [0, 0, 0, 0],
            [1, 1, 0, 1],
            [0, 0, 0, 0],
            [1, 0, 1, 1]
        ]
    
    def reset(self):
        self.state = [0, 0]
        self.step_num = 0
        self.reward = 0
        self.done = False
        self.info = {}
        return self.state

    def step(self, action):
        self.step_num += 1
        pre_state = self.state.copy()

        if action == 0:
            self.state[0] -= 1
        elif action == 1:
            self.state[1] += 1
        elif action == 2:
            self.state[0] += 1
        elif action == 3:
            self.state[1] -= 1
        
        if self.state[0] < 0:
            self.state[0] = 0
        elif self.state[0] > 3:
            self.state[0] = 3
        if self.state[1] < 0:
            self.state[1] = 0
        elif self.state[1] > 3:
            self.state[1] = 3

        
        if self.map[self.state[0]][self.state[1]] == 1:
            self.state = pre_state
            self.reward -= 2
        else:
            self.reward -= 1
        
        if self.state == [2, 3]:
            self.reward = 100
            self.done = True

        if self.step_num >= self.max_step:
            self.done = True
        return self.state, self.reward, self.done, self.info
    
    def render(self):
        for i in range(4):
            for j in range(4):
                if self.state == [i, j]:
                    print("o", end=" ")
                elif self.map[i][j] == 1:
                    print("#", end=" ")
                else:
                    print(".", end=" ")
            print()
        print()
        time.sleep(0.5)


if __name__ == "__main__":
    env = Maze()
    env.reset()
    env.render()
    for i in range(100):
        action = random.randint(0, 4)
        state, reward, done, info = env.step(action)
        print(state)
        # env.render()
        if done:
            break
    print("End")