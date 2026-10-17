from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext

from datetime import datetime, date

from keyboards import get_appoinments_menu, get_services_menu
from config import SERVICES
from states import Booking

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
        "Выберите желаемую услугу",
        reply_markup=get_services_menu(),
    )

@router.callback_query(F.data == "view_appointment")
async def handle_view_appointment(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(
        "Ваша текущая запись",
        reply_markup=get_appoinments_menu(),
    )

@router.callback_query(F.data.startswith("service_"))
async def handle_service_choice(callback: CallbackQuery, state: FSMContext):
    code = callback.data.removeprefix("service_")

    if code not in SERVICES:
        await callback.answer("Выбранной услуги несуществует")
        return

    await callback.answer()
    await state.update_data(service=code)
    await state.set_state(Booking.waiting_date)
    await callback.message.edit_text(
        f"Вы выбрали: {SERVICES[code]}\n"
        "Введите дату в формате ДД.ММ.ГГГГ"    
    )

@router.message(Booking.waiting_date, F.text)
async def handle_date(message: Message, state: FSMContext):
    try:
        chosen_date = datetime.strptime(message.text, "%d.%m.%Y").date()
    except ValueError:
        await message.answer(
            "Введите существующую дату в формате ДД.ММ.ГГГГ"
        )
        return

    if chosen_date < date.today():
        await message.answer("Эта дата уже прошла. Введите другую")
        return

    await state.update_data(date=chosen_date.isoformat())
    await state.set_state(Booking.waiting_time)
    await message.answer(
        f"Дата выбрана: {chosen_date.strftime('%d.%m.%Y')}"
    )
