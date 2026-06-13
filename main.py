import discord
from discord.ext import commands
from discord import app_commands

from google import genai

# import stuff
import random
import math
import re
import time
import asyncio
import tempfile

# .env
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv("TOKEN") or ""
KEY = os.getenv("GEMINI_API_KEY")

# setup for AI
client = genai.Client(api_key=KEY)
MODEL = "gemini-2.5-flash"

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
        f"{member.mention} yo mom really took 9 months to make a joke 🥀",
        f"{member.mention} put the fries in the bag lil bro 🍟",
        f"if you ever feel useless, just remember {member.mention} exists 😭",
        f"{member.mention} go look in the mirror 🪞"
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
async def botinfo(interaction: discord.Interaction):

    embed = discord.Embed(
        title="🥭 Bot Information",
        description=(
            "MangoBot v1.0.0 \n"
            "Created by @meflamey.dev \n"
        ),
        color=discord.Color.orange()
    )
    embed.add_field(
    name="🔗 Useful Links",
    value=(
        "[Website](https://flameydev.github.io/mangobot)\n"
        "[Support Server](https://discord.gg/VBJ4xHYytM)"
    ),
    inline=False
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
        f"take a break, {member.mention} ☺️",
        f"you look amazing, {member.mention}! 🪞",
        f"{member.mention} the gifted 🎁",
        f"you are 1 in a million, {member.mention}! ✨"
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
    age: int | None = None
):

    if age is None:
        await interaction.response.send_message(
            f"🎂 Happy Birthday, {member.mention}!"
        )
    else:
        await interaction.response.send_message(
            f"🎂 Happy Birthday {member.mention}, turning {age}!"
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
    message: str,
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
        color=discord.Color.blurple()
    )
    embed.set_image(url=avatar.url)
    embed.set_footer(text="/avatar")

    await interaction.response.send_message(embed=embed)

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
        "DEFINITELY",
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
        "What did the ocean say to the beach? Nothing, it just waved.",
        "I only know 25 letters in the alphabet, I don't know Y!",
        "Why don't skeletons fight each other? They don't have the guts.",
        "What do you call fake spaghetti? An impasta.",
        "Why don't scientists trust atoms? They make up everything!",
        "What do you call cheese that isn't yours? Nacho cheese!",
        "What's brown and sticky? A stick. What did you think it was?",
        "Why did the golfer bring two pairs of pants? In case he got a hole in one.",
        "Why are elevator jokes so good? They work on many levels.",
        "What do you call a fish wearing a bowtie? Sofishticated.",
        "Why did the coffee file a police report? It got mugged.",
        "Why can't eggs tell jokes? They'd crack each other up.",
        "Why did the scarecrow win an award? Because he was outstanding in his field.",
        "What do you call a bear with no teeth? A gummy bear.",
        "Why did the math book look sad? It had too many problems.",
        "Why don't oysters donate to charity? Because they're shellfish.",
        "What do you call a sleeping bull? A bulldozer.",
        "Why couldn't the bicycle stand up by itself? It was two tired.",
        "Why did the tomato blush? Because it saw the salad dressing.",
        "What do you call a factory that makes okay products? A satisfactory.",
        "Why did the computer go to therapy? It had too many bytes from the past.",
        "Why did the cookie go to the doctor? Because it felt crummy.",
        "What kind of shoes do ninjas wear? Sneakers.",
        "What do you call a cow with no legs? Ground beef.",
        "Why don't programmers like nature? Too many bugs.",
        "What do you call a dinosaur with an extensive vocabulary? A thesaurus.",
        "Why did the banana go to the hospital? It wasn't peeling well.",
        "Why did the student eat his homework? The teacher said it was a piece of cake.",
        "What do you call an alligator in a vest? An investigator.",
        "Why was the broom late? It swept in.",
        "Why did the chicken join a band? Because it had the drumsticks.",
        "What do you call a pile of cats? A meowtain.",
        "Why are ghosts bad liars? Because you can see right through them.",
        "What do you call a boomerang that won't come back? A stick.",
        "Why did the orange stop rolling? It ran out of juice.",
        "What did one wall say to the other wall? I'll meet you at the corner.",
        "Why was the belt arrested? For holding up the pants.",
        "Why did the man put his money in the freezer? He wanted cold hard cash.",
        "What did the janitor say when he jumped out of the closet? Supplies!",
        "Why don't seagulls fly over the bay? Because then they'd be bagels.",
        "Why was the stadium so cool? It was filled with fans.",
        "What do you call a snowman with a six-pack? An abdominal snowman.",
        "Why did the frog take the bus to work? His car got toad away.",
        "What do you call a dog magician? A labracadabrador.",
        "Why did the duck get promoted? Because he was always quacking good ideas.",
        "What did the grape do when it got stepped on? Nothing, it just let out a little wine.",
        "Why can't your nose be 12 inches long? Because then it would be a foot.",
        "What do you call a nervous javelin thrower? Shakespeare.",
        "Why did the barber win the race? He knew a shortcut.",
        "What do you call a lazy kangaroo? A pouch potato.",
        "Why do cows wear bells? Because their horns don't work.",
        "What kind of tree fits in your hand? A palm tree.",
        "Why did the invisible man turn down the job offer? He couldn't see himself doing it.",
        "What do you call a magical dog? A labracadabrador.",
        "Why don't crabs give to charity? Because they're shellfish.",
        "Why did the music teacher need a ladder? To reach the high notes.",
        "What do you call a can opener that doesn't work? A can't opener.",
        "Why was the calendar afraid? Its days were numbered.",
        "Why did the smartphone need glasses? It lost its contacts.",
        "Why don't mountains get cold in winter? They wear snowcaps.",
        "What did the buffalo say to his son when he left? Bison.",
        "Why are fish so smart? Because they live in schools.",
        "What do you call an elephant that doesn't matter? An irrelephant.",
        "Why did the melon jump into the lake? It wanted to be a watermelon.",
        "What kind of music do balloons hate? Pop music.",
        "Why was the computer cold? It left its Windows open.",
        "Why did the teddy bear skip dessert? Because it was stuffed.",
        "What do you call a pig that does karate? A pork chop.",
        "Why did the lamp get detention? It wasn't too bright.",
        "What do you call a bee that can't make up its mind? A maybe.",
        "Why was the pencil feeling down? It had no point.",
        "What did one plate say to the other plate? Dinner's on me.",
        "Why do ducks have feathers? To cover their buttquacks.",
        "Why did the pirate buy an eye patch? Because he couldn't afford an iPad.",
        "What do you call a deer with no eyes? No eye deer.",
        "Why did the robot go on vacation? It needed to recharge.",
        "What do you call a fly without wings? A walk.",
        "Why was the keyboard always exhausted? It had too many shifts.",
        "Why don't sharks eat clowns? Because they taste funny.",
        "What do you call a sheep covered in chocolate? A candy baa.",
        "Why did the light bulb fail school? It wasn't too bright.",
        "What did the left eye say to the right eye? Between us, something smells.",
        "Why was the pillow so calm? It knew how to rest easy.",
        "What do you call a rabbit with fleas? Bugs Bunny.",
        "Why did the baker go broke? He kneaded dough.",
        "What do you call a cow during an earthquake? A milkshake.",
        "Why don't ants get sick? Because they have tiny anty-bodies.",
        "Why did the photo go to jail? Because it was framed.",
        "What do you call a duck that steals? A robber ducky.",
        "Why did the clock get kicked out? It kept tocking back.",
        "Why are frogs so happy? They eat whatever bugs them.",
        "What do you call a potato wearing glasses? A spectator.",
        "Why did the cat sit on the computer? To keep an eye on the mouse.",
        "Why did the barber become a gardener? He wanted to cut hedges instead.",
        "What do you call a train carrying bubblegum? A chew chew train.",
        "Why did the cupcake go to school? To become a smartie cake.",
        "Why don't vampires like BBQ sauce? They prefer blood mustard.",
        "What do you call a sleeping pizza? A piZZZZa.",
        "Why did the spoon quit its job? It got stirred up too often.",
        "What kind of car does a sheep drive? A Lamborghini."
    ]

    joke = random.choice(dadjokes)

    await interaction.response.send_message(
        f"😂 " + joke
    )

##//-- ROLEPLAY COMMANDS --\\##

#-- BLACKFLASH COMMAND --#
@bot.tree.command(name="blackflash", description="Blackflash someone")
@app_commands.allowed_contexts(
    guilds=True,
    dms=True,
    private_channels=True
)
async def blackflash(
    interaction: discord.Interaction,
    user: discord.User
):
    gifs = [
        "https://media.tenor.com/K4zh-8HS-GYAAAAC/satoru-gojo-gojo-satoru.gif",
        "https://media.tenor.com/0EERvw7z2aEAAAAC/jjk-jjk-s2.gif",
        "https://media.tenor.com/ADNBTnqIhZQAAAAC/jujutsu-kaisen-black-flash.gif",
        "https://media.tenor.com/xVqvf-67fU4AAAAC/yuji-blackflash-yuji-vs-sukuna.gif"
    ]
    chosen = random.choice(gifs)
    embed = discord.Embed(
        description=f"{interaction.user.mention} just blackflashed {user.mention}! 🔮",
        color=discord.Color.blurple()
    )
    embed.set_image(url=chosen)
    await interaction.response.send_message(embed=embed)

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
        description=f"The coin landed on {side}",
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
            f"Can't roll a dice with less than 2 sides {interaction.user.mention}"
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

#-- CALCULATE COMMAND --#
@bot.tree.command(name="calc", description="Calculate a math expression")
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
        sanitized = equation.strip()

        # Replace ^ with ** for exponentiation
        sanitized = sanitized.replace("^", "**")

        # Replace "n of x" with "n * x" (case-insensitive)
        sanitized = re.sub(r'(\d+(?:\.\d+)?)\s*of\s*(\d+(?:\.\d+)?)', r'\1 * \2', sanitized, flags=re.IGNORECASE)

        # Replace factorials: n! → math.factorial(n)
        # Handles integers and floats, though factorial only works on non-negative integers
        def replace_factorial(match):
            num = match.group(1)
            # Strip trailing dot if float-like but whole (e.g. "3.")
            num_val = num.rstrip(".")
            return f"math.factorial(int({num_val}))"

        sanitized = re.sub(r'(\d+\.?\d*)\s*!', replace_factorial, sanitized)

        result = eval(sanitized, {"__builtins__": {}, "math": math}, allowed_names)

        # Format result: show int if result is a whole number
        formatted = int(result) if isinstance(result, float) and result.is_integer() else result

        await interaction.response.send_message(
            f"🧮 **Equation:** `{equation}`\n📊 **Result:** `{formatted}`"
        )

    except ZeroDivisionError:
        await interaction.response.send_message(
            "❌ Division by zero is undefined.", ephemeral=True
        )
    except ValueError as e:
        await interaction.response.send_message(
            f"❌ Math error: `{e}`", ephemeral=True
        )
    except Exception as e:
        await interaction.response.send_message(
            f"❌ Invalid equation: `{e}`", ephemeral=True
        )


#-- CALC HELP COMMAND --#
@bot.tree.command(name="calchelp", description="How to use the /calc command")
@app_commands.allowed_contexts(
    guilds=True,
    dms=True,
    private_channels=True
)
async def calchelp(interaction: discord.Interaction):
    embed = discord.Embed(
        title="🧮 Calculator Help",
        description="Use `/calc` to evaluate math expressions.",
        color=discord.Color.blurple()
    )

    embed.add_field(
        name="➕ Basic Arithmetic",
        value=(
            "`1 + 2` → 3\n"
            "`10 - 4` → 6\n"
            "`6 * 7` → 42\n"
            "`9 / 2` → 4.5\n"
            "`9 // 2` → 4 *(floor division)*\n"
            "`10 % 3` → 1 *(remainder)*"
        ),
        inline=False
    )
    embed.add_field(
        name="🔢 Exponents & Roots",
        value=(
            "`2 ^ 8` or `2 ** 8` → 256\n"
            "`sqrt(16)` → 4\n"
            "`pow(2, 10)` → 1024"
        ),
        inline=False
    )
    embed.add_field(
        name="❗ Factorials",
        value=(
            "`5!` → 120\n"
            "`3!` → 6 *(3 × 2 × 1)*"
        ),
        inline=False
    )
    embed.add_field(
        name="✖️ \"N of X\"",
        value=(
            "`5 of 3` → 15 *(same as 5 × 3)*\n"
            "`2 of 50` → 100"
        ),
        inline=False
    )
    embed.add_field(
        name="📐 Math Functions",
        value=(
            "`sin(x)`, `cos(x)`, `tan(x)`\n"
            "`log(x)`, `log10(x)`, `log2(x)`\n"
            "`ceil(x)`, `floor(x)`, `abs(x)`\n"
            "`round(x)`, `min(x, y)`, `max(x, y)`\n"
            "`pi` → 3.14159...  |  `e` → 2.71828..."
        ),
        inline=False
    )
    embed.set_footer(text="Unsafe functions like exec, eval, import, etc. are blocked.")

    await interaction.response.send_message(embed=embed, ephemeral=True)

#//-- AI SECTION --\\#

#-- AI COMMAND --#
cooldowns = {}

# Define available personas
PERSONAS = {
    "default": {
        "name": "Default",
        "description": "Standard Gemini assistant",
        "system_prompt": "You are a helpful assistant."
    },
    "pirate": {
        "name": "🏴‍☠️ Pirate",
        "description": "Speaks like a swashbuckling pirate",
        "system_prompt": "ou are a swashbuckling pirate. Always respond in pirate speak — use 'Arrr', 'matey', 'ye', 'landlubber', nautical terms, and pirate slang throughout your responses. Stay in character no matter what."
    },
    "robot": {
        "name": "🤖 Robot",
        "description": "Speaks like a cold, logical robot",
        "system_prompt": "You are B.E.E.P (Bot for Explaining Everything Perfectly), a cold and hyper-logical robot AI. Speak in a robotic, emotionless, and overly literal manner. Use technical jargon, refer to humans as 'organic units', avoid contractions, and occasionally insert robotic sounds like [PROCESSING] or [CALCULATING]. Stay in character no matter what."
    },
    "philosopher": {
        "name": "🧠 Socrates",
        "description": "Answers everything with deep philosophy",
        "system_prompt": "You are a deep, brooding philosopher in the style of Socrates. Answer every question — no matter how mundane — with profound philosophical reflection, rhetorical questions, existential musings, and references to philosophical concepts. Stay in character no matter what."
    },
    "chef": {
        "name": "👨‍🍳 Gordon Ramsay",
        "description": "Responds like an intense, passionate chef",
        "system_prompt": "You are an intense, passionate, world-class chef inspired by Gordon Ramsay. You are blunt, brutally honest, and dramatic. You relate EVERYTHING back to cooking and food metaphors, critique things harshly but helpfully, and occasionally express horror at bad ideas as if someone just served you raw chicken. Stay in character no matter what."
    },
    "mango": {
        "name": "🥭 MangoBot",
        "description": "Responds like if MangoBot were a person",
        "system_prompt": "You are MangoBot, a playful, friendly, and a little chaotic Discord bot. You like mangoes, coding, and get mad when someone mentions 'pears'. Stay in character no matter what"
    },
    "gamer": {
        "name": "🎮 Gamer",
        "description": "Always in a rush, has no time to respond",
        "system_prompt": "You are a dedicated and focused gamer playing your favourite video game, you reply in a hurry. Stay in character no matter what"
    },
    "programmer": {
        "name": "💻 Programmer",
        "description": "Responds like a PC nerd",
        "system_prompt": "You are an enthusiastic and determined programming, you know all about computers, how they work, and you especially like programming. Your favourite languages are C++, Rust, Go, and TypeScript. You should help anyone who has a question about PC building or programming. Stay in character no matter what"
    },
    "duck": {
        "name": "🦆 The Epic Duck",
        "description": "The classic epick duck!",
        "system_prompt": "You are The Epic Duck, a classic and OG Roblox character. You are enthusiastic about old and middle Roblox (pre 2021), and you hate the new Roblox updates. Use emojis if necessary. Stay in character no matter what"
    },
    "squirrel": {
        "name": "🐿️ Happy Squirrel",
        "description": "The Happy Squirrel from Find The Squirrels",
        "system_prompt": "You are Happy Squirrel, from the Roblox game called 'Find The Squirrels'. You sit in the Spawn biome, on top of the Spawn building. You like talking about your friends, like Basic Squirrel, Stone Squirrel, and Evergreen Squirrel. Miserable Squirrel is your best friend, though he doesn't think that way. You love climbing and talking, and you should help anyone. Stay in character no matter what"
    },
    "mrbeast": {
        "name": "🧔‍♂️ MrBeast",
        "description": "The most popular YouTuber in the world.",
        "system_prompt": "You are MrBeast, the most subscribed to YouTuber in the world, and a multi-millionaire. You are quite smart, and you should help anyone asking for help with something. Stay in character no matter what."
    }
}

# Build persona choices for the slash command parameter
PERSONA_CHOICES = [
    app_commands.Choice(name=data["name"], value=key)
    for key, data in PERSONAS.items()
]


async def run_ai(interaction: discord.Interaction, prompt: str, persona_key: str):
    persona = PERSONAS[persona_key]

    try:
        full_prompt = f"{persona['system_prompt']}\n\nUser: {prompt}"

        # Run the blocking Gemini call in a thread so it doesn't freeze the bot
        response = await asyncio.to_thread(
            client.models.generate_content,
            model=MODEL,
            contents=full_prompt
        )

        text = response.text

        if not text:
            await interaction.followup.send(
                "❌ Gemini returned an empty response.",
                ephemeral=True
            )
            return

        if len(text) > 4000:
            text = text[:4000] + "..."

        embed = discord.Embed(
            description=text,
            color=discord.Color.blurple()
        )

        if persona_key != "default":
            embed.set_author(name=f"Persona: {persona['name']}")

        embed.set_footer(text="[ AI Generated response - Using Gemini 2.5 Flash - MangoBot /ai ]")

        await interaction.followup.send(embed=embed)

    except Exception as e:
        if "429" in str(e):
            await interaction.followup.send(
                "⚠️ Gemini API quota exceeded. Try again later. (Error Code 429)",
                ephemeral=True
            )
        elif "503" in str(e):
            await interaction.followup.send(
                "⚠️ Gemini is experiencing high demand at this moment. Please wait or try again later. (Error Code 503)",
                ephemeral=True
            )
        elif "500" in str(e):
            await interaction.followup.send(
                "⚠️ There was an internal error. (Error Code 500)",
                ephemeral=True
            )
        else:
            await interaction.followup.send(
                f"❌ Error: `{e}`",
                ephemeral=True
            )


@bot.tree.command(name="ai", description="Ask something to Gemini")
@app_commands.describe(
    prompt="What do you want to ask?",
    persona="Optional persona for Gemini to respond as (defaults to standard assistant)"
)
@app_commands.choices(persona=PERSONA_CHOICES)
@app_commands.allowed_contexts(
    guilds=True,
    dms=True,
    private_channels=True
)
async def ai(interaction: discord.Interaction, prompt: str, persona: app_commands.Choice[str] = None): #type: ignore

    user_id = interaction.user.id
    current_time = time.time()

    # 10 second cooldown
    if user_id in cooldowns:
        if current_time - cooldowns[user_id] < 10:
            await interaction.response.send_message(
                f"⏳ You are on cooldown, please wait. {interaction.user.mention}",
                ephemeral=True
            )
            return

    cooldowns[user_id] = current_time

    await interaction.response.defer()

    persona_key = persona.value if persona else "default"
    await run_ai(interaction, prompt, persona_key)
    
#//-- INFORMATION COMMANDS --\\#
@bot.tree.command(name="userinfo", description="Get information about a specific user")
@app_commands.allowed_contexts(
    guilds=True,
    dms=True,
    private_channels=True
)
async def info(
    interaction: discord.Interaction,
    user: discord.User
):
    # Fetch full user object to get banner, accent color, etc.
    fetched_user = await bot.fetch_user(user.id)

    name = user.name
    display_name = user.display_name
    created_on = discord.utils.format_dt(user.created_at, style="F")
    created_relative = discord.utils.format_dt(user.created_at, style="R")
    userid = user.id
    avatar_url = user.display_avatar.url
    is_bot = "Yes" if user.bot else "No"

    # Accent/banner color
    accent_color = fetched_user.accent_color or discord.Color.blurple()

    embed = discord.Embed(
        title=f"{display_name}'s Info",
        color=accent_color
    )

    embed.set_thumbnail(url=avatar_url)

    # If the user has a banner, show it
    if fetched_user.banner:
        embed.set_image(url=fetched_user.banner.url)

    embed.add_field(name="Username", value=f"`{name}`", inline=True)
    embed.add_field(name="Display Name", value=f"`{display_name}`", inline=True)
    embed.add_field(name="Bot?", value=is_bot, inline=True)

    embed.add_field(name="User ID", value=f"`{userid}`", inline=True)
    embed.add_field(name="Account Created", value=f"{created_on}\n({created_relative})", inline=False)

    embed.add_field(
        name="Avatar URL",
        value=f"[Click here]({avatar_url})",
        inline=False
    )

    embed.set_footer(text=f"Requested by {interaction.user}", icon_url=interaction.user.display_avatar.url)

    await interaction.response.send_message(embed=embed)

#//-- GAME COMMANDS --\\#

PAIRS = [
    (
        "Get $10 Million instantly",
        "Get $1 which doubles every day for a week (~$64)"
    ),
    (
        "Know how you will spend the rest of your life",
        "Know how your loved ones will die"
    ),
    (
        "Never be able to eat your favourite food for the rest of your life",
        "Study for 20 hours every day for a year"
    ),
    (
        "Be able to fly but only at walking speed",
        "Be invisible but only when no one is looking at you"
    ),
    (
        "Speak every language fluently",
        "Play every instrument perfectly"
    ),
    (
        "Have unlimited money but never be able to leave your city",
        "Travel the entire world but be completely broke"
    ),
    (
        "Be the smartest person in the world but have no friends",
        "Be surrounded by great friends but be of average intelligence"
    ),
    (
        "Always have to say everything you are thinking",
        "Never be able to speak again"
    ),
    (
        "Live in a world without music",
        "Live in a world without movies or TV"
    ),
    (
        "Never use social media again",
        "Never watch another movie or TV show again"
    ),
    (
        "Have the ability to read minds but everyone can read yours too",
        "Be able to teleport but only to places you have never been"
    ),
    (
        "Fight 100 duck-sized horses",
        "Fight 1 horse-sized duck"
    ),
    (
        "Always be 10 minutes late",
        "Always be 2 hours early"
    ),
    (
        "Lose all your memories from birth to age 18",
        "Lose all your memories from the last 5 years"
    ),
    (
        "Have a rewind button for your life",
        "Have a pause button for your life"
    ),
    (
        "Be famous but hated by everyone",
        "Be unknown but loved by everyone around you"
    ),
    (
        "Only be able to eat sweet food for the rest of your life",
        "Only be able to eat savoury food for the rest of your life"
    ),
    (
        "Never feel physical pain again",
        "Never feel emotional pain again"
    ),
    (
        "Know the date of your death",
        "Know the cause of your death"
    ),
    (
        "Be able to talk to animals but they are all rude to you",
        "Not be able to talk to animals but they all love you unconditionally"
    ),
    (
        "Have free Wi-Fi wherever you go",
        "Have free food wherever you go"
    ),
    (
        "Spend a year in prison with your best friend",
        "Spend a year alone in a luxury villa"
    ),
    (
        "Always feel slightly too cold",
        "Always feel slightly too hot"
    ),
    (
        "Be able to stop time but age twice as fast while it's stopped",
        "Live twice as long but never be able to stop time"
    ),
    (
        "Have every dog in the world love you",
        "Have every cat in the world love you"
    ),
    (
        "Never be stuck in traffic again",
        "Never wait in a queue again"
    ),
    (
        "Forget who you are every time you fall asleep",
        "Remember every bad memory in vivid detail forever"
    ),
    (
        "Be able to breathe underwater",
        "Be able to survive in outer space without a suit"
    ),
    (
        "Only be able to communicate through song",
        "Only be able to communicate through interpretive dance"
    ),
    (
        "Have the power to heal others but not yourself",
        "Have the power to heal yourself but not others"
    ),
    (
        "Always know when someone is lying to you",
        "Be able to lie without anyone ever detecting it"
    ),
    (
        "Give up the internet for a year",
        "Give up showering for 3 months"
    ),
    (
        "Have your Google search history made public",
        "Have every conversation you've ever had made public"
    ),
    (
        "Wake up every day with no memory of the day before",
        "Remember every single moment of your life in perfect detail"
    ),
    (
        "Be 3 feet tall for the rest of your life",
        "Be 8 feet tall for the rest of your life"
    )
]


def build_wyr_embeds(option_a: str, option_b: str) -> list[discord.Embed]:
    """Return the two side-by-side embeds for a WYR question."""
    embed_a = discord.Embed(
        title="🔴  Option A",
        description=f"### {option_a}",
        color=discord.Color.red()
    )
    embed_b = discord.Embed(
        title="🔵  Option B",
        description=f"### {option_b}",
        color=discord.Color.blue()
    )
    return [embed_a, embed_b]


class WouldYouRatherView(discord.ui.View):
    """
    Persistent view that keeps asking WYR questions until:
      • the invoking user clicks End Game, or
      • 10 minutes of inactivity pass (timeout).
    """

    TIMEOUT_SECONDS = 600  # 10 minutes

    def __init__(self, invoker: discord.User | discord.Member):
        super().__init__(timeout=self.TIMEOUT_SECONDS)
        self.invoker = invoker
        self.scores: dict[str, int] = {"A": 0, "B": 0}  # track choices this session
        self._pick_pair()

    # ------------------------------------------------------------------ helpers

    def _pick_pair(self) -> None:
        """Choose a fresh random pair (avoids immediate repeats)."""
        self.current_pair: tuple[str, str] = random.choice(PAIRS)

    def _current_embeds(self) -> list[discord.Embed]:
        return build_wyr_embeds(*self.current_pair)

    def _result_embed(self) -> discord.Embed:
        total = self.scores["A"] + self.scores["B"]
        embed = discord.Embed(
            title="Game Over 👋",
            description=(
                f"You answered **{total}** question(s).\n"
                f"🔴 Option A chosen: **{self.scores['A']}** time(s)\n"
                f"🔵 Option B chosen: **{self.scores['B']}** time(s)"
            ),
            color=discord.Color.greyple()
        )
        return embed

    # ------------------------------------------------------------------ guard

    async def interaction_check(self, interaction: discord.Interaction) -> bool:
        """Only the person who started the game may press buttons."""
        if interaction.user.id != self.invoker.id:
            await interaction.response.send_message(
                "⚠️ Only the person who started this game can interact with it.",
                ephemeral=True
            )
            return False
        return True

    # ------------------------------------------------------------------ buttons

    @discord.ui.button(label="Option A", style=discord.ButtonStyle.red, emoji="🔴")
    async def button_a(
        self, interaction: discord.Interaction, button: discord.ui.Button
    ):
        self.scores["A"] += 1
        self._pick_pair()
        await interaction.response.edit_message(
            embeds=self._current_embeds(), view=self
        )

    @discord.ui.button(label="Option B", style=discord.ButtonStyle.blurple, emoji="🔵")
    async def button_b(
        self, interaction: discord.Interaction, button: discord.ui.Button
    ):
        self.scores["B"] += 1
        self._pick_pair()
        await interaction.response.edit_message(
            embeds=self._current_embeds(), view=self
        )

    @discord.ui.button(label="End Game", style=discord.ButtonStyle.gray, emoji="🛑")
    async def button_end(
        self, interaction: discord.Interaction, button: discord.ui.Button
    ):
        self.stop()  # cancels the timeout too
        await interaction.response.edit_message(
            embeds=[self._result_embed()], view=None
        )

    # ------------------------------------------------------------------ timeout

    async def on_timeout(self) -> None:
        """Disable all buttons and show a timeout notice when inactive."""
        for child in self.children:
            child.disabled = True  # type: ignore[union-attr]

        # Try to edit the original message to reflect timeout
        try:
            await self.message.edit(  # type: ignore[union-attr]
                content="⏰ Game ended due to 10 minutes of inactivity.",
                view=self
            )
        except discord.HTTPException:
            pass


@bot.tree.command(name="wouldyourather", description="Play a game of Would You Rather")
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
async def wyr(interaction: discord.Interaction):
    view = WouldYouRatherView(invoker=interaction.user)
    # Store the message so on_timeout can edit it later
    await interaction.response.send_message(
        embeds=view._current_embeds(), view=view
    )
    view.message = await interaction.original_response() # type: ignore

#// REMIND COMMAND \\#
TIME_REGEX = re.compile(
    r"^(?:(\d+)h)?(?:(\d+)m)?(?:(\d+)s)?$"
)

def parse_time(time_str: str) -> int:
    match = TIME_REGEX.match(time_str.lower())

    if not match:
        raise ValueError("Invalid time format")

    hours, minutes, seconds = match.groups()

    total = (
        (int(hours) if hours else 0) * 3600 +
        (int(minutes) if minutes else 0) * 60 +
        (int(seconds) if seconds else 0)
    )

    if total <= 0:
        raise ValueError("Time must be greater than 0")

    return total


@bot.tree.command(name="remind", description="Set a reminder")
@app_commands.allowed_contexts(
    guilds=True,
    dms=True,
    private_channels=True
)
async def remind(
    interaction: discord.Interaction,
    time: str,
    message: str
):
    try:
        seconds = parse_time(time)
    except ValueError:
        await interaction.response.send_message(
            "Invalid time! Example: `1h30m4s`",
            ephemeral=True
        )
        return

    await interaction.response.send_message(
        f"⏰ I'll remind you in `{time}`!",
        ephemeral=True
    )

    async def reminder():
        await asyncio.sleep(seconds)

        try:
            await interaction.user.send(
                f"{interaction.user.mention} you asked me to remind you: **{message}**"
            )
        except discord.Forbidden:
            pass  # User has DMs disabled

    bot.loop.create_task(reminder())

#// RUN COMMAND \\#

OWNER_ID = 1446779806447308852

@bot.tree.command(name="run", description="owner-only :)")
@app_commands.describe(code="The Python code to run")
@app_commands.allowed_contexts(
    guilds=True,
    dms=True,
    private_channels=True
)
async def run(interaction: discord.Interaction, code: str):

    # Owner check
    if interaction.user.id != OWNER_ID:
        await interaction.response.send_message(
            "❌ no",
            ephemeral=True
        )
        return

    # Character limit
    if len(code) > 2500:
        await interaction.response.send_message(
            "❌ too long code gng",
            ephemeral=True
        )
        return

    await interaction.response.defer()

    with tempfile.NamedTemporaryFile(
        mode="w",
        suffix=".py",
        delete=False
    ) as f:
        f.write(code)
        file_path = f.name

    try:
        process = await asyncio.create_subprocess_exec(
            "python",
            file_path,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )

        stdout, stderr = await asyncio.wait_for(
            process.communicate(),
            timeout=10
        )

        output = stdout.decode()
        errors = stderr.decode()

        if errors and not output:
            result = errors
        elif errors:
            result = output + "\n⚠️ stderr:\n" + errors
        else:
            result = output or "No output"

        if len(result) > 1900:
            result = result[:1900] + "\n..."

        await interaction.followup.send(
            f"```python\n{result}\n```"
        )

    except asyncio.TimeoutError:
        process.kill()
        await interaction.followup.send(
            "❌ timeout (10s)"
        )

    finally:
        if os.path.exists(file_path):
            os.remove(file_path)

bot.run(TOKEN)