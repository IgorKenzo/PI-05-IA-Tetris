import time
import numpy as np
from nes_py.wrappers import JoypadSpace
import gym_tetris
from gym_tetris.actions import MOVEMENT

from wrappers import wrapper
from DQNAgent import DQNAgent

# Build env (first level, right only)
env = gym_tetris.make('TetrisA-v3')
env = JoypadSpace(env, MOVEMENT)
env = wrapper(env)
# Parameters
states = (84, 84, 4)
actions = env.action_space.n
# Agent
agent = DQNAgent(states=states, actions=actions, max_memory=10000, double_q=False)
# Episodes
episodes = 10000
rewards = []
# Timing
start = time.time()
step = 0
# Main loop
for e in range(episodes):
    # Reset env
    state = env.reset()
    # Reward
    total_reward = 0
    iter = 0
    # Play
    while True:
        # Show env (disabled)
        env.render()
        # Run agent
        action = agent.run(state=state)
        # Perform action
        next_state, reward, done, info = env.step(action=action)
        # Remember transition
        agent.add(experience=(state, next_state, action, reward, done))
        # Update agent
        agent.learn()
        # Total reward
        total_reward += reward
        # Update state
        state = next_state
        # Increment
        iter += 1
        # If done break loop
        if done: #or info['flag_get']:
            break
    # Rewards
    rewards.append(total_reward / iter)
    # Print
    if e % 100 == 0:
        print('Episode {e} - +'
              'Frame {f} - +'
              'Frames/sec {fs} - +'
              'Epsilon {eps} - +'
              'Mean Reward {r}'.format(e=e,
                                       f=agent.step,
                                       fs=np.round((agent.step - step) / (time.time() - start)),
                                       eps=np.round(agent.eps, 4),
                                       r=np.mean(rewards[-100:])))
        start = time.time()
        step = agent.step

    if e % 500 == 0:
      np.save(f'rewards{e/500}.npy', rewards)      
# Save rewards
np.save('rewards.npy', rewards)

    # action = agent.run(state=state)
    # # Perform action
    # next_state, reward, done, info = env.step(action=action)
    # print(info)
