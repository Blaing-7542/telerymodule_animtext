from pyrogram import Client, filters
from pyrogram.errors import FloodWait
import time


with open("userbot.info", "r") as file:
    lines = file.readlines()
    prefix_userbot = lines[2].strip()

cinfo = f"`{prefix_userbot}animtext`"
ccomand = " анимирует текст."


def command_example(app):
    @app.on_message(filters.command("animtext", prefixes=prefix_userbot) & filters.me)
    async def animtext_command(_, message):
        input_text = message.text.split("animtext ", maxsplit=1)[1]
        temp_text = input_text
        edited_text = ""
        typing_symbol = "█"
        while edited_text != input_text:
            try:
                await message.edit(edited_text + typing_symbol)
                time.sleep(0.1)
                edited_text = edited_text + temp_text[0]
                temp_text = temp_text[1:]
                await message.edit(edited_text)
                time.sleep(0.1)
            except FloodWait:
                print("Превышен лимит сообщений в секунду. Подождите...")

print("Модуль animtext загружен!")
