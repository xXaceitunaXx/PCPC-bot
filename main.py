from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Attachment, Member
from discord.ext import commands
from problems import Problem_list

# Load token
load_dotenv()
TOKEN: Final[str] = os.getenv("DISCORD_TOKEN")
WELCOME_CHANNEL: Final[str] = os.getenv("WELCOME_CHANNEL")

# Bot setup
intents: Intents = Intents.default()
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix="/", intents=intents)
problems: Problem_list = Problem_list(["Test 1", "Test 2"])


@bot.hybrid_command()
async def ping(ctx: commands.Context):
    await ctx.send("pong")


@bot.hybrid_command()
async def hello(ctx: commands.Context):
    await ctx.send(f"Hello {ctx.author.nick}")


@bot.hybrid_command()
async def list_problems(ctx: commands.context):
    await ctx.send(str(problems))


@bot.hybrid_command()
async def request(
    ctx: commands.Context, user: str, password: str, problem: str, file: Attachment
):
    print(f"Recibed request from {user}")

    if not file.filename.endswith(".cpp"):
        await ctx.reply("Por favor selecciona un fichero c++", ephemeral=True)
        return

    if not (user and password):
        await ctx.reply("Por favor introduce unas credenciales validas", ephemeral=True)
        return

    print("Request processed correctly")

    await ctx.reply("Request procesada correctamente", ephemeral=True)

    channel = ctx.channel
    await channel.send(
        f"User {user} made a request with file {file.filename} to problem {problem}"
    )

    await channel.send(file)


@bot.hybrid_command()
async def sync(ctx: commands.Context):
    await bot.tree.sync()
    await ctx.send("Comandos sincronizados")


@bot.event
async def on_member_join(member: Member):
    print(f"Member {member.name} joined!")
    channel = bot.get_channel(channel=WELCOME_CHANNEL)
    if channel:
        await channel.send(f"Bienvenido {member.name}!")


@bot.event
async def on_ready():
    print(f"{bot.user} has connected to Discord!")
    await bot.tree.sync()


def main() -> None:
    bot.run(token=TOKEN)


if __name__ == "__main__":
    main()
