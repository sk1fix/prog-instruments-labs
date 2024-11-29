import aiohttp
import random
import asyncio

API_KEY = '5C8ctDZbxR8tbwEpd0r2A9EeN5Fw6mCE'

async def get_random_gif(query):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://api.giphy.com/v1/gifs/search?q={query}&api_key={API_KEY}&limit=10") as response:
                if response.status == 200:
                    data = await response.json()
                    gifs = [result["images"]["original"]["url"] for result in data["data"]]
                    if gifs:
                        return random.choice(gifs)
                    else:
                        print("Нет гифок по запросу.")
                        return None
                else:
                    print(f"Ошибка Giphy: {response.status}")
                    return None
    except Exception as e:
        print(f"Ошибка при запросе Giphy: {e}")
        return None


gif_url = asyncio.run(get_random_gif("hello"))
print(gif_url)