import sys
import random

import discord
import aiohttp

from const import API_KEY, DISCORD_KEY


sys.stdout.reconfigure(encoding='utf-8')

intents = discord.Intents.default()
intents.members = True
intents.messages = True
intents.message_content = True
intents.reactions = True


class MyClient(discord.Client):
    def __init__(self, **kwargs):
        """
        Initializes the Discord client, sets up reaction roles and the channel name for messages.

        :param kwargs: Arguments for the Discord client.
        """
        super().__init__(**kwargs)
        self.role_by_reaction = {
            "<:Iron_3_Rank:1194288576742051952>": ("iron", discord.Color.dark_gray()),
            "<:Bronze_3_Rank:1194288567871082556>": ("bronze", discord.Color.dark_orange()),
            "<:Silver_3_Rank:1194288581024424076>": ("silver", discord.Color.light_gray()),
            "<:Gold_3_Rank:1194288572329631744>": ("gold", discord.Color.gold()),
            "<:Platinum_3_Rank:1194288578356842506>": ("platinum", discord.Color.blue()),
            "<:Diamond_3_Rank:1194288569452347492>": ("diamond", discord.Color.purple()),
            "<:Ascendant_3_Rank:1194288565119631450>": ("ascendant", discord.Color.green()),
            "<:Immortal_3_Rank:1194288573940244540>": ("immortal", discord.Color.red())
        }
        self.chanel_name = 'test'

    async def send_reaction_message(self) -> None:
        """
        Sends a message in the channel with emojis for reactions to assign roles.
        Creates an embed message with emojis corresponding to roles.
        """
        guild = discord.utils.get(self.guilds)
        if not guild:
            return

        channel = discord.utils.get(guild.text_channels, name=self.chanel_name)
        if not channel:
            return

        description = "Реагируйте на эмодзи, чтобы получить роли:\n"
        for emoji, (role_name, _) in self.role_by_reaction.items():
            description += f"{emoji} — {role_name}\n"

        embed = discord.Embed(
            title="Роли по реакциям",
            description=description,
            color=discord.Color.blurple()
        )

        message = await channel.send(embed=embed)

        for emoji in self.role_by_reaction.keys():
            await message.add_reaction(emoji)

    async def on_raw_reaction_add(self, payload: discord.RawReactionActionEvent) -> None:
        """
        Handles the event when a reaction is added to a message.
        Grants the role to the user if the emoji matches a role.

        :param payload: The reaction event data.
        """
        guild = self.get_guild(payload.guild_id)
        if not guild:
            return

        member = guild.get_member(payload.user_id)
        if not member or member.bot:
            return

        emoji = str(payload.emoji)
        if emoji in self.role_by_reaction:
            role_name, role_color = self.role_by_reaction[emoji]

            role = discord.utils.get(guild.roles, name=role_name)
            if not role:
                role = await guild.create_role(
                    name=role_name,
                    color=role_color,
                    reason="Роль создана для реакции"
                )

            if role not in member.roles:
                await member.add_roles(role)

    async def on_raw_reaction_remove(self, payload: discord.RawReactionActionEvent) -> None:
        """
        Handles the event when a reaction is removed from a message.
        Removes the role from the user if it was assigned via a reaction.

        :param payload: The reaction event data.
        """
        guild = self.get_guild(payload.guild_id)
        if not guild:
            return

        member = guild.get_member(payload.user_id)
        if not member or member.bot:
            return

        emoji = str(payload.emoji)
        if emoji in self.role_by_reaction:
            role_name, _ = self.role_by_reaction[emoji]

            role = discord.utils.get(guild.roles, name=role_name)
            if role and role in member.roles:
                await member.remove_roles(role)

    async def on_ready(self) -> None:
        """
        Called when the bot successfully connects to the Discord server.
        Sends a message with reactions for role assignments.
        """
        await self.send_reaction_message()

    async def on_member_join(self, member: discord.Member) -> None:
        """
        Called when a new member joins the server.
        Sends a welcome message to the specified channel.

        :param member: The new member who joined the server.
        """
        channel = discord.utils.get(
            member.guild.text_channels, name=self.chanel_name)
        if channel:
            gif_url = await self.get_random_gif("hello")
            if gif_url:
                await channel.send(f"Добро пожаловать, {member.mention}!", embed=discord.Embed().set_image(url=gif_url))

    async def get_random_gif(self, query: str) -> str | None:
        """
        Fetches a random GIF from the Giphy API based on the query.

        :param query: The query for searching a GIF.
        :return: A URL to the GIF or None if no GIF is found.
        """
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(f"https://api.giphy.com/v1/gifs/search?q={query}&api_key={API_KEY}&limit=10") as response:
                    if response.status == 200:
                        data = await response.json()
                        gifs = [result["images"]["original"]["url"]
                                for result in data["data"]]
                        if gifs:
                            return random.choice(gifs)
                        else:
                            return None
                    else:
                        return None
        except Exception:
            return None


client = MyClient(intents=intents)
client.run(DISCORD_KEY)
