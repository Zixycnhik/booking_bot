from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import CallbackQuery, Message

from keyboards import get_appoinments_menu

router = Router()

@router.message(Command("start"))
async def command_start_handler(message: Message) -> None:
    await message.answer(
        "Здравствуйте, вы попали к боту записи на оказание услуг для клиентов! Чем мы можем помочь?",
        reply_markup=get_appoinments_menu(),
    )

@router.callback_query(F.data == "make_appointment")
async def handle_make_appointment(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(
        "На какое время вы желаете записаться?",
        reply_markup=get_appoinments_menu(),
    )

@router.callback_query(F.data == "view_appointment")
async def handle_view_appointment(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(
        "Ваша текущая запись",
        reply_markup=get_appoinments_menu(),
    )
