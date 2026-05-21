import discord
from discord.ext import commands
from discord import app_commands

from google import genai

import random
import math

from dotenv import load_dotenv
import os

load_dotenv()
t = os.getenv("TOKEN")
k = os.getenv("API_KEY")
if t != None:
    TOKEN = t
if k != None:
    KEY = k

client = genai.Client(api_key=KEY)
MODEL = "gemini-1.5-flash"

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)

    print(f"Logged in as {bot.user}")


# ---------------- ROAST COMMAND ---------------- #

@app_commands.allowed_contexts(
    guilds=True,
    dms=True,
    private_channels=True
)
@bot.tree.command(
    name="roast",
    description="Send a random roast message to someone!"
)
async def roast(interaction: discord.Interaction, member: discord.User):

    roasts = [
        f"{member.mention} smells like expired chicken nuggets 💀",
        f"it has been approximately 931 days since {member.mention} last showered 🚿",
        f"go touch some grass {member.mention} 🙏",
        f"job applications be sitting around the campfire telling stories about {member.mention} 👻",
        f"{member.mention} yo mom really took 9 months to make a joke 🥀"
    ]

    await interaction.response.send_message(
        random.choice(roasts)
    )


# ---------------- INFO COMMAND ---------------- #

@app_commands.allowed_contexts(
    guilds=True,
    dms=True,
    private_channels=True
)
@bot.tree.command(
    name="info",
    description="Get information about the bot"
)
async def info(interaction: discord.Interaction):

    embed = discord.Embed(
        title="🥭 Bot Information",
        description=(
            "I am a totally useful Discord bot created by "
            "@meflamey.dev.\n\n"
            "If I stop working, blame him"
        ),
        color=discord.Color.blue()
    )

    embed.set_footer(
        text=f"Requested by {interaction.user}"
    )

    await interaction.response.send_message(embed=embed)


# ---------------- COMPLIMENT COMMAND ---------------- #

@app_commands.allowed_contexts(
    guilds=True,
    dms=True,
    private_channels=True
)
@bot.tree.command(
    name="compliment",
    description="Send a random compliment to someone!"
)
async def compliment(interaction: discord.Interaction, member: discord.User):

    compliments = [
        f"{member.mention} everybody loves you 💖",
        f"dont you EVER give up, {member.mention} 💪",
        f"{member.mention} go show them what you GOT! 😤",
        f"have a good day, {member.mention} 😁",
        f"{member.mention} good job today! 💯",
        f"take a break, {member.mention} ☺️"
    ]

    await interaction.response.send_message(
        random.choice(compliments)
    )


# ---------------- BIRTHDAY COMMAND ---------------- #

@app_commands.allowed_contexts(
    guilds=True,
    dms=True,
    private_channels=True
)
@bot.tree.command(
    name="birthday",
    description="Wish someone a happy birthday!"
)
async def birthday(
    interaction: discord.Interaction,
    member: discord.User,
    turning: int | None = None
):

    if turning is None:
        await interaction.response.send_message(
            f"🎂 Happy Birthday, {member.mention}!"
        )
    else:
        await interaction.response.send_message(
            f"🎂 Happy Birthday {member.mention}, turning {turning}!"
        )

#-- SAY COMMAND --#
@app_commands.allowed_contexts(
    guilds=True,
    dms=True,
    private_channels=True
)
@bot.tree.command(name="say", description="Make the bot say something")
async def say(
    interaction: discord.Interaction,
    message: str
):
    await interaction.response.send_message(
        message
    )

#-- AVATAR COMMAND --#
@app_commands.allowed_contexts(
    guilds=True,
    dms=True,
    private_channels=True
)
@bot.tree.command(name="avatar", description="Get someone's Discord avatar to download or share")
async def avatar(
    interaction: discord.Interaction,
    user: discord.User
):
    avatar = user.avatar or user.default_avatar

    embed = discord.Embed(
        title=f"{user.display_name}'s Avatar",
        color=discord.Color.green()
    )
    embed.set_image(url=avatar.url)

    await interaction.response.send_message(embed=embed)

#-- BEG COMMAND --#
@app_commands.allowed_contexts(
    guilds=True,
    dms=True,
    private_channels=True
)
@bot.tree.command(name="beg", description="Beg people to use the bot")
async def beg(
    interaction: discord.Interaction
):
    await interaction.response.send_message(
        "Pls use MangoBot please: https://discord.com/oauth2/authorize?client_id=1505167456488915065&permissions=5066929756167745&integration_type=0&scope=bot"
    )

#-- LOVE PERCENTAGE --#
@app_commands.allowed_contexts(
    guilds=True,
    dms=True,
    private_channels=True
)
@bot.tree.command(name="ship", description="Calculate the love percentage for 2 users")
async def ship(
    interaction: discord.Interaction,
    user1: discord.User,
    user2: discord.User
):
    id1 = user1.id
    id2 = user2.id
    seed = id1 + id2
    random.seed(seed)
    percentage = random.randint(0, 100)
    
    if percentage < 25:
        await interaction.response.send_message(
            f"💔 {user1.mention} + {user2.mention} = {percentage}% of love. They don't go well together"
        )

    elif percentage >= 25 and percentage < 50:
        await interaction.response.send_message(
            f"🌹 {user1.mention} + {user2.mention} = {percentage}% of love. Strange pair, but kind of works!"
        )

    elif percentage >= 50 and percentage < 75:
        await interaction.response.send_message(
            f"💖 {user1.mention} + {user2.mention} = {percentage}% of love. Pretty cute together!"
        )

    elif percentage >= 75 and percentage < 90:
        await interaction.response.send_message(
            f"💞 {user1.mention} + {user2.mention} = {percentage}% of love. Now THIS is a solid match 👀"
        )

    elif percentage >= 90 and percentage < 100:
        await interaction.response.send_message(
            f"🔥 {user1.mention} + {user2.mention} = {percentage}% of love. Yall are soulmates fr"
        )

    else:
        await interaction.response.send_message(
            f"💍 {user1.mention} + {user2.mention} = 100% of love. BRO JUST GET MARRIED ALREADY 😭"
        )

#-- 8BALL COMMAND --#
@app_commands.allowed_contexts(
    guilds=True,
    dms=True,
    private_channels=True
)
@bot.tree.command(name="8ball", description="Ask a question to 8 Ball")
async def ball(
    interaction: discord.Interaction,
    question: str
):
    responses = [
        "Yes",
        "No",
        "Maybe",
        "Probably",
        "Sure. Why not?",
        "Probably Not",
        "I don't know",
        "Do what your heart says",
    ]

    choice = random.choice(responses)

    embed = discord.Embed(
        title="🎱 The 8 Ball has decided! 🎱",
        description=choice,
        color=discord.Color.blurple()
    )
    embed.set_footer(text=f"Question: {question}")

    await interaction.response.send_message(embed=embed)

@app_commands.allowed_contexts(
    guilds=True,
    dms=True,
    private_channels=True
)
@bot.tree.command(name="dadjoke", description="Send a random dad joke")
async def dadjoke(
    interaction: discord.Interaction,
):
    dadjokes = [
        "What did the ocean say to the beach? Nothing, it just waved",
        "I only know 25 letters in the alphabet, I don't know Y!",
        "Why don't skeletons fight each other? They don't have the guts",
        "What do you call fake spaghetti? An impasta",
        "Why don't scientists trust atoms? They make up everything!",
        "What do you call cheese that isn't yours? Nacho Cheese!",
        "What's brown and sticky? A stick. What did you think it was?",
        "Why did the golfer bring two pairs of pants? In case he got a hole in one.",
        "Why are elevator jokes so good? They work on many levels.",
        "What do you call a fish wearing a bowtie? Sofishticated.",
        "Why did the coffee file a police report? It got mugged.",
        "Why can't eggs tell jokes? They'd crack each other up."
    ]

    joke = random.choice(dadjokes)

    await interaction.response.send_message(
        f"😂 " + joke
    )

##//-- ROLEPLAY COMMANDS --\\##

#-- SHOOT COMMAND --#

@bot.tree.command(name="shoot", description="Shoot someone")
@app_commands.allowed_contexts(
    guilds=True,
    dms=True,
    private_channels=True
)
async def shoot(
    interaction: discord.Interaction,
    user: discord.User
):
    gifs = [
        "https://media.tenor.com/AGTqt-wXyiEAAAAC/nichijou-minigun.gif",
        "https://media.tenor.com/Uvr8PctYvYcAAAAC/glock-gun.gif",
        "https://media.tenor.com/4vm4NhESp5IAAAAC/kermit-gun.gif",
        "https://media.tenor.com/MkeUMFTlVNcAAAAC/delete-kar.gif",
        "https://media.tenor.com/ABxjgSX8p4YAAAAC/cat-gun.gif",
        "https://media.tenor.com/i3ijQxePt_cAAAAC/gun-gif.gif",
        "https://media.tenor.com/SSUL40mibXwAAAAC/yangyangpls.gif",
        "https://media.tenor.com/rPUs2bveMucAAAAC/tutorial-terry-tutorial.gif"
    ]
    chosen = random.choice(gifs)
    embed = discord.Embed(
        description=f"{interaction.user.mention} just shot {user.mention}! 🔫",
        color=discord.Color.blurple()
    )
    embed.set_image(url=chosen)
    await interaction.response.send_message(embed=embed)

#-- SLAP COMMAND --#

@bot.tree.command(name="slap", description="Slap someone")
@app_commands.allowed_contexts(
    guilds=True,
    dms=True,
    private_channels=True
)
async def slap(
    interaction: discord.Interaction,
    user: discord.User
):
    gifs = [
        "https://media.tenor.com/KC56LsHlsY0AAAAC/cats-cat-slap.gif",
        "https://media.tenor.com/MXZGFeabIIwAAAAC/taiga-toradora.gif",
        "https://media.tenor.com/W2QqtV4k6ykAAAAC/orange-cat-cat-hitting-cat.gif",
        "https://media.tenor.com/eU5H6GbVjrcAAAAC/slap-jjk.gif",
        "https://media.tenor.com/HTHoXnBc400AAAAC/in-your-face-slap.gif",
        "https://media.tenor.com/SQ1N_QKllQQAAAAC/penguin-slap.gif"
    ]
    chosen = random.choice(gifs)
    embed = discord.Embed(
        description=f"{interaction.user.mention} just slapped {user.mention}! 🤚",
        color=discord.Color.blurple()
    )
    embed.set_image(url=chosen)
    await interaction.response.send_message(embed=embed)

#-- PING COMMAND --#
@bot.tree.command(name="ping", description="Check the bot's latency")
@app_commands.allowed_contexts(
    guilds=True,
    dms=True,
    private_channels=True
)
async def ping(
    interaction: discord.Interaction
):
    latency = round(bot.latency * 1000)  # Convert seconds → milliseconds

    embed = discord.Embed(
        title="🏓 Pong!",
        description=f"**Latency:** {latency}ms",
        color=discord.Color.blurple()
    )

    await interaction.response.send_message(embed=embed)

#-- COINFLIP COMMAND --#
@bot.tree.command(name="coinflip", description="Flip a coin")
@app_commands.allowed_contexts(
    guilds=True,
    dms=True,
    private_channels=True
)
async def flip(
    interaction: discord.Interaction
):
    sides = ["Heads 👤", "Tails 🐇"]
    side = random.choice(sides)
    gif = "https://media.tenor.com/9PALsSO_XpsAAAAC/misaka-mikoto.gif"

    embed = discord.Embed(
        title="🪙 Flipping a coin..",
        description=f"It landed on {side}!",
        color=discord.Color.blurple()
    )
    embed.set_image(url=gif)
    embed.set_footer(text=f"Coinflip requested by {interaction.user.display_name}")

    await interaction.response.send_message(embed=embed)

#-- DICE COMMAND --#
@bot.tree.command(name="dice", description="Roll a dice")
@app_commands.allowed_contexts(
    guilds=True,
    dms=True,
    private_channels=True
)
async def dice(
    interaction: discord.Interaction,
    sides: int | None = None
):
    if sides == None:
        sides = 6
        rolled = random.randint(1, sides)
    elif sides >= 2:
        rolled = random.randint(1, sides)
    else:
        await interaction.response.send_message(
            f"Can't roll a dice with less than 2 sides! {interaction.user.mention}"
        )
        return  # stop execution

    gif = "https://media.tenor.com/2JDf6-BMy3cAAAAC/ll-legendary-league.gif"

    embed = discord.Embed(
        title="🎲 Rolling the Dice..",
        description=f"The dice landed on **{rolled}**!",
        color=discord.Color.blurple()
    )
    embed.set_footer(text=f"Dice Roll requested by {interaction.user.display_name} with {sides} sides")
    embed.set_image(url=gif)

    await interaction.response.send_message(embed=embed)

#-- CALCULATE COMMAND--#
@bot.tree.command(name="calc", description="Calculate something")
@app_commands.allowed_contexts(
    guilds=True,
    dms=True,
    private_channels=True
)
async def calc(
    interaction: discord.Interaction,
    equation: str
):

    # Safe evaluation using a restricted environment
    allowed_names = {
        k: v for k, v in math.__dict__.items() if not k.startswith("__")
    }
    allowed_names.update({"abs": abs, "round": round, "min": min, "max": max})

    # Block any unsafe characters/keywords
    blocked = ["import", "exec", "eval", "open", "os", "sys", "__"]
    for word in blocked:
        if word in equation.lower():
            await interaction.response.send_message(
                "❌ That equation contains disallowed terms.", ephemeral=True
            )
            return

    try:
        # Replace ^ with ** for exponentiation
        sanitized = equation.replace("^", "**")

        result = eval(sanitized, {"__builtins__": {}}, allowed_names)

        await interaction.response.send_message(
            f"🧮 **Equation:** `{equation}`\n📊 **Result:** `{result}`"
        )

    except ZeroDivisionError:
        await interaction.response.send_message(
            "❌ Division by zero is undefined.", ephemeral=True
        )
    except Exception as e:
        await interaction.response.send_message(
            f"❌ Invalid equation: `{e}`", ephemeral=True
        )

#//-- AI SECTION --\\#

#-- ASKAI COMMAND --#
@bot.tree.command(name="ai", description="Ask something to Gemini 1.5 Flash")
@app_commands.allowed_contexts(
    guilds=True,
    dms=True,
    private_channels=True
)
async def ai(
    interaction: discord.Interaction,
    prompt: str
):
    response = client.models.generate_content(
        model=MODEL,
        contents=prompt,
    )

    if response:
        embed = discord.Embed(
            description=response,
            color=discord.Color.blurple()
        )
        embed.set_footer(text="Gemini 1.5 Flash • AI Generated response")

        await interaction.response.send_message(embed=embed)
    else:
        await interaction.response.send_message(content=f"Failed to generate a response, please try again later.", ephemeral=True)
    

bot.run(TOKEN)