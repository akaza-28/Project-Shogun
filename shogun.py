import asyncio
import genshin

async def main():
    cookies = {"ltuid":ownkey, "ltoken":"owntokken"}
    client = genshin.Client()
    client.set_browser_cookies()
    
    skip_on_failure=True
    uid= int(input("Enter your UID : "))
    user = await client.get_full_genshin_user(uid)
        
    print("Username :  ",user.info.nickname)
    print("Characters : ",user.stats.characters)
    print("Days Active : ",user.stats.days_active)
    print("Acievements : ",user.stats.achievements)
    print("Anemoculus Collected",user.stats.anemoculi)
    print("Geoculus Collected",user.stats.geoculi)
    print("Electroculus Collected ",user.stats.electroculi)
    print("Dendroculus Collected",user.stats.dendroculi)

asyncio.run(main())

