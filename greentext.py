import asyncio
import logging

from .. import loader, utils
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.types import MessageMediaDocument

import urllib3

logger = logging.getLogger(__name__)


@loader.tds
class GreenTextMod(loader.Module):
    """Greentext"""  # Translateable due to @loader.tds
    strings = {"name": "Green Text",
               "author": "https://t.me/smolovk_ftg"}

    async def client_ready(self, client, db):
        self.client = client

    def __init__(self):
        self.name = self.strings['name']

    # Security setting to change who can use the command (defaults to owner | sudo)
    @loader.unrestricted
    async def gtcmd(self, message):
        """Returns PEPE greentext"""
        args = utils.get_args_raw(message)
        reply = await message.get_reply_message()
        if not reply:
            await message.edit("<b>Reply to text</b>")
            return
        try:
            text = "/gt " + reply.text
        except:
            await message.edit("<b>Only text</b>")
            return

        chat = '@greentextBot'
        await message.edit('<b>Работаем...</b>')
        async with message.client.conversation(chat) as conv:
            try:
                response = conv.wait_event(events.NewMessage(
                    incoming=True, from_users=1648991466))
                mm = await message.client.send_message(chat, text)
                response = await response
                await mm.delete()
            except YouBlockedUserError:
                await message.reply('<b>ass</b>')
                return
            await message.delete()
            await response.delete()
            await message.client.send_file(message.to_id, response.media, reply_to=await message.get_reply_message())

    async def rwpcmd(self, message):
        """Returns Russian War Pig"""
        args = utils.get_args_raw(message)
        reply = await message.get_reply_message()
        if not reply:
            await message.edit("<b>Reply to text</b>")
            return
        try:
            text = "/rwp " + reply.text
        except:
            await message.edit("<b>Only text</b>")
            return

        chat = '@greentextBot'
        await message.edit('<b>Работаем...</b>')
        async with message.client.conversation(chat) as conv:
            try:
                response = conv.wait_event(events.NewMessage(
                    incoming=True, from_users=1648991466))
                mm = await message.client.send_message(chat, text)
                response = await response
                await mm.delete()
            except YouBlockedUserError:
                await message.reply('<b>ass</b>')
                return
            await message.delete()
            await response.delete()
            await message.client.send_file(message.to_id, response.media, reply_to=await message.get_reply_message())

    async def jewcmd(self, message):
        """Returns jew"""
        args = utils.get_args_raw(message)
        reply = await message.get_reply_message()
        if not reply:
            await message.edit("<b>Reply to text</b>")
            return
        try:
            text = "/jew " + reply.text
        except:
            await message.edit("<b>Only text</b>")
            return

        chat = '@greentextBot'
        await message.edit('<b>Работаем...</b>')
        async with message.client.conversation(chat) as conv:
            try:
                response = conv.wait_event(events.NewMessage(
                    incoming=True, from_users=1648991466))
                mm = await message.client.send_message(chat, text)
                response = await response
                await mm.delete()
            except YouBlockedUserError:
                await message.reply('<b>ass</b>')
                return
            await message.delete()
            await response.delete()
            await message.client.send_file(message.to_id, response.media, reply_to=await message.get_reply_message())

    async def rollcmd(self, message):
        """Roll"""
        chat = '@greentextBot'
        await message.edit('<i>Rolling...</i>')

        async with message.client.conversation(chat) as conv:
            try:
                response = conv.wait_event(events.NewMessage(
                    incoming=True, from_users=1648991466))
                mm = await message.client.send_message(chat, "/roll")
                response = await response
                await mm.delete()
            except YouBlockedUserError:
                await message.reply('<b>ass</b>')
                return

        await message.delete()
        await response.delete()

        await message.client.send_message(message.to_id, response.text)
