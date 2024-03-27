from aiogram import types


button1 = types.KeyboardButton(text='/start')
button2 = types.KeyboardButton(text='/вопрос о записи')
button3 = types.KeyboardButton(text='/вопрос о враче')
button4 = types.KeyboardButton(text='/общая информация о клинике')
button5 = types.KeyboardButton(text='/стоимость за день')

keyboard1 = [
    
 [button1, button2, button3],
 [button4, button5],
]
keyboard2 = [
    
 [button1, button2, button3],

 
] 
 
 

keyboard1 = types.ReplyKeyboardMarkup(keyboard=keyboard1)

keyboard2 = types.ReplyKeyboardMarkup(keyboard=keyboard2)