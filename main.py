import aiohttp
import asyncio
import json
import os

# Read the token from environment variables
TOKEN = os.getenv('DISCORD_TOKEN')

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