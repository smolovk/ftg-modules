#    Friendly Telegram (telegram userbot)
#    Copyright (C) 2018-2019 The Authors

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.

#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

import asyncio
import logging

from .. import loader, utils

logger = logging.getLogger(__name__)


@loader.tds
class PolizeiMod(loader.Module):
    """Police lights"""  # Translateable due to @loader.tds
    strings = {"name": "Polizei"}

    def __init__(self):
        pass

    @loader.unrestricted  # Security setting to change who can use the command (defaults to owner | sudo)
    async def polizeicmd(self, message):
        logger.debug("Polizei")
        for i in range(10): 
            await utils.answer(message, "🔵🔴")
            await asyncio.sleep(0.05)
            await utils.answer(message, "🔴🔵")
            await asyncio.sleep(0.05)

