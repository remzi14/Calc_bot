from aiogram import types
from keyboards.default.keymenyu import obhavo

from keyboards.inline.calckeyboard import menu
from loader import dp,bot






value = ""

@dp.message_handler(commands="calc")
async def select_message(message: types.Message):
    global value
    await message.answer(value or "0", reply_markup=menu)

@dp.callback_query_handler(lambda call: True)
async def self_calc(query: types.CallbackQuery):
    global value
    data = query.data

    if data == "C":
        value = ""
    elif data == "=":
        try:
            value = str(eval(value))
        except:
            value = "Xatolik"
    elif data != "no":
        value += data

    if value != query.message.text:
        await bot.edit_message_text(
            chat_id=query.message.chat.id,
            message_id=query.message.message_id,
            text=value or "0",
            reply_markup=menu
        )






@dp.message_handler(commands="ob-havo")
@dp.message_handler(commands="Location")
async def select_menu(message:types.Message):
    await message.answer("Manzilingizni yuboring",reply_markup=obhavo)




import requests

WEATHER_API_KEY = "12c82a0790e84ec8ae6154829232611"

@dp.message_handler(content_types=types.ContentTypes.LOCATION)
async def handle_location(message: types.Message):
    latitude = message.location.latitude
    longitude = message.location.longitude

    # WeatherAPI ga so'rov tuzish
    api_url = f"https://api.weatherapi.com/v1/current.json?key={WEATHER_API_KEY}&q={latitude},{longitude}&aqi=yes"
    response = requests.get(api_url)

    if response.status_code == 200:
        weather_data = response.json()
        # Endi  weather_data obyektida foydalanuvchi joylashuvi bo'yicha hozirgi ob-havo ma'lumotlarini topasiz
        # Shu ma'lumotlarni foydalanuvchiga yuboring yoki kerakli vazifalarni bajarishni davom ettirishingiz mumkin
        await message.answer(f"Ob-havo ma'lumotlari: {weather_data}")
    else:
        await message.answer("Ob-havo ma'lumotlarini olishda xatolik yuz berdi. Iltimos, qayta urinib ko'ring.")






