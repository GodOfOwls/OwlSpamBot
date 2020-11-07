# This is a sample Python script.
import asyncio
from kantex.md import *
from telethon import TelegramClient, events
from telethon.events import NewMessage
from secret import *

import spamwatch
from telethon.tl import functions, types
from telethon.tl.custom import Message

client = spamwatch.Client(ebg_token,
                          host='https://kantek.eule.computer')
swclient = spamwatch.Client(sw_token)




async def main():
    bot = TelegramClient(NAME, API_ID, API_HASH)

    await bot.start(bot_token=TOKEN)

    @bot.on(events.NewMessage(pattern='/start', forwards=False))
    async def start(event):
        await event.respond(f'Helluwu, \n'
                            f'you can check if an id is banned in @SpamWatch or @OwlAntispam by doing:\n'
                            f'/spamwatch [id] to check in SpamWatch\n'
                            f'/ebg [id] to check in OwlAntispam')

    @bot.on(events.NewMessage(pattern='/ebg', forwards=False))
    async def check(event):
        msg: Message = event.message
        text: str = msg.raw_text
        id = text.split(' ')[1]
        ban = client.get_ban(id)
        if not ban:
            await event.respond(f' The ID {id} is not banned in the EBG Network')
            return

        message = f'The User with the ID {Code(id)} is banned!\n' \
                  f'' \
                  f'Time of the Ban: {Code(ban.date)}\n' \
                  f'Reason for the Ban: {Code(ban.reason)}\n' \
                  f'Offending Message (if on record):\n {Code(ban.message) if ban.message else Code("Fehlt")}\n' \
                  f'\n\n\nPowered by @GodOfOwls'

        await event.respond(message)

    @bot.on(events.NewMessage(pattern='/spamwatch', forwards=False))
    async def check(event):
        msg: Message = event.message
        text: str = msg.raw_text
        id = text.split(' ')[1]
        ban = swclient.get_ban(id)
        if not ban:
            await event.respond(f' The ID {id} is not banned in SpamWatch')
            return

        message = f'The User with the ID {Code(id)} is banned!\n' \
                  f'' \
                  f'Time of the Ban: {Code(ban.date)}\n' \
                  f'Reason for the Ban: {Code(ban.reason)}\n' \
                  f'Offending Message (if on record):\n {Code(ban.message) if ban.message else Code("Fehlt")}\n' \
                  f'\n\n\nPowered by @GodOfOwls\n using the official @Spamwatch API'
        await event.respond(message)

    @bot.on(events.NewMessage(pattern='/eule1234567891011', forwards=False))
    async def restart(event):

        await event.respond(f'k')
        await bot.disconnect()




    await bot.run_until_disconnected()


if __name__ == '__main__':
    asyncio.run(main())
