#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Run script."""
import agents
import argparse


def create_environment(remote):
    return grc.RemoteEnv('tmp/sock') if remote else \
        local.make(
            game='SonicTheHedgehog-Genesis',
            state='LabyrinthZone.Act1'
        )


def create_agent(env):
    return agents.PseudoRandomAgent(env)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Run the agent')
    parser.add_argument('-remote', action='store_true', help='whether to run on remote mode')

    args = parser.parse_args()

    if args.remote:
        import gym_remote.exceptions as gre
        import gym_remote.client as grc
    else:
        import retro_contest.local as local

    try:
        env = create_environment(args.remote)
        agent = create_agent(env)

        obs = env.reset()
        while True:
            act = agent.choose_action(obs)
            obs, rew, done, _ = env.step(act)
            if not args.remote:
                env.render()
            if done:
                env.reset()

    except Exception as e:
        print('exception', e)
