import asyncio
import requests
import string
import random
from configs import Config
from pyrogram import Client
from pyrogram.types import Message
from pyrogram.errors import FloodWait
from handlers.helpers import str_to_b64

async def reply_forward(message: Message, file_id: int):
    try:
        await message.reply_text(
            f"</b> ⚠️𝙁𝙞𝙡𝙚𝙨 𝙬𝙞𝙡𝙡 𝙗𝙚 𝙙𝙚𝙡𝙚𝙩𝙚𝙙 𝙞𝙣 30 𝙢𝙞𝙣𝙪𝙩𝙚𝙨 ⏳️ 𝙩𝙤 𝙖𝙫𝙤𝙞𝙙 𝙘𝙤𝙥𝙮𝙧𝙞𝙜𝙝𝙩 ©️ 𝙞𝙨𝙨𝙪𝙚𝙨. 𝙋𝙡𝙚𝙖𝙨𝙚 𝙛𝙤𝙧𝙬𝙖𝙧𝙙 𝙖𝙣𝙙 𝙨𝙖𝙫𝙚 𝙩𝙝𝙚𝙢.\n\n 𝙄𝙛 𝙮𝙤𝙪 𝙬𝙖𝙣𝙩 𝙩𝙤 𝙒𝙖𝙩𝙘𝙝 𝙤𝙣𝙡𝙞𝙣𝙚 𝙏𝙝𝙚𝙣 𝙎𝙚𝙣𝙙 𝙏𝙝𝙞𝙨 𝙁𝙞𝙡𝙚 𝙩𝙤 𝙊𝙪𝙧 𝙎𝙩𝙧𝙚𝙖𝙢𝙞𝙣𝙜 𝘽𝙤𝙩<a href='https://telegram.me/AJxSTREAMING_Bot?start=AJx'>@𝘼𝙅𝙭𝙎𝙏𝙍𝙀𝘼𝙈𝙄𝙉𝙂_𝘽𝙤𝙩 🤖</a> 𝙀𝙣𝙟𝙤𝙮 !!\n\n<a href='https://t.me/How_Download_mOVIES4KHub/26'>#𝙃𝙤𝙬 𝙩𝙤 𝙪𝙨𝙚 𝙎𝙩𝙧𝙚𝙖𝙢 𝘽𝙤𝙩 𝙩𝙪𝙩𝙤𝙧𝙞𝙖𝙡 💡</a>",
            disable_web_page_preview=True,
            quote=True
        )
    except FloodWait as e:
        await asyncio.sleep(e.x)
        await reply_forward(message, file_id)

async def media_forward(bot: Client, user_id: int, file_id: int):
    try:
        if Config.FORWARD_AS_COPY is True:
            return await bot.copy_message(chat_id=user_id, from_chat_id=Config.DB_CHANNEL,
                                          message_id=file_id)
        elif Config.FORWARD_AS_COPY is False:
            return await bot.forward_messages(chat_id=user_id, from_chat_id=Config.DB_CHANNEL,
                                              message_ids=file_id)
    except FloodWait as e:
        await asyncio.sleep(e.value)
        return media_forward(bot, user_id, file_id)
        await message.delete()

async def send_media_and_reply(bot: Client, user_id: int, file_id: int):
    sent_message = await media_forward(bot, user_id, file_id)
    await reply_forward(message=sent_message, file_id=file_id)
    asyncio.create_task(delete_after_delay(sent_message, 1800))

async def delete_after_delay(message, delay):
    await asyncio.sleep(delay)
    await message.delete()
