from typing import final 
import os 
from dotenv import load_dotenv
from discord import Intents , Client , Message 
from responses import get_response 

# step 00 : Load token from .env file
load_dotenv()
TOKEN: final = os.getenv('DISCORD_TOKEN')

# step1 : bot setup
intents = Intents.default()
intents.message_content = True
client = Client(intents=intents)

# step 2 : message handling
async def send_message(message:Message, user_message:str):
    if not user_message:
        print('Message is empty')
        return
    
    if is_private:=user_message[0]=='?':
        user_message = user_message[1:]
        # await message.author.send(get_responses(user_message))
        
    try:
        response = get_response(user_message)
        await message.channel.send(response) if not is_private else await message.author.send(response)
    except Exception as e:
        print(e)

# step 3 : run the bot
@client.event
async def on_ready():
    print(f'{client.user} is now running!')

#step4 : listen for messages
@client.event
async def on_message(message:Message):
    if message.author == client.user:
        return

    username = str(message.author)
    user_message = str(message.content)
    channel = str(message.channel)

    print(f"{username} said '{user_message}' ({channel})")
    await send_message(message, user_message)
    
    # step 5 : main entry point
def main():
    client.run(token=TOKEN)

if __name__ == '__main__':
    main()