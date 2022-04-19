from aiogram import Dispatcher

from loader import dp
# from .is_admin import AdminFilter
from .Bot import Bot
from .Kanal import Kanal
from .Grups import Grups

if __name__ == "filters":
    #dp.filters_factory.bind(is_admin)
    dp.filters_factory.bind(Grups)
    dp.filters_factory.bind(Kanal)
    dp.filters_factory.bind(Bot)
