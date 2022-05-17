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


# If you have a lot of commands and want to disable docs,
# which are shown when module is loaded, add the comment as
# shown below:

#disable_onload_docs


# If you want to use logging, leave it at that
logger = logging.getLogger(__name__)
# Usage:
#  logger.debug("Text")
#  logger.warning("Text")
#  logger.error("Text")
#  logger.log("Text")
#  logger.critical("Text") and etc...

# Module class must end with `Mod` and contain `loader.Module` in args
# Example: `MODULE_NAMEMod(loader.Module)`
@loader.tds
class YourMod(loader.Module):
    """Example module"""  # Docstring for module | Translateable due to @loader.tds

    # Strings used in the messages | Translateable due to @loader.tds
    strings = {
        "name": "Module's name",
        "cfg_doc": "This is what is said, you can edit me with the configurator",
        "after_sleep": "We have finished sleeping!"
    }

    # If you want to use config, leave this `def` at that
    def __init__(self):
        self.config = loader.ModuleConfig("CONFIG_STRING", "hello", lambda m: self.strings("cfg_doc", m))
        # To get data from config: `self.config["CONFIG_STRING"]`

    # Sometimes you need to use infinite loop. In that case, use the following structure
    async def infinite_loop(self):
        # Infinite loop itself
        while True:
            # Your code goes here
            # Delay between iterations
            await asyncio.sleep(10)

    # `client_ready` is being executed after loading module
    # It also adds support for the database (`self.db = db`) and TelegramClient (`self.client = client`)
    # client can also be access through Message atribute `message.client`
    async def client_ready(self, client, db):
        self.client: TelegramClient = client  # Telethon client

        self.db = db  # FTG Database
        # self.db.get(self.strings('name'), "Key", "Value", `Any`)
        #  `Any` - The value that will be returned if the key is not found
        # self.db.set(self.strings('name'), "Key", "Value")

        # Infinite loop starts here. Do not use `await` for that purpose, bc it is not good
        # Use `asyncio.ensure_future`
        # Also, save this task to `self.loop_task` so we can cancel it later
        self.loop_task = asyncio.ensure_future(self.infinite_loop())

    # `on_unload` is being executed when module is unloading, and is used to stop infinite loops, save data etc
    # This method is being executed only in GeekTG 2.0.4beta+
    # Older versions will just ignore it, so be careful!
    async def on_unload(self):
        # Cancel coroutine of infinite loop
        self.loop_task.cancel()

    # To add a module command, create an asynchronous function that must end with -cmd and contain `self, message` in args 
    # .example == `async def examplecmd(self, message)`
    @loader.owner  # Security setting to change who can use the command (defaults to owner | sudo)
    async def examplecmd(self, message: types.Message):
        """Does something when you type .example (hence, named examplecmd)"""  # Docstrings for command

        logger.debug("We logged something!")  # Example of logging in cmd

        # To get data from config use: `self.config["CONFIG_STRING"]`
        message = await utils.answer(message, self.config["CONFIG_STRING"])

        await asyncio.sleep(5)  # Never use time.sleep, bc it stops execution!

        # Strings usage: `self.strings("STRING", message)` or `self.strings("STRING", message).format(ur_data)`
        # Use `utils.answer(message, <...>)` over `message.edit(<...>)` due to 
        # compatibility (second will not work, if command is executed by another user)
        await utils.answer(message, self.strings("after_sleep", message))

    # In case you want to handle all incoming messages, not just
    # commands, you `watcher`. It receives all incoming messages, 
    # including service messages, so be careful, do not forget
    # to handle various message types and structures
    async def watcher(self, message: types.Message):
        # Add this if you want to process only outcoming messages
        if not getattr(message, 'out', False):
            return

        # Code example
        logger.info(getattr(message, 'raw_text', 'No text'))