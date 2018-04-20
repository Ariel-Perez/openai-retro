# Use OpenAI's base as a parent image
FROM openai/retro-agent

# Add the current files
ADD src .

# Command to run when starting the container
CMD ["python", "-u", "/root/compo/run.py -remote"]
