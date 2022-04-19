from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
"""Foydalanuvchilar haqida baza filname"""
from utils.db_api.Users_haqida import Database

from data import config

bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
baza = Database(path_to_db='data/Users_baza1.db')