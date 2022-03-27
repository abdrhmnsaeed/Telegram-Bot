from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from random import randint

bot = Bot(token='5220350839:AAG3WhAPiKQZBLmzQZUnsIsGyhiI1KxyBfM')
dp = Dispatcher(bot)

button1 = InlineKeyboardButton(text="button1", callback_data="randomvalue_of10")
button2 = InlineKeyboardButton(text="button2", callback_data="randomvalue_of100")
button3 = InlineKeyboardButton(text="button3", callback_data="randomvalue_of100")
button4 = InlineKeyboardButton(text="button4", callback_data="randomvalue_of100")
button5 = InlineKeyboardButton(text="button5", callback_data="randomvalue_of100")
keyboard_inline = InlineKeyboardMarkup().add(button1, button2, button3, button4)

keyboard1 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add("AIRTIME", "DATA")
keyboard2 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add("MTN", "AIRTEL", "9MOBLIE", "GLO", "BACK")


@dp.message_handler(commands=['random'])
async def random_answer(message: types.Message):
    await message.reply("Select a range:", reply_markup=keyboard_inline)


@dp.message_handler(commands=['start', 'help'])
async def welcome(message: types.Message):
    await message.reply("Hello! Am amTiredBot, How can i help you?", reply_markup=keyboard1)


@dp.message_handler()
async def serviceSelection(message: types.Message):
    if message.text == 'AIRTIME':
        await message.reply("Select Network", reply_markup=keyboard2)
    elif message.text == 'DATA':
        await message.reply("Select Network", reply_markup=keyboard2)
    elif message.text == 'BACK':
        await message.reply("Select Network", reply_markup=keyboard1)
    else:
        await message.reply(f"Your message is: {message.text}")


executor.start_polling(dp)