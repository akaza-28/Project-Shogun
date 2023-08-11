import asyncio
import genshin

async def main():
    cookies = {"ltuid":ownkey, "ltoken":"owntokken"}
    client = genshin.Client()
    
    skip_on_failure=True
    uid = 
    data = await client.get_genshin_user(uid)
    print("You have a total of {data.stats.characters} characters")

asyncio.run(main())

