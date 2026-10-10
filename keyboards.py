from aiogram.utils.keyboard import InlineKeyboardBuilder

def get_appoinments_menu():
    builder = InlineKeyboardBuilder()

    builder.button(text="Записаться на услугу", callback_data="make_appointment")
    builder.button(text="Посмотреть запись", callback_data="view_appointment")

    builder.adjust(2)

    return builder.as_markup()