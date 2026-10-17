from aiogram.utils.keyboard import InlineKeyboardBuilder
from config import SERVICES

def get_appoinments_menu():
    builder = InlineKeyboardBuilder()

    builder.button(text="Записаться на услугу", callback_data="make_appointment")
    builder.button(text="Посмотреть запись", callback_data="view_appointment")

    builder.adjust(2)

    return builder.as_markup()

def get_services_menu():
    builder = InlineKeyboardBuilder()

    for code, name in SERVICES.items():
        builder.button(text=name, callback_data=f"service_{code}")

    builder.adjust(1)

    return builder.as_markup()