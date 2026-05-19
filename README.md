<p align="center">
<h1>MangoBot</h1>
Source code for my Discord bot called MangoBot. Feel free to use it to make your own bot.
</p>

## Make your Own Bot

### 1. Fork the Repo

Fork this repository and open it in VS Code or any other IDE you have installed.
Edit the [code](main.py) if required to add more commands or edit commands, etc.

### 2. Install requirements

Install the dependencies from [requirements.txt](requirements.txt) using `pip`:

```sh
pip install discord.py
pip install python-dotenv
```

### 3. Configure .env

Create a new file in the root directory named `.env`
Edit the contents of this file to include your bot token:

```env
TOKEN=YOUR_BOT_TOKEN_HERE
```

You can get your bot token by going to [your discord app](https://www.discord.com/developers/applications) and click on `Bot` on the left sidebar. Now find the **Token** section and click **View Token** or **Reset Token**. Keep the token in your .env file and update it whenever you reset the token.

### 4. Test the bot

You have to authorize the bot now to test it.
Go over to your Application on the Discord developer portal and click on OAuth2 on the sidebar. Select `bot` and `applications.commands` Then copy the generated link.
Paste the link in your browser and add the bot to a server

Now to bring your Bot online and use the commands, open up the terminal in VS Code and run `main.py`:

```shell
python main.py
```

Now back in the discord server, try using commands.

### 5. Host the Bot

If we want the Bot to work at all times and stay online, we have to host it somewhere.
This specific Bot is hosted on [Discloud.com](https://discloud.com) which offers for free:

- 100MB of RAM
- 0.25 vCPUs AMD Epyc
- Unlimited bandwith
- Enterprise NVMe SSD

To host it on Discloud, you need to create a `requirements.txt` file and a `discloud.config` file.

The `discloud.config` file should be structured like this:

```config
NAME=YourBotName
MAIN=the_main_script.py
TYPE=bot
RAM=100
```

The `requirements.txt` file should just contain all the packages used, each one seperated in new lines:

```txt
discord.py
python-dotenv
```

Now just simply zip the entire folder, and upload it to Discloud to make the Bot live.

If you need to update the bot, make the edits on your computer and then upload the updated file in the "Commit" section for the Bot, it will automatically update the file.
