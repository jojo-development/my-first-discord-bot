import discord
from discord.ext import commands
import os

# ── Bot Configuration ──────────────────────────────────────────────
TOKEN = os.getenv("DISCORD_TOKEN")   # Store your token as an env variable (never hardcode it)

intents = discord.Intents.default()
intents.message_content = True       # Required to read message content

bot = commands.Bot(command_prefix="!", intents=intents)

# ── Events ─────────────────────────────────────────────────────────
@bot.event
async def on_ready():
    print(f"⚓  Logged in as {bot.user} (ID: {bot.user.id})")
    print(f"⚓  Connected to {len(bot.guilds)} server(s)")
    await bot.change_presence(
        activity=discord.Game(name="Sailin' the Seven Seas 🏴‍☠️")
    )

@bot.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.text_channels, name="general")
    if channel:
        await channel.send(
            f"Ahoy, {member.mention}! Welcome aboard Somesh's Server, ye scallywag! 🏴‍☠️"
        )

# ── Commands ────────────────────────────────────────────────────────
@bot.command(name="ahoy")
async def ahoy(ctx):
    """Pirate greeting"""
    await ctx.send(f"Ahoy, {ctx.author.mention}! What brings ye to these waters? ⚓")

@bot.command(name="treasure")
async def treasure(ctx):
    """Get a pirate tip"""
    await ctx.send("🗺️  X marks the spot! The real treasure was the code we wrote along the way.")

@bot.command(name="ship")
async def ship(ctx):
    """Show server info"""
    guild = ctx.guild
    await ctx.send(
        f"🚢 **Ship Name:** {guild.name}\n"
        f"👥 **Crew Size:** {guild.member_count} sailors\n"
        f"⚓ **Captain:** {guild.owner}"
    )

# ── Run the bot ─────────────────────────────────────────────────────
if __name__ == "__main__":
    if not TOKEN:
        raise ValueError("No DISCORD_TOKEN found. Set it as an environment variable.")
    bot.run(TOKEN)
