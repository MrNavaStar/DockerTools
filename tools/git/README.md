# Git
A docker container configured to pull code from a git repo for real time development.

## Usage
Copy `update.sh` to the root of your project.

Your code will need a way to trigger `update.sh`. You could do this through with a webhook
or something else external from the container. You could also run the script periodically with
a cron job or something similar.

Inside `update.sh` you must set the following variables:
```bash
# The command to restart your application after updating
start_cmd="./program.sh"
# The branch you want the container to pull from
repo_branch="origin/master"
```

You can use the provided debian Dockerfile, but more likely you'll have you own.
The important parts are as follows:
```dockerfile
# Install git
RUN apt-get update
RUN apt-get install git

# Setup app dir
COPY . /app
WORKDIR /app

# Setup the local git repo
RUN git init -b master
RUN git remote add origin $REPO_URL

# Give update.sh permission to run
RUN chmod +x update.sh
```

## Notice

Docker isn't really intended to be used in this fashion, so there are probably some major security
flaws with this approach. Don't use this for anything that is very important.