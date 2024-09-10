from pypresence import Presence
import time

# Replace with your actual Discord application's client ID
client_id = '1'

# Initialize the presence object
RPC = Presence(client_id)
RPC.connect()

def update_presence():
    # Update presence with custom details
    RPC.update(
        state="The unseen hand",
        details="Behind every move",
        large_image="big_image",  # Use a key for the image; this should match the key you set in Discord Developer Portal
        large_image_text="The Long Game",
        start=time.time(),  # Using current time for the timestamp
        activity_type=0,  # 0 for playing
    )

while True:
    update_presence()
    time.sleep(15)  # Update every 15 seconds