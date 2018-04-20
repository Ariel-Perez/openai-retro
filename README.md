# OpenAI Retro Contest
Entry for the transfer learning [contest](https://blog.openai.com/retro-contest/) held by OpenAI.

The OpenAI Retro Contest provides a training set of levels from the Sonic The Hedgehog™ series of games, and measures algorithm performance on a test set* of custom levels have created for the contest. The contest runs from April 5th to June 5th 2018.

## Setup
In order to be able to run this code, first go through the [instructions](https://contest.openai.com/details) provided by OpenAI for setting up the environment.

## Register in the contest
After you've registered in the [website](https://contest.openai.com/register), enter your credentials in the `docker-keys.json` file. Your credentials can be found [here](https://contest.openai.com/user).
Make sure to untrack the file in git so you don't end up uploading your credentials.
```bash
git update-index --assume-unchanged docker-keys.json
```

## Running the Code
```bash
python run.py [-h] [-remote]

Run the agent. Defaults to local mode, and displays the screen as the agent plays.

optional arguments:
  -h, --help  show this help message and exit
  -remote     Whether to run on remote mode
```

## Making a Submission
```bash
python submit.py [-h] tag

Submit a script to OpenAI using Docker. Requires `docker-keys.json` to be properly set up.

positional arguments:
  tag         the tag for the submission

optional arguments:
  -h, --help  show this help message and exit
```
