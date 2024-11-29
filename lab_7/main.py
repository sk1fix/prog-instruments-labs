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


class MyClient(discord.Client):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_member_join(self, member):
        channel = discord.utils.get(member.guild.text_channels, name='test')
        if channel:
            gif_url = await self.get_random_gif("hello")
            if gif_url:
                await channel.send(f"Добро пожаловать, {member.mention}!", embed=discord.Embed().set_image(url=gif_url))
            else:
                print("Не удалось получить гифку.")
        else:
            print("Канал не найден.")

    async def get_random_gif(self, query):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(f"https://api.giphy.com/v1/gifs/search?q={query}&api_key={API_KEY}&limit=10") as response:
                    if response.status == 200:
                        data = await response.json()
                        gifs = [result["images"]["original"]["url"] for result in data["data"]]
                        if gifs:
                            return random.choice(gifs)
                        else:
                            return None
                    else:
                        return None
        except Exception as e:
            return None


client = MyClient(intents=intents)
client.run(DISCORD_KEY)
