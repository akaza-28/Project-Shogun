import asyncio
import genshin
try:
    async def main():
        cookies = {"ltuid": 215584138, "ltoken": "xhPj1YJ1A751yIzTb4Tc63OWf0UZiykFac5pp5K0"}
        client = genshin.Client()
        client.set_cookies_auto()

        data = await client.get_genshin_user(857107919)
        print("You have a total of {data.stats.characters} characters")

    asyncio.run(main())
except ValidationError as e:
    print(e)