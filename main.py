import asyncio
import logging
import sys
from time import sleep

from parser import find_goods
from config import TOKEN

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message


dp = Dispatcher()
bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
current_goods = ""


@dp.message(CommandStart())
async def new_goods(message: Message):
    while True:
        global current_goods
        update_goods = find_goods()
        if update_goods != current_goods:
            current_goods = update_goods
            await message.answer("New goods - " + current_goods)
            sleep(3600)
        else:
            sleep(3600)

async def main() -> None:
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())