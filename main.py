import discord
from discord.ext import commands
from discord import app_commands

from google import genai

import random
import math
import re

from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv("TOKEN") or ""
KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=KEY)
MODEL = "gemini-2.0-flash"

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
        f"{member.mention} go look in the mirror 🪞",
        f"i am running out of ways to roast you, {member.mention} 🔥"
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
        # e.g. "5 of 3", "5of3", "5 of3" → "5 * 3"
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

#-- ASKAI COMMAND --#
@bot.tree.command(name="ai", description="Ask something to Gemini 2.0 Flash")
@app_commands.allowed_contexts(
    guilds=True,
    dms=True,
    private_channels=True
)
async def ai(
    interaction: discord.Interaction,
    prompt: str
):

    await interaction.response.defer()  # prevents timeout

    try:
        response = client.models.generate_content(
            model=MODEL,
            contents=prompt
        )

        text = response.text

        if not text:
            await interaction.followup.send(
                "❌ Gemini returned an empty response.",
                ephemeral=True
            )
            return

        # Discord embed description limit = 4096 chars
        if len(text) > 4000:
            text = text[:4000] + "..."

        embed = discord.Embed(
            title="🤖 Gemini AI",
            description=text,
            color=discord.Color.blurple()
        )

        embed.set_footer(text="Gemini 2.0 Flash")

        await interaction.followup.send(embed=embed)

    except Exception as e:
        await interaction.followup.send(
            f"❌ Error: `{e}`",
            ephemeral=True
        )
    

bot.run(TOKEN)