#!/usr/bin/env python3

import asyncio
import logging

from .. import loader, utils
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.types import MessageMediaDocument

import urllib3

logger = logging.getLogger(__name__)


@loader.tds
class RollMod(loader.Module):
    """Roll"""  # Translateable due to @loader.tds
    strings = {"name": "ROLL",
               "author": "https://t.me/smolovk_ftg"}

    async def client_ready(self, client, db):
        self.client = client

    def __init__(self):
        self.name = self.strings['name']


    @loader.unrestricted  # Security setting to change who can use the command (defaults to owner | sudo)
    async def rollcmd(self, message):
        logger.debug('roll!')
        chat = '@roll_smolovk_bot'
        await message.edit('<i>Rolling...</i>')

        async with message.client.conversation(chat) as conv:
            try:
                response = conv.wait_event(events.NewMessage(incoming=True, from_users=2018963821))
                mm = await message.client.send_message(chat, "/roll")
                response = await response
                await mm.delete()
            except YouBlockedUserError:
                await message.reply('<b>ass</b>')
                return

        await message.delete()
        await response.delete()

        await message.client.send_message(message.to_id, response.text)
