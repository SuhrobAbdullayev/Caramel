import asyncpg
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from data.answers import answers
from keyboards.default.keys import *
from loader import dp, db, bot

class MenuStates(StatesGroup):
    vacancies = State()
    branches = State()
    locations = State()
    positions = State()
    working_hours = State()
    full_name = State()
    gender = State()
    dob = State()
    address = State()
    salary = State()
    marital_status = State()
    experience = State()
    languages = State()
    driver_license = State()
    about_you = State()
    photo = State()
    confirm = State()


@dp.message_handler(CommandStart(), state="*")
async def bot_start(message: types.Message, state: FSMContext):
    try:
        await state.finish()
    except:
        pass
    try:
        user = await db.add_user(telegram_id=message.from_user.id,
                                 full_name=message.from_user.full_name,
                                 username=message.from_user.username)
        await message.answer("assalomu eleykum, tilni tanlang", reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text="O'zbekcha", callback_data="uz"),
                    InlineKeyboardButton(text="Русский", callback_data="ru")
                ]]
        ))
    except asyncpg.exceptions.UniqueViolationError:
        user = await db.select_user(telegram_id=message.from_user.id)
        text = answers[user["lang"]]["welcome"]
        await message.answer(f"{text}", reply_markup=get_main_menu(user["lang"]))

@dp.callback_query_handler(text=["uz", "ru"])
async def choose_language(callback: types.CallbackQuery):
    lang = callback.data
    await db.update_user_lang(telegram_id=callback.from_user.id, lang=lang)

    welcome_text = answers[lang]["welcome"]
    await callback.message.answer(welcome_text, reply_markup=get_main_menu(lang))
    await callback.message.delete()

@dp.message_handler(text=["⚙️ Tilni o'zgartirish", "⚙️ Изменить язык"])
async def change_language(message: types.Message):
    await message.answer("Tilni tanlang:", reply_markup=InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="O'zbekcha", callback_data="uz"),
                InlineKeyboardButton(text="Русский", callback_data="ru")
            ]
        ]
    ))

@dp.message_handler(text=[main_menu_buttons["uz"]["about"], main_menu_buttons["ru"]["about"]])
async def about_us(message: types.Message):
    user = await db.select_user(telegram_id=message.from_user.id)
    lang = user["lang"]
    await message.answer(answers[lang]["about_us"], reply_markup=get_main_menu(lang))

@dp.message_handler(text=[main_menu_buttons["uz"]["contact"], main_menu_buttons["ru"]["contact"]])
async def contact_us(message: types.Message):
    user = await db.select_user(telegram_id=message.from_user.id)
    lang = user["lang"]
    await message.answer(answers[lang]["contact"], reply_markup=get_main_menu(lang))

# vocancies button answers
@dp.message_handler(text=[main_menu_buttons["uz"]["vacancies"], main_menu_buttons["ru"]["vacancies"]])
async def vacancies(message: types.Message):
    user = await db.select_user(telegram_id=message.from_user.id)
    lang = user["lang"]
    await message.answer(answers[lang]["choose_vacancy"], reply_markup=get_vacancies_menu(lang))
    await MenuStates.branches.set()

# branches will be sent here
@dp.message_handler(state=MenuStates.branches)
async def caramel_vacancies(message: types.Message, state: FSMContext):
    user = await db.select_user(telegram_id=message.from_user.id)
    lang = user["lang"]

    if message.text == back_text["uz"]["back"] or message.text == back_text["ru"]["back"]:
        await message.answer(answers[lang]["welcome"], reply_markup=get_main_menu(lang))
        try:
            await state.finish()
        except: pass
        return

    if message.text == vacancies_menu_buttons["uz"]["caramel"] or message.text == vacancies_menu_buttons["ru"]["caramel"]:
        await state.update_data(place = vacancies_menu_buttons[lang]["caramel"])
        await message.answer(answers[lang]["choose_branch"], reply_markup=get_caramel_locations_menu(lang))
        await state.update_data(branch = "caramel")
    elif message.text == vacancies_menu_buttons["uz"]["production"] or message.text == vacancies_menu_buttons["ru"]["production"]:
        await state.update_data(place = vacancies_menu_buttons[lang]["production"])
        await message.answer(answers[lang]["choose_branch"], reply_markup=get_production_locations_menu(lang))
        await state.update_data(branch = "production")
    elif message.text == vacancies_menu_buttons["uz"]["office"] or message.text == vacancies_menu_buttons["ru"]["office"]:
        await state.update_data(place = vacancies_menu_buttons[lang]["office"])
        await message.answer(answers[lang]["choose_branch"], reply_markup=get_production_locations_menu(lang))
        await state.update_data(branch = "office")
    elif message.text == vacancies_menu_buttons["uz"]["terra"] or message.text == vacancies_menu_buttons["ru"]["terra"]:
        await state.update_data(place = vacancies_menu_buttons[lang]["terra"])
        await message.answer(answers[lang]["choose_branch"], reply_markup=get_terra_locations_menu(lang))
        await state.update_data(branch = "terra")
    await MenuStates.locations.set()


# locations will be sent there
@dp.message_handler(state=MenuStates.locations)
async def choose_location(message: types.Message, state: FSMContext):
    user = await db.select_user(telegram_id=message.from_user.id)
    lang = user["lang"]
    data = await state.get_data()
    branch = data.get("branch")

    if message.text == back_text["uz"]["back"] or message.text == back_text["ru"]["back"]:
        await message.answer(answers[lang]["choose_branch"], reply_markup=get_vacancies_menu(lang))
        await MenuStates.branches.set()
        return

# HERE I NEED TO WRITE SENDING LOCATIONS
    if message.text == caramel_locations_buttons["uz"]["abulgazi"] or message.text == caramel_locations_buttons["ru"]["abulgazi"]:
        await message.answer(answers[lang]["choose_position"], reply_markup=get_caramel_vacancies_menu(lang))
        await bot.send_venue(
            chat_id=message.chat.id,
            latitude= 41.55929523566943,
            longitude= 60.6404770846579,
            title="Manzil:",
            address=message.text,
        )
    elif message.text == caramel_locations_buttons["uz"]["pahlavon"] or message.text == caramel_locations_buttons["ru"]["pahlavon"]:
        await message.answer(answers[lang]["choose_position"], reply_markup=get_caramel_vacancies_menu(lang))
        await bot.send_venue(
            chat_id=message.chat.id,
            latitude= 41.556876078474666,
            longitude= 60.6365371693158,
            title="Manzil:",
            address=message.text,
        )
    elif message.text == caramel_locations_buttons["uz"]["xorazmiy"] or message.text == caramel_locations_buttons["ru"]["xorazmiy"]:
        await message.answer(answers[lang]["choose_position"], reply_markup=get_caramel_vacancies_menu(lang))
        await bot.send_venue(
            chat_id=message.chat.id,
            latitude= 41.55647102348824,
            longitude= 60.63084279630266,
            title="Manzil:",
            address=message.text,
        )
    elif message.text == terra_locations_buttons["uz"]["pahlavon2"] or message.text == terra_locations_buttons["ru"]["pahlavon2"]:
        await message.answer(answers[lang]["choose_position"], reply_markup=get_caramel_vacancies_menu(lang))
        await bot.send_venue(
            chat_id=message.chat.id,
            latitude= 41.562841105636316,
            longitude= 60.610507000000005,
            title="Manzil:",
            address=message.text,
        )
    elif message.text == terra_locations_buttons["uz"]["amudaryo"] or message.text == terra_locations_buttons["ru"]["amudaryo"]:
        await message.answer(answers[lang]["choose_position"], reply_markup=get_caramel_vacancies_menu(lang))
        await bot.send_venue(
            chat_id=message.chat.id,
            latitude= 41.558802844127435,
            longitude= 60.655207542328945,
            title="Manzil:",
            address=message.text,
        )
    elif message.text == terra_locations_buttons["uz"]["elobod"] or message.text == terra_locations_buttons["ru"]["elobod"]:
        await message.answer(answers[lang]["choose_position"], reply_markup=get_caramel_vacancies_menu(lang))
        await bot.send_venue(
            chat_id=message.chat.id,
            latitude= 41.37949172076444,
            longitude= 60.37571116931579,
            title="Manzil:",
            address=message.text,
        )

    # Check for caramel locations
    if branch == "caramel" and (message.text in caramel_locations_buttons["uz"].values() or message.text in caramel_locations_buttons["ru"].values()):
        await state.update_data(location=message.text)
        await message.answer(answers[lang]["choose_position"], reply_markup=get_caramel_vacancies_menu(lang))

    # Check for production locations
    elif branch == "production" and (message.text in production_office_locations_buttons["uz"].values() or message.text in production_office_locations_buttons["ru"].values()):
        await state.update_data(location=message.text)
        await message.answer(answers[lang]["choose_position"], reply_markup=get_production_vacancies_menu(lang))
    # Check for office locations
    elif branch == "office" and (message.text in production_office_locations_buttons["uz"].values() or message.text in production_office_locations_buttons["ru"].values()):
        await state.update_data(location=message.text)
        await message.answer(answers[lang]["choose_position"], reply_markup=get_production_vacancies_menu(lang))

    # Check for terra locations
    elif branch == "terra" and (message.text in terra_locations_buttons["uz"].values() or message.text in terra_locations_buttons["ru"].values()):
        await state.update_data(location=message.text)
        await message.answer(answers[lang]["choose_position"], reply_markup=get_terra_vacancies_menu(lang))
    await MenuStates.positions.set()





