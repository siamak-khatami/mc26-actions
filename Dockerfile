# Loading the base image
# This image is a lightweight linux with Python pre-installed.
# The python version here should match the one used in the project toml file.
FROM python:3.12-slim

# We do not want to copy paste files to the root of the linux in container. 
# So we make a working directory for our application.
# The terminal to run RUN and CMD commands will be set to this working directory.
WORKDIR /app

# Copy the requirements file first to leverage Docker cache for dependencies.
# The cache works line by line, at each line that it detects a change, it will 
# stop using cache for all following lines.
# If we have pip install after copying all files, 
# any change in the code will invalidate the cache for the pip install step.
# Thus after any code change, it will also re-run the pip install step which is useless.
# We want it to be installed whenever the requirements file changes.
COPY ./requirements.txt ./requirements.txt
# Install the dependencies listed in the requirements file.
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code after installing dependencies.
# It will ignore files and directories listed in the .dockerignore file.
COPY . .

# Expose the port that the application will run on.
EXPOSE 8000

# Set the default command to run the application using uvicorn.
CMD ["uvicorn", "main:voting_app", "--host", "0.0.0.0", "--port", "8000", "--reload"]