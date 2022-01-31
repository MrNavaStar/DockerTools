# Discord Bot
This is an example of a discord bot using this tool.

## Usage

If you want to test this project, you will need to create a `.env` file that contains the following:
```dotenv
DISCORD_BOT_TOKEN=tokenstring
```
You probably also want to point the Dockerfile to use your own repo instead of this one:
```dockerfile
RUN git remote add origin $YOUR_OWN_REPO
```
Then build the container and your off to the races. The bot will update from the repo when you say `!update` in any channel.
