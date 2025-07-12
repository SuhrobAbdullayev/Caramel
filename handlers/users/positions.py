from aiogram import types
from aiogram.dispatcher import FSMContext

from data.answers import answers
from handlers.users.start import MenuStates
from keyboards.default.keys import caramel_vacancies_buttons, office_vacancies_buttons, production_vacancies_buttons, \
    terra_vacancies_buttons, work_time, get_main_menu, back_text, get_gender, \
    get_back_button, get_confirm_keyboard, get_caramel_vs_terra_menu, get_tera_work_time_menu, \
    get_caramel_work_time_menu
from loader import dp, db, bot


def keyFinder(item):
    if item in caramel_vacancies_buttons["uz"].values():
        for key, value in caramel_vacancies_buttons["uz"].items():
            if value == item:
                return key
    elif item in caramel_vacancies_buttons["ru"].values():
        for key, value in caramel_vacancies_buttons["ru"].items():
            if value == item:
                return key
    elif item in office_vacancies_buttons["uz"].values():
        for key, value in office_vacancies_buttons["uz"].items():
            if value == item:
                return key
    elif item in office_vacancies_buttons["ru"].values():
        for key, value in office_vacancies_buttons["ru"].items():
            if value == item:
                return key
    elif item in production_vacancies_buttons["uz"].values():
        for key, value in production_vacancies_buttons["uz"].items():
            if value == item:
                return key
    elif item in production_vacancies_buttons["ru"].values():
        for key, value in production_vacancies_buttons["ru"].items():
            if value == item:
                return key
    elif item in terra_vacancies_buttons["uz"].values():
        for key, value in terra_vacancies_buttons["uz"].items():
            if value == item:
                return key
    elif item in terra_vacancies_buttons["ru"].values():
        for key, value in terra_vacancies_buttons["ru"].items():
            if value == item:
                return key
    return None

@dp.message_handler(state=MenuStates.positions)
async def handle_vacancies(message: types.Message, state: FSMContext):
    user = await db.select_user(telegram_id=message.from_user.id)
    lang = user["lang"]
    key = keyFinder(message.text)
    if message.text in [back_text["uz"]["back"], back_text["ru"]["back"]]:
        await message.answer(answers[lang]["choose_vacancy"], reply_markup=get_caramel_vs_terra_menu(lang))
        await MenuStates.branches.set()
        return
    if key:
        position_info = await db.get_position(key, lang)
        if position_info:
            await message.answer(position_info[lang])
            data = await state.get_data()
            branch = data.get("branch")
            if branch == "terra":
                await message.answer(answers[lang]["working_hours"], reply_markup=get_tera_work_time_menu(lang))
            else:
                await message.answer(answers[lang]["working_hours"], reply_markup=get_caramel_work_time_menu(lang))
            await state.update_data(position=message.text)
            await MenuStates.working_hours.set()
        else:
            await message.answer("Error: /start")
    else:
        await message.answer("Error: /start")

@dp.message_handler(state=MenuStates.working_hours)
async def handle_working_hours(message: types.Message, state: FSMContext):
    user = await db.select_user(telegram_id=message.from_user.id)
    lang = user["lang"]

    if message.text in [back_text["uz"]["back"], back_text["ru"]["back"]]:
        await message.answer(answers[lang]["choose_vacancy"], reply_markup=get_caramel_vs_terra_menu(lang))
        await MenuStates.branches.set()
        return
    elif message.text in [back_text["uz"]["main"], back_text["ru"]["main"]]:
        await message.answer(answers[lang]["welcome"], reply_markup=get_main_menu(lang))
        try:
            await state.finish()
        except: pass
        return
    elif message.text in [back_text["uz"]["boshqa"], back_text["ru"]["boshqa"]]:
        await message.answer(answers[lang]["another_working_hours"], reply_markup=get_back_button(lang))
        await MenuStates.another_hours.set()
        return
    else:
        if message.text in work_time[lang].values():
            await state.update_data(working_hours=message.text)
            await message.answer(answers[lang]["ask_fullname"], reply_markup=get_back_button(lang))
            await MenuStates.full_name.set()
        else:
            await message.answer("Error: /start")
            try:
                await state.finish()
            except: pass

@dp.message_handler(state=MenuStates.another_hours)
async def handle_another_hours(message: types.Message, state: FSMContext):
    user = await db.select_user(telegram_id=message.from_user.id)
    lang = user["lang"]

    if message.text in [back_text["uz"]["back"], back_text["ru"]["back"]]:
        await message.answer(answers[lang]["choose_vacancy"], reply_markup=get_caramel_vs_terra_menu(lang))
        await MenuStates.branches.set()
        return

    await state.update_data(working_hours=message.text)
    await message.answer(answers[lang]["ask_fullname"], reply_markup=get_back_button(lang))
    await MenuStates.full_name.set()

@dp.message_handler(state=MenuStates.full_name)
async def handle_full_name(message: types.Message, state: FSMContext):
    user = await db.select_user(telegram_id=message.from_user.id)
    lang = user["lang"]
    if message.text in [back_text["uz"]["back"], back_text["ru"]["back"]]:
        await message.answer(answers[lang]["choose_vacancy"], reply_markup=get_caramel_vs_terra_menu(lang))
        await MenuStates.branches.set()
        return

    full_name = message.text
    await state.update_data(full_name=full_name)
    await message.answer(answers[lang]["ask_gender"], reply_markup=get_gender(lang))
    await MenuStates.gender.set()

@dp.message_handler(state=MenuStates.gender)
async def handle_gender(message: types.Message, state: FSMContext):
    user = await db.select_user(telegram_id=message.from_user.id)
    lang = user["lang"]
    if message.text in [back_text["uz"]["back"], back_text["ru"]["back"]]:
        await message.answer(answers[lang]["choose_vacancy"], reply_markup=get_caramel_vs_terra_menu(lang))
        await MenuStates.branches.set()
        return
    await state.update_data(gender=message.text)
    await message.answer(answers[lang]["ask_dob"], reply_markup=get_back_button(lang))
    await MenuStates.dob.set()

@dp.message_handler(state=MenuStates.dob)
async def handle_dob(message: types.Message, state: FSMContext):
    user = await db.select_user(telegram_id=message.from_user.id)
    lang = user["lang"]
    if message.text in [back_text["uz"]["back"], back_text["ru"]["back"]]:
        await message.answer(answers[lang]["choose_vacancy"], reply_markup=get_caramel_vs_terra_menu(lang))
        await MenuStates.branches.set()
        return
    await state.update_data(dob=message.text)
    await message.answer(answers[lang]["ask_address"], reply_markup=get_back_button(lang))
    await MenuStates.address.set()

@dp.message_handler(state=MenuStates.address)
async def handle_address(message: types.Message, state: FSMContext):
    user = await db.select_user(telegram_id=message.from_user.id)
    lang = user["lang"]
    if message.text in [back_text["uz"]["back"], back_text["ru"]["back"]]:
        await message.answer(answers[lang]["choose_vacancy"], reply_markup=get_caramel_vs_terra_menu(lang))
        await MenuStates.branches.set()
        return
    await state.update_data(address=message.text)
    await message.answer(answers[lang]["ask_salary"], reply_markup=get_back_button(lang))
    await MenuStates.salary.set()

@dp.message_handler(state=MenuStates.salary)
async def handle_salary(message: types.Message, state: FSMContext):
    user = await db.select_user(telegram_id=message.from_user.id)
    lang = user["lang"]
    if message.text in [back_text["uz"]["back"], back_text["ru"]["back"]]:
        await message.answer(answers[lang]["choose_vacancy"], reply_markup=get_caramel_vs_terra_menu(lang))
        await MenuStates.branches.set()
        return
    await state.update_data(salary=message.text)
    await message.answer(answers[lang]["ask_marital_status"], reply_markup=get_back_button(lang))
    await MenuStates.marital_status.set()

@dp.message_handler(state=MenuStates.marital_status)
async def handle_marital_status(message: types.Message, state: FSMContext):
    user = await db.select_user(telegram_id=message.from_user.id)
    lang = user["lang"]
    if message.text in [back_text["uz"]["back"], back_text["ru"]["back"]]:
        await message.answer(answers[lang]["choose_vacancy"], reply_markup=get_caramel_vs_terra_menu(lang))
        await MenuStates.branches.set()
        return
    await state.update_data(marital_status=message.text)
    await message.answer(answers[lang]["ask_experience"], reply_markup=get_back_button(lang))
    await MenuStates.experience.set()

@dp.message_handler(state=MenuStates.experience)
async def handle_experience(message: types.Message, state: FSMContext):
    user = await db.select_user(telegram_id=message.from_user.id)
    lang = user["lang"]
    if message.text in [back_text["uz"]["back"], back_text["ru"]["back"]]:
        await message.answer(answers[lang]["choose_vacancy"], reply_markup=get_caramel_vs_terra_menu(lang))
        await MenuStates.branches.set()
        return
    await state.update_data(experience=message.text)
    await message.answer(answers[lang]["ask_languages"], reply_markup=get_back_button(lang))
    await MenuStates.languages.set()

@dp.message_handler(state=MenuStates.languages)
async def handle_languages(message: types.Message, state: FSMContext):
    user = await db.select_user(telegram_id=message.from_user.id)
    lang = user["lang"]
    if message.text in [back_text["uz"]["back"], back_text["ru"]["back"]]:
        await message.answer(answers[lang]["choose_vacancy"], reply_markup=get_caramel_vs_terra_menu(lang))
        await MenuStates.branches.set()
        return
    await state.update_data(languages=message.text)
    await message.answer(answers[lang]["ask_driver_license"], reply_markup=get_back_button(lang))
    await MenuStates.driver_license.set()

@dp.message_handler(state=MenuStates.driver_license)
async def handle_driver_license(message: types.Message, state: FSMContext):
    user = await db.select_user(telegram_id=message.from_user.id)
    lang = user["lang"]
    if message.text in [back_text["uz"]["back"], back_text["ru"]["back"]]:
        await message.answer(answers[lang]["choose_vacancy"], reply_markup=get_caramel_vs_terra_menu(lang))
        await MenuStates.branches.set()
        return
    await state.update_data(driver_license=message.text)
    await message.answer(answers[lang]["ask_about_you"], reply_markup=get_back_button(lang))
    await MenuStates.about_you.set()

@dp.message_handler(state=MenuStates.about_you)
async def handle_about_you(message: types.Message, state: FSMContext):
    user = await db.select_user(telegram_id=message.from_user.id)
    lang = user["lang"]
    if message.text in [back_text["uz"]["back"], back_text["ru"]["back"]]:
        await message.answer(answers[lang]["choose_vacancy"], reply_markup=get_caramel_vs_terra_menu(lang))
        await MenuStates.branches.set()
        return
    await state.update_data(about_you=message.text)
    await message.answer(answers[lang]["ask_phone"], reply_markup=get_back_button(lang))
    await MenuStates.phone_number.set()

@dp.message_handler(state=MenuStates.phone_number)
async def handle_phone_number(message: types.Message, state: FSMContext):
    user = await db.select_user(telegram_id=message.from_user.id)
    lang = user["lang"]

    if message.text in [back_text["uz"]["back"], back_text["ru"]["back"]]:
        await message.answer(answers[lang]["choose_vacancy"], reply_markup=get_caramel_vs_terra_menu(lang))
        await MenuStates.branches.set()
        return

    await state.update_data(phone_number=message.text)

    await message.answer(answers[lang]["ask_photo"], reply_markup=get_back_button(lang))
    await MenuStates.photo.set()

@dp.message_handler(content_types=types.ContentType.PHOTO, state=MenuStates.photo)
async def handle_photo(message: types.Message, state: FSMContext):
    user = await db.select_user(telegram_id=message.from_user.id)
    lang = user["lang"]

    photo_id = message.photo[-1].file_id
    await state.update_data(photo=photo_id)

    data = await state.get_data()

    # Generate confirmation text directly here
    if lang == "uz":
        confirmation_text = (
            f"👤 Ism, familiya, otasining ismi: {data.get('full_name', '-')}\n"
            f"🚻 Jinsi: {data.get('gender', '-')}\n"
            f"🎂 Tug'ilgan sana: {data.get('dob', '-')}\n"
            f"🏠 Yashash manzili: {data.get('address', '-')}\n"
            f"💰 Istalgan maosh: {data.get('salary', '-')}\n"
            f"💍 Oilaviy holati: {data.get('marital_status', '-')}\n"
            f"💼 Tajriba: {data.get('experience', '-')}\n"
            f"🌐 Chet tillari: {data.get('languages', '-')}\n"
            f"🚘 Haydovchilik guvohnomasi: {data.get('driver_license', '-')}\n"
            f"📝 O'zingiz haqingizda: {data.get('about_you', '-')}\n"
            f"⏰ Ish vaqti: {data.get('working_hours', '-')}\n"
            f"🏢 Lavozim: {data.get('position', '-')}\n"
            f"📍 Filial: {data.get('location', '-')}\n"
            f"🏭 Bo'lim: {data.get('place', '-')}\n"
            f"📱 Telefon raqami: {data.get('phone_number', '-')}\n"
        )
    else:
        confirmation_text = (
            f"👤 ФИО: {data.get('full_name', '-')}\n"
            f"🚻 Пол: {data.get('gender', '-')}\n"
            f"🎂 Дата рождения: {data.get('dob', '-')}\n"
            f"🏠 Адрес проживания: {data.get('address', '-')}\n"
            f"💰 Желаемая зарплата: {data.get('salary', '-')}\n"
            f"💍 Семейное положение: {data.get('marital_status', '-')}\n"
            f"💼 Опыт работы: {data.get('experience', '-')}\n"
            f"🌐 Языки: {data.get('languages', '-')}\n"
            f"🚘 Водительские права: {data.get('driver_license', '-')}\n"
            f"📝 О себе: {data.get('about_you', '-')}\n"
            f"⏰ График работы: {data.get('working_hours', '-')}\n"
            f"🏢 Должность: {data.get('position', '-')}\n"
            f"📍 Филиал: {data.get('location', '-')}\n"
            f"🏭 Отдел: {data.get('place', '-')}\n"
            f"📱 Номер телефона: {data.get('phone_number', '-')}\n"
        )

    await message.answer(answers[lang]["check_info"])

    await bot.send_photo(
        chat_id=message.chat.id,
        photo=photo_id,
        caption=confirmation_text[:1024],  # Telegram caption limit
        reply_markup=get_confirm_keyboard(lang)
    )

    await MenuStates.confirm.set()


@dp.message_handler(lambda m: m.text in [back_text["uz"]["back"], back_text["ru"]["back"]], state=MenuStates.photo)
async def handle_photo_back(message: types.Message, state: FSMContext):
    user = await db.select_user(telegram_id=message.from_user.id)
    lang = user["lang"]

    await message.answer(answers[lang]["choose_vacancy"], reply_markup=get_caramel_vs_terra_menu(lang))
    await MenuStates.branches.set()


@dp.callback_query_handler(text="confirm", state=MenuStates.confirm)
async def process_confirm(callback: types.CallbackQuery, state: FSMContext):
    user = await db.select_user(telegram_id=callback.from_user.id)
    lang = user["lang"]

    await bot.copy_message(
        chat_id=1029949773,
        from_chat_id=callback.message.chat.id,
        message_id=callback.message.message_id
    )
    await bot.copy_message(
        chat_id=1051264616,
        from_chat_id=callback.message.chat.id,
        message_id=callback.message.message_id
    )
    await callback.message.answer(answers[lang]["done"], reply_markup=get_main_menu(lang))
    await callback.message.delete()
    try:
        await state.finish()
    except: pass

@dp.callback_query_handler(text="cancel", state=MenuStates.confirm)
async def process_cancel(callback: types.CallbackQuery, state: FSMContext):
    user = await db.select_user(telegram_id=callback.from_user.id)
    lang = user["lang"]

    await callback.message.answer(answers[lang]["welcome"], reply_markup=get_main_menu(lang))
    await callback.message.delete()
    try:
        await state.finish()
    except: pass


@dp.message_handler(text=[back_text["uz"]["back"], back_text["ru"]["back"]], state=MenuStates.confirm)
async def handle_back_in_confirm(message: types.Message, state: FSMContext):
    user = await db.select_user(telegram_id=message.from_user.id)
    lang = user["lang"]
    await message.answer(answers[lang]["welcome"], reply_markup=get_main_menu(lang))
    try:
        await state.finish()
    except: pass



