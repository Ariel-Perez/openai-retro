import abc
import random


class Agent(abc.ABC):

    def __init__(self, env):
        self.action_space = env.action_space

    @abc.abstractmethod
    def choose_action(self, obs):
        raise NotImplementedError()


class RandomAgent(Agent):

    def choose_action(self, obs):
        action = self.action_space.sample()
        return action


class SimpleAgent(Agent):

    def choose_action(self, obs):
        action = self.action_space.sample()
        action[7] = 1
        return action


class PseudoRandomAgent(Agent):

    def choose_action(self, obs):
        action = self.action_space.sample()
        rand = random.random()
        if rand > 0.3:
            action[7] = 1

        return action
