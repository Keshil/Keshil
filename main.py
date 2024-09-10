import aiohttp
import asyncio
import json

TOKEN = 'YOUR_DISCORD_USER_TOKEN'  # Replace with your Discord user token

async def update_activity():
    url = "https://discord.com/api/v10/users/@me/activities"
    headers = {
        'Authorization': f'Bearer {TOKEN}',
        'Content-Type': 'application/json'
    }
    activity = {
        "activity": {
            "name": "Behind every move",
            "type": 0  # 0 for playing
        }
    }

    async with aiohttp.ClientSession() as session:
        while True:
            async with session.patch(url, headers=headers, data=json.dumps(activity)) as resp:
                if resp.status == 200:
                    print("Activity updated successfully")
                else:
                    print(f"Failed to update activity: {resp.status}")
            await asyncio.sleep(15)  # Update every 15 seconds

if __name__ == "__main__":
    asyncio.run(update_activity())