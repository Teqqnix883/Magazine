from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo

bot = Bot('5804359688:AAFS7Q4EBwDQapxb0zeQOVtyEeiCqDyAb1c')
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('Відкрити веб сторінку', web_app=WebAppInfo(url='https://www.instagram.com/vlad.yk/')))
    await message.answer('Привіт, мій друже!', reply_markup=markup)

executor.start_polling(dp)