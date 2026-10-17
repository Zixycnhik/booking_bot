from os import getenv
from dotenv import load_dotenv

load_dotenv()
TOKEN = getenv("BOT_TOKEN")

SERVICES = {
    "haircut" : "Стрижка",
    "beard" : "Борода",
    "combo" : "Стрижка + борода",
}
