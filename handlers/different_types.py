from aiogram import Router
from aiogram.types import Message

router = Router()

@router.message()
async def not_a_theme(message: Message):
    await message.answer("Это текстовое сообщение!")
