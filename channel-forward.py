###################################
#
# █▀ █▀▄▀█ █▀█ █░░ █▀█ █░█ █▄▀
# ▄█ █░▀░█ █▄█ █▄▄ █▄█ ▀▄▀ █░█
#           t.me/smolovk_ftg
##################################


# requires: requests numpy

# Must be in any module
from .. import loader, utils
from telethon import types, TelegramClient

import asyncio
import logging


logger = logging.getLogger(__name__)

@loader.tds
class ChannelForwardMod(loader.Module):
    """Forward messages from a channel to chat. Set from and to ids in .config"""  # Docstring for module | Translateable due to @loader.tds

    # Strings used in the messages | Translateable due to @loader.tds
    strings = {
        "name": "ChannelForward",
        "cfg_doc": "Forward messages from a channel to chat. Set from and to ids in .config",
    }

    # If you want to use config, leave this `def` at that
    def __init__(self):
        self.config = loader.ModuleConfig(
            "FROM_ID",
            -1001501288557,
            "Where to take messages",
            "TO_ID",
            -1001699938038,
            "Where to send messages"
        )

    async def watcher(self, message: types.Message):
        # Add this if you want to process only outcoming messages
        if not getattr(message, 'in', False):
            if (message.chat_id == self.config["FROM_ID"]):
                await self.client.send_message(self.config["TO_ID"], message)
            return