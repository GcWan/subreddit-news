# RSS2Reddit

![GitHub release (latest by date)](https://img.shields.io/github/v/release/georgecwan/rss2reddit?sort=semver)
![MIT License](https://img.shields.io/github/license/georgecwan/rss2reddit)

### Description

This script will post the latest news (title and link) from RSS feeds to subreddits of your choice. Each subreddit can
be configured with multiple lists of RSS feeds. The script will go through each feed in each list and listen to them
one at a time. While listening, the script will check the RSS feed for new items every 30 minutes. If a new item is
found, the script will post the new item's url address in the corresponding subreddit. *(Note: only links added to the
RSS feed **after** the script begins listening will be posted)* After posting, the script will not check the RSS feed
for new links and any updates to the RSS feed will be ignored until the script begins listening to the RSS feed again.
To better understand the functionalities of this script, please read
the [Config Documentation](https://github.com/georgecwan/rss2reddit/wiki/V3-Config-Documentation)
in the wiki.

Note: You should only use this on subreddits that you moderate. Make sure you do not break Reddit's terms of service or
subreddit rules while using this script.

## Table of Contents

- [Setup Steps](#getting-started)
    - [Register App on Reddit](#register-app-on-reddit)
    - [Set up Environment Variables](#set-up-environment-variables)
    - [Configuring the Script](#configuring-the-script)
- [Running the Script](#running-the-script)
    - [Option 1: Local Python Installation](#option-1-local-python-installation)
    - [Option 2: Docker Compose](#option-2-docker-compose)
- [Setting up a Discord Webhook](#setting-up-a-discord-webhook)
- [Useful Links](#useful-links)

## Getting Started

Download the desired [release of this repository](https://github.com/GcWan/rss2reddit/releases) and unzip it on
your own computer.

### Register app on Reddit

- You will need your own reddit account.
- Login to reddit and access account settings [here](https://www.reddit.com/prefs/apps/).
- Scroll to bottom and click button to create app. (Click "are you a developer" if necessary.)
- Fill out form as follows:
    - Name: RSS2Reddit by /u/GeoWa
    - App type: script
    - Redirect uri: http://localhost
- The remaining fields are optional.
- Click "create app".
- Copy down the client id (found under the text "Personal Use Script"
  and client secret (beside the text "secret"). You will need these later.

### Set up environment variables

#### .env file format

```dotenv
USER_NAME=your_reddit_username
PASSWORD=your_reddit_password
CLIENT_ID=your_client_id
CLIENT_SECRET=your_client_secret
DISCORD_WEBHOOK_URL=your_discord_webhook_url
```

- Create a file named ".env" in your local rss2reddit folder
    - You can also directly rename the `env.example` file to `.env`
- Open the file in a text editor of your choice and use the format above to fill in the following fields:
    - Replace `your_reddit_username` with your Reddit account's username
    - Replace `your_reddit_password` with your Reddit account's password
    - Replace `your_client_id` and `your_client_secret` with the client id and secret you copied from in
      the [previous step](#register-app-on-reddit).
- If you would like to receive notifications about new posts in a Discord server, you can set up a Discord webhook.
  Follow the steps in the [Setting up a Discord Webhook](#setting-up-a-discord-webhook) section to set up a Discord
  webhook. Otherwise, you can delete the `DISCORD_WEBHOOK_URL=` line from the `.env` file.

**KEEP THE .ENV FILE PRIVATE. DO NOT SHARE WITH ANYONE ELSE.**

### Configuring the script

#### Config.yaml format

```yaml
---
- name: mysubreddit1
  cycles:
    - feeds:
        - url: https://example.com/feed1.rss
      check_interval: 3600
      flair: Flair
```

- Copy (or rename) the `config.example.yaml` file to `config.yaml` and open it in a text editor of your choice.
- The format above is an example that posts from one RSS feed to one subreddit.
    - Replace `mysubreddit1` with the name of the subreddit you want to post to.
    - Replace `https://example.com/feed1.rss` with the URL of the RSS feed you want to listen to.
    - Most URLs can be directly pasted, but you may have to surround it with quotation marks
      if it contains special characters.
    - The entry can be copied and pasted multiple to add more feeds and subreddits.
- The `check_interval` parameter should be a positive integer representing how many seconds the program waits before
  listening to RSS feed for updates.
    - The flair parameter is optional. If you want to add a flair to your posts, enter the text you want to use as
      flair.
      Otherwise, do not include the flair parameter in your config file.
- Make sure that the config.yaml file is indented correctly. The indentation should be 2 spaces (not a tab) for each
  level.
  The program will not be able to read the config file if the indentation is incorrect.

The script can also be configured with multiple RSS feeds for each subreddit, different check intervals per feed, and a
list of blocked words for each RSS feed. For more detailed instructions, check out
the [wiki](https://github.com/GcWan/rss2reddit/wiki).

## Running the Script

You can run the script using either a Python 3 environment or a Docker container.

### Option 1: Local Python Installation

#### Step 1: Install Python dependencies

This step only needs to be completed **_once_**. If you have completed this step before, skip
to [Step 2](#step-2-start-the-script).

- Install Python 3.9 or higher [here](https://www.python.org/downloads/)
    - Select the option to add Python to path during installation if it appears
    - If you have a pre-existing installation of Python 3.9 or higher, you do not have to reinstall it.
- Open your command-line app (e.g. Powershell, Terminal, etc.)
- Type `python --version` and press enter. Make sure that the Python version shown is 3.9 or higher. You may need to
  download a newer version of Python otherwise.
    - If the Python version is shown to be Python 2, you might have to run the same command with `python3` instead
      of `python` (i.e. `python3 --version`). If the correct command `python3`, Make sure to use the `python3` command
      for all future commands as well.
- Navigate to your local copy of the rss2reddit folder: `cd PATH_TO_FOLDER`
    - If you are unsure about the path, dragging the folder into the command line interface might paste the path in for
      you. On some platforms, you can also right-click the folder and select "Copy as path".
- Create a virtual environment: `python -m venv venv`
    - Activate the virtual environment: `venv\Scripts\activate.bat` (Windows CMD) or `source venv/bin/activate`
      (Mac/Linux)
    - It should say (venv) at the beginning of the command line prompt if the virtual environment is active.
    - If you encounter errors trying to create the virtual environment, you can find links to helpful tutorials in
      the [Useful Links](#useful-links) section.
- Install dependencies from requirements.txt: `python -m pip install -r requirements.txt`

#### Step 2: Start the script

- Navigate to your local copy of the rss2reddit folder: `cd PATH_TO_FOLDER`
- Activate the virtual environment: `venv\Scripts\activate.bat` (Windows CMD)
  or `source venv/bin/activate` (
  Mac/Linux)
- Run script: `python main.py` or `python3 main.py`
    - You should start to see output in the command line interface indicating that the script is running.
    - Note that the script will probably terminate if you close the command line interface. If you want to run the
      script in the background, you can use a tool like `screen` or `tmux` on Mac/Linux or `start` on Windows.
- Stop the script with Ctrl-C
- Note that the script has to be restarted to reflect any changes made inside the folder, including changes to
  config.yaml.

### Option 2: Docker Compose

#### Step 1: Installing Docker

This step only needs to be completed **_once_**. If you have completed this step before, skip
to [Step 2](#step-2-start-the-docker-container).

- Install Docker [here](https://docs.docker.com/get-docker/)
- *Optional:* When you run the Docker container, it will use UTC time by default. If you want the program to
  display your own timezone, follow the steps below:
    - Look up your timezone's TZ database name
      [here](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones)
    - Open `docker-compose.yaml` in a text editor of your choice
    - Enter your own timezone's TZ database name after the `TZ=`
        - E.g. `- TZ=America/New_York`

#### Step 2: Start the Docker Container

- Open your command-line app (e.g. Powershell, Terminal, etc.)
- Navigate to your local copy of the rss2reddit folder: `cd PATH_TO_FOLDER`
    - If you are unsure about the path, dragging the folder into the command line interface might paste the path in for
      you. On some platforms, you can also right-click the folder and select "Copy as path".
- Run the Docker container using Docker Compose: `docker compose up`
    - If you have made changes to `config.yaml` since the last time you ran the command,
      run `docker compose up -d --build` to rebuild the image. Otherwise, the script will use the old config file.
    - The script will terminate if you close the command line interface. If you want to run the script in the
      background,
      you can add the `-d` flag to the command: `docker compose up -d`
- Stop the script with Ctrl-C or by running `docker compose down` if you used the `-d` flag.

## Setting up a Discord Webhook

If you would like to receive notifications about new posts in a Discord server, you can set up a Discord webhook.
These steps are completely optional and the script will still work without a Discord webhook.

- Go to the server settings of your Discord server
- Find the "Integrations" section and click "Webhooks"
- Click "Create Webhook"
- Give the webhook a name and assign it to the channel you would like to receive notifications in
- Copy the webhook URL
- Open the `.env` file in a text editor of your choice
- Paste the webhook URL on a new line with the format `DISCORD_WEBHOOK_URL=your_discord_webhook_url`
- Restart the script. If the webhook is set up correctly, you should receive a message in the Discord channel
  you assigned the webhook to.

# Useful Links

- [Reddit Help](https://www.reddithelp.com/hc/en-us)
- [Reddit Bottiquette](https://www.reddit.com/wiki/bottiquette/)
- [Python Virtual Environments Primer](https://realpython.com/python-virtual-environments-a-primer/)
- [Docker Documentation](https://docs.docker.com/)
- [Docker Compose Documentation](https://docs.docker.com/compose/)
