import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import Message, ContentType
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ParseMode
API_TOKEN = "6917946395:AAGBFSZtAuemH9Txpo2xMHqJcNSX8tDqoPg"
bot = Bot(token=API_TOKEN, parse_mode='HTML')
dp = Dispatcher(bot, storage=MemoryStorage())
logging.basicConfig(level=logging.INFO)
malumotlar = {
}  #
class HELPERS(StatesGroup):
    name_helper = State()
    directon = State()
    region = State()
    age = State()
    number = State()
    help = State()
    price = State()
    job = State()
    time = State()
    wants = State()
    info = State()

@dp.message_handler(commands='start')
async def starter(message: Message, state: FSMContext):
    print(message.from_user.id)
    await message.answer(
 f"""Assalomu alaykum <b>{message.from_user.full_name}</b>UstozShogird kanalining rasmiy botiga xush kelibsiz!
 async def direction_taking(message: Message, state: FSMContext):
    malumotlar[message.from_user.id].append(yonlaish)
    a = yonlaish.replace(',', ' ')
    a = a.split()
    print(a)
    print(a)
    search = ''
    for i in a:
        search += f'#{i}  '
        print(search)
        search += "#"+i
    malumotlar[message.from_user.id].append(search)

    print(a)



    await message.answer(
        "<b>🌐 Hudud:</b>\n\nQaysi hududdansiz?\nViloyat nomi, Toshkent shahar yoki Respublikani kiriting.")
    await state.finish()
@@ -123,30 +125,56 @@ async def job_taking(message: Message, state: FSMContext):
    await state.finish()
    await HELPERS.time.set()

    @dp.message_handler(state=HELPERS.time)
    async def time_taking(message: Message, state: FSMContext):
@dp.message_handler(state=HELPERS.time)
async def time_taking(message: Message, state: FSMContext):
        time_2 = message.text
        malumotlar[message.from_user.id].append(time_2)
        print(time_2)
        print(malumotlar)

        await message.answer(f"""

      Ma'lumotlarga ko'ra:
    👨‍💼Xodim: <b>{malumotlar[message.from_user.id][0]}</b>
    🕑Yosh: <b>{malumotlar[message.from_user.id][4]}</b>
    📚Texnologiya:<b>{malumotlar[message.from_user.id][1]}</b>
    🇺🇿Telegram:<b>@{message.from_user.username}</b>
    📞Aloqa:<b>{malumotlar[message.from_user.id][5]}</b>
    🌐Hudud:<b>{malumotlar[message.from_user.id][3]}</b>
    💰Narxi: <b>{malumotlar[message.from_user.id][6]}</b>
    👨🏻‍💻Kasbi: <b>{malumotlar[message.from_user.id][7]}</b>
    🕰 Murojaat qilish vaqti: <b>{malumotlar[message.from_user.id][8]}
    {malumotlar[message.from_user.id][2]} </b>""")


     Ma'lumotlarga ko'ra:(
👨‍💼 Xodim: <b>{malumotlar[message.from_user.id][0]}</b>
🕑 Yosh: <b>{malumotlar[message.from_user.id][4]}</b>
📚 Texnologiya: <b>{malumotlar[message.from_user.id][1]}</b>
🇺🇿 Telegram: <b>@{message.from_user.username}</b>
📞 Aloqa: <b>{malumotlar[message.from_user.id][5]}</b>
🌐 Hudud: <b>{malumotlar[message.from_user.id][3]}</b>
💰 Narxi: <b>{malumotlar[message.from_user.id][6]}</b>
👨🏻‍💻 Kasbi: <b>{malumotlar[message.from_user.id][7]}</b>
🕰 Murojaat qilish vaqti: <b>{malumotlar[message.from_user.id][8]}
{malumotlar[message.from_user.id][2]}</b>""")
    await message.answer("Barcha ma`lumotlar to`g`rimi ?")
    await state.finish()


@dp.message_handler(content_types=types.ContentType.TEXT)
async def rozilik(message:types.Message):
    if message.text == 'ha':
        await bot.send_message(6216398846,f"""
Ma'lumotlarga ko'ra:
👨‍💼 Xodim: <b>{malumotlar[message.from_user.id][0]}</b>
🕑 Yosh: <b>{malumotlar[message.from_user.id][4]}</b>
📚 Texnologiya: <b>{malumotlar[message.from_user.id][1]}</b>
🇺🇿 Telegram: <b>@{message.from_user.username}</b>
📞 Aloqa: <b>{malumotlar[message.from_user.id][5]}</b>
🌐 Hudud: <b>{malumotlar[message.from_user.id][3]}</b>
💰 Narxi: <b>{malumotlar[message.from_user.id][6]}</b>
👨🏻‍💻 Kasbi: <b>{malumotlar[message.from_user.id][7]}</b>
🕰 Murojaat qilish vaqti: <b>{malumotlar[message.from_user.id][8]}
{malumotlar[message.from_user.id][2]}
</b>""")

    elif message.text == 'yoq':
        await message.answer('Ma`lumotlaringizni qaytib kriting!')
        await message.answer("<b>Ism, familiyangizni kiriting?</b>")
        await HELPERS.name_helper.set()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)














