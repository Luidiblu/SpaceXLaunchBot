"""
Handles interactions with the discordbots.org API
"""

import aiohttp
import logging

import config

DBL_URL = f"https://discordbots.org/api/bots/{config.BOT_CLIENT_ID}/stats"
DBL_HEADERS = {
    "Authorization": config.API_TOKEN_DBL,
    "Content-Type": "application/json",
}


async def update_guild_count(guild_count: int) -> None:
    """
    Updates the live guild count for the bots discordbots.org page

    :param guild_count: The number of guilds the bot is currently a member of
    :return: None
    """
    logging.info(f"Sending a guild_count of {guild_count} to DBL")

    async with aiohttp.ClientSession() as session:
        await session.post(
            DBL_URL, json={"server_count": guild_count}, headers=DBL_HEADERS
        )
