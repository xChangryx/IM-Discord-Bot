__version__ = "1.0.2"

from asyncio.tasks import create_task
import os
import StorageHandler as DB
import emoji
import re


# ----- TOKEN ----- #
from dotenv import load_dotenv
load_dotenv()
token = os.getenv('TOKEN')
# ----- TOKEN ----- #


# ----- DISCORD ----- #
import discord
from discord.embeds import Embed
intents = discord.Intents.default()
client = discord.Client(intents=intents)
# ----- DISCORD ----- #





class RoleReactionEmbed:
    def __init__(self, message) -> None:
        self.input = message
        self.output = None
        self.reactions = {} # emoji : role.id

        # Find all emojis and roles in the input message
        for line in self.input.content.splitlines():
            reaction = None
            for char in line:
                if char in emoji.UNICODE_EMOJI['en']:
                    reaction = char
                    break
            match = re.findall(r"<.+:(\d+)>", line)
            if match: reaction = match[0]
            role = re.findall(r"<@&(\d+)>", line)
            if reaction and role:
                self.reactions[reaction] = role[0]

    def save(self) -> None: 
        for emoji in self.reactions:
            if isinstance(emoji, str):
                DB.add_reaction(
                    self.output.guild.id,
                    self.output.channel.id,
                    self.output.id,
                    0, emoji, 0,
                    int(self.reactions[emoji])
                )
            else:
                DB.add_reaction(
                    self.output.guild.id,
                    self.output.channel.id,
                    self.output.id,
                    emoji.id, "", 1,
                    int(self.reactions[emoji])
                )

    def create_embed(self) -> Embed:
        embed_dict = {
            "title": "Roles",
            "color": 0x5865F2,
            "description": "\n".join(self.input.content.splitlines()[1:])
        }
        return Embed.from_dict(embed_dict)
    
    async def send(self) -> None:
        self.output = await self.input.channel.send(embed=self.create_embed())
        for emoji in self.reactions:
            print(emoji)
            if len(emoji) > 1: emoji = client.get_emoji(int(emoji))
            print(emoji)
            await self.output.add_reaction(emoji)
        self.save()






@client.event
async def on_ready():
    print("Online")


@client.event
async def on_raw_reaction_add(payload):
    if payload.user_id == client.user.id: return
    role_id = DB.get_role_from_reaction(payload)
    if not role_id: return
    
    guild = client.get_guild(payload.guild_id)
    member = guild.get_member(payload.user_id)
    member.add_roles([guild.get_role(role_id)])


@client.event
async def on_message(message):
    if message.author == client.user: return
    if str(message.channel.type) == "private": return
    if message.content.splitlines()[0].lower() != "!roles": return
    if not message.channel.permissions_for(message.author).administrator: return

    embed = RoleReactionEmbed(message)
    await embed.send()


@client.event
async def on_raw_message_delete(payload):
    DB.remove_reactions(payload)


client.run(token)