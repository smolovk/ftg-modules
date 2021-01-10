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
import urllib, json

from .. import loader, utils

logger = logging.getLogger(__name__)


@loader.tds
class CovidStatsUaMod(loader.Module):
    """Covid statistics for Ukraine module"""

    strings = {
        "name": "Covid stats for UA"
    }

    def __init__(self):
        pass

    def fetch_api(self):
        response = urllib.request.urlopen("https://coronavirus-19-api.herokuapp.com/countries/ukraine")
        response = response.read().decode("utf-8")
        return response

    @loader.unrestricted
    async def covidcmd(self, message):
        await utils.answer(message, self.fetch_api())

    