from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder

def choose_crypto() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="XMR")
    kb.button(text="BTC")
    kb.button(text="ZEC")
    kb.button(text="TON")
    kb.button(text="ETH")
    kb.button(text="BCH")
    kb.adjust(3)
    return kb.as_markup(resize_keyboard=True)

def yes_no() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="Да")
    kb.button(text="Нет")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)