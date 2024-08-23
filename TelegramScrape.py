import pandas as pd
import datetime
from telethon import TelegramClient


# Define an async function
async def fetch_telegram_data(api_id, api_hash, chats):
    # Initialize the Telegram client
    async with TelegramClient('test', api_id, api_hash) as client:

        # Fetch all dialogs to ensure the client is properly connected
        await client.get_dialogs()

        # List to store data
        data = []

        # Fetch messages for each chat
        for chat in chats:
            # Get the entity of the chat (whether it's an ID or a username)
            entity = await client.get_entity(chat)

            # Iterate through messages in the chat
            async for message in client.iter_messages(entity, offset_date=datetime.datetime.today(), reverse=False):
                data.append({
                    "group": entity.title if hasattr(entity, 'title') else chat,
                    "sender": message.sender_id,
                    "text": message.text,
                    "date": message.date
                })

        # Create DataFrame
        df = pd.DataFrame(data)
        df['date'] = df['date'].dt.tz_localize(None)
        # Export to Excel
        df.to_excel(f"C:\\ResellerEngine\\data_{datetime.datetime.today().date()}.xlsx", index=False)


# Example usage (assuming you have your API credentials and chat list)
api_id = ***
api_hash = '***'
chats = [****] #ID can be gotten by opening telegram web...the ID in on the URL

# To run the async function
import asyncio

asyncio.run(fetch_telegram_data(api_id, api_hash, chats))
