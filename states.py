from aiogram.fsm.state import State, StatesGroup

class Booking(StatesGroup):
    waiting_date=State()
    waiting_time=State()