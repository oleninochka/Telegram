from re import compile

from aiogram.filters import Command

AnyCommand = Command(compile(r'.*'))
