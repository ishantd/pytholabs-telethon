import asyncio
from telethon import TelegramClient
from telethon.tl import functions, types

api_id = 1662957
api_hash = '5552518e928df0ddddc291f1b7f680df'
client = TelegramClient('anon', api_id, api_hash)

async def main():
    await client.connect()
    channel = await client.get_entity('MyGovCoronaNewsdesk')
    messages = await client.get_messages(channel, limit=15)

    for x in messages:
        print(x.text)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())