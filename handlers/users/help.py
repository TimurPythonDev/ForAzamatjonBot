from loader import dp
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp




@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("<b>Buyruqlar:</b>\n\n",
            "/start - Botni ishga tushirish",
            "/help - Yordam",
            "/anketa - Ma'lumotlarni to'ldirish")
    
    await message.answer("\n".join(text))