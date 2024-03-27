import asyncio
import config
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
import logging
import random
from keyboards import keyboard1, keyboard2

logging.basicConfig(level=logging.INFO)

bot = Bot(token=config.token)

dp = Dispatcher()


keyboard2 = types.ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
    [
        types.KeyboardButton(text="Информация")
    ]
])

# Хендлер на команду
@dp.message(Command('start'))
async def cmd_start(message: types.Message):
    name = message.chat.first_name
    await message.answer(f'чем могу помочь, {name}', reply_markup=keyboard2)
    
# Хендлер на команду
@dp.message(Command("вопрос о записи"))
async def cmd_start(message: types.Message):
    name = message.chat.first_name
    await message.answer(f'Сейчас подключится специалист для записи на прием., {name}', reply_markup=keyboard2)    
    
# Хендлер на команду
@dp.message(Command("вопрос о враче"))
async def cmd_start(message: types.Message):
    name = message.chat.first_name
    await message.answer(f'Сейчас подключится специалист для консультации о врачах., {name}', reply_markup=keyboard2)    
    
    
    
# Хендлер на команду
@dp.message(Command("общая информация о клинике"))
async def cmd_start(message: types.Message):
    name = message.chat.first_name
    await message.answer(f'Сейчас подключится специалист для предоставления общей информации о клинике., {name}', reply_markup=keyboard2)  
    
    
    
# Хендлер на команду
@dp.message(Command("стоимость за день"))
async def cmd_start(message: types.Message):
    name = message.chat.first_name
    await message.answer(f'2000 рублей., {name}', reply_markup=keyboard2)       
      
    

# Определение функции main перед местом вызова
async def main():
    await dp.start_polling(bot)

# Вызов функции main
if __name__ == "__main__":
    asyncio.run(main())