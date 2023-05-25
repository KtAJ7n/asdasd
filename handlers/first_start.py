from aiogram import Router
from aiogram.filters import Command
from aiogram.filters.text import Text
from aiogram.types import Message, ReplyKeyboardRemove

from keyboards.start_keyboard import choose_crypto, yes_no

router = Router()

@router.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer(
        "Какую криптовалюту планируете использовать?",
        reply_markup=choose_crypto()
    )
    

@router.message(Text(text="xmr", ignore_case=True))
async def answer_xmr(message: Message):
    await message.answer(
        "Вы выбрали xmr(Monero)",
        reply_markup=ReplyKeyboardRemove()
    )
    await message.answer(
        "Продолжим?",
        reply_markup=yes_no()
    )


@router.message(Text(text="zec", ignore_case=True))
async def answer_zec(message: Message):
    await message.answer(
        "Вы выбрали zec(ZCash)",
        reply_markup=ReplyKeyboardRemove()
    )
    await message.answer(
        "Продолжим?",
        reply_markup=yes_no()
    )
@router.message(Text(text="btc", ignore_case=True))
async def answer_btc(message: Message):
    await message.answer(
        "Вы выбрали btc(Bitcoin)",
        reply_markup=ReplyKeyboardRemove()
    )
    await message.answer(
        "Продолжим?",
        reply_markup=yes_no()
    )

@router.message(Text(text="eth", ignore_case=True))
async def answer_eth(message: Message):
    await message.answer(
        "Вы выбрали eth(Etherium)",
        reply_markup=ReplyKeyboardRemove()
    )
    await message.answer(
        "Продолжим?",
        reply_markup=yes_no()
    )

@router.message(Text(text="bch", ignore_case=True))
async def answer_bch(message: Message):
    await message.answer(
        "Вы выбрали bch(Bitcoin cash)",
        reply_markup=ReplyKeyboardRemove()
    )
    await message.answer(
        "Продолжим?",
        reply_markup=yes_no()
    )


@router.message(Text(text="ton", ignore_case=True))
async def answer_ton(message: Message):
    await message.answer(
        "Вы выбрали ton(Toncoin)",
        reply_markup=ReplyKeyboardRemove()
    )
    await message.answer(
        "Продолжим?",
        reply_markup=yes_no()
    )

@router.message(Text(text="да", ignore_case=True))
async def answer_ton(message: Message):
    await message.answer(
        "Хорошо",
        reply_markup=ReplyKeyboardRemove()
    )
    

@router.message(Text(text="нет", ignore_case=True))
async def answer_ton(message: Message):
    await message.answer(
        "Ладно",
        reply_markup=choose_crypto()
    )
    await message.answer(
        "Какую криптовалюту планируете использовать?",
        reply_markup=choose_crypto()
    )