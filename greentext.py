import asyncio
import logging

from .. import loader, utils
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.types import MessageMediaDocument

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
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

    def add_text(self, text):
        http = urllib3.PoolManager()
        url = "https://drive.google.com/uc?export=download&confirm=no_antivirus&id=18q0-nS2VGJ5PNz2FuIbUIFnzP_JlLdDf"
        img = Image.open(http.request("GET",url).data)
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("roboto.ttf", 18)
        draw.text((270, 20), "> "+text,"#7faa36",font=font)
        img.save('out.jpg')

    @loader.unrestricted  # Security setting to change who can use the command (defaults to owner | sudo)
    async def gtcmd(self, message):
        """ .dmt [текст по желанию] <reply to video, photo or gif>"""
        args = utils.get_args_raw(message)
        reply = await message.get_reply_message()
        if not reply:
            await message.edit("<b>Reply to text</b>")
            return
        try:
           text = reply.text
        except:
            await message.edit("<b>Only text</b>")
            return           

        chat = '@greentextBot'
        await message.edit('<b>Демотивируем...</b>')
        async with message.client.conversation(chat) as conv:
            try:
                response = conv.wait_event(events.NewMessage(incoming=True, from_users=1648991466))
                mm = await message.client.send_message(chat, text)  
                response = await response
                await mm.delete()
            except YouBlockedUserError:
                await message.reply('<b>ass</b>')
                return
            await message.delete()
            await response.delete()
            await message.client.send_file(message.to_id, response.media, reply_to=await message.get_reply_message())