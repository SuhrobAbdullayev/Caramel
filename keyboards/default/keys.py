from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

from data.answers import answers

back_text = {
    "uz": {
        "main": "Bosh menyu",
        "pass": "O`tkazib yuborish",
        "back": "Orqaga"
    },
    "ru": {
        "main": "Главное меню",
        "pass": "Пропустить",
        "back": "Назад"
    }
}

# ----------------------------------- MAIN MENU -----------------------------------
main_menu_buttons = {
    "uz": {
        "about": "Biz haqimizda",
        "vacancies": "Vakansiyalar",
        "contact": "Biz bilan bog'lanish",
        "language": "⚙️ Tilni o'zgartirish",
    },
    "ru": {
        "about": "О нас",
        "vacancies": "Вакансии",
        "contact": "Связаться с нами",
        "language": "⚙️ Изменить язык",
    }
}


def get_main_menu(lang):
    t = main_menu_buttons[lang]
    markup = ReplyKeyboardMarkup(resize_keyboard=True)

    markup.add(KeyboardButton(t["about"]))
    markup.add(KeyboardButton(t["vacancies"]))
    markup.row(KeyboardButton(t["contact"]), KeyboardButton(t["language"]))

    return markup

# ------------------------------------ END OF MAIN MENU ------------------------------------

# ----------------------------------- Vacancies button -----------------------------------

vacancies_menu_buttons = {
    "uz": {
        "caramel": "Caramel Magazin",
        "production": "Ishlab chiqarish",
        "terra": "Terra cafeteria",
        "office": "Ofis",
    },
    "ru": {
        "caramel": "Карамель Магазин",
        "production": "Производство",
        "terra": "Кафе Терра",
        "office": "Офис",
    }
}

def get_vacancies_menu(lang):
    t = vacancies_menu_buttons[lang]
    b = back_text[lang]
    markup = ReplyKeyboardMarkup(resize_keyboard=True)

    markup.add(KeyboardButton(t["caramel"]), KeyboardButton(t["production"]))
    markup.add(KeyboardButton(t["terra"]), KeyboardButton(t["office"]))
    markup.row(KeyboardButton(b["back"]))

    return markup
# ------------------------------------ END OF Vacancies button ------------------------------------

# ----------------------------------- Caramel Locations -----------------------------------

caramel_locations_buttons = {
    "uz": {
        "abulgazi": "Abulg'ozi Bahodirxon 150A",
        "pahlavon": "Pahlavon Mahmud 31",
        "xorazmiy": "Al-Xorazmiy ko'chasi 67",
    },
    "ru": {
        "abulgazi": "Абулгазий Бахадирхон 150A",
        "pahlavon": "Пахлавон Махмуд 31",
        "xorazmiy": "Ал-Хоразмий кочаси 67",
    }
}

def get_caramel_locations_menu(lang):
    t = caramel_locations_buttons[lang]
    b = back_text[lang]
    markup = ReplyKeyboardMarkup(resize_keyboard=True)

    markup.add(KeyboardButton(t["abulgazi"]))
    markup.add(KeyboardButton(t["pahlavon"]))
    markup.add(KeyboardButton(t["xorazmiy"]))
    markup.row(KeyboardButton(b["back"]))

    return markup

# ------------------------------------ END OF Caramel locations ------------------------------------

# ------------------------------------ Production and office locations ------------------------------------
production_office_locations_buttons = {
    "uz": {
        "abulgazi": "Abulg'ozi Bahodirxon 150A",
    },
    "ru": {
        "abulgazi": "Абулгазий Бахадирхон 150A",
    }
}
def get_production_locations_menu(lang):
    t = production_office_locations_buttons[lang]
    b = back_text[lang]
    markup = ReplyKeyboardMarkup(resize_keyboard=True)

    markup.add(KeyboardButton(t["abulgazi"]))
    markup.row(KeyboardButton(b["back"]))

    return markup

# ------------------------------------ END OF Production and office locations ------------------------------------

# ------------------------------------ Terra locations ------------------------------------

terra_locations_buttons = {
    "uz": {
        "pahlavon2": "Pahlavon Mahmud 220A",
        "amudaryo": "Amudaryo ko'chasi 19",
        "elobod": "Elobod 112/1",
    },
    "ru": {
        "pahlavon2": "Пахлавон Махмуд 220A",
        "amudaryo": "Амударё кочаси 19",
        "elobod": "Элобод 112/1",
    }
}
def get_terra_locations_menu(lang):
    t = terra_locations_buttons[lang]
    b = back_text[lang]
    markup = ReplyKeyboardMarkup(resize_keyboard=True)

    markup.add(KeyboardButton(t["pahlavon2"]))
    markup.add(KeyboardButton(t["amudaryo"]))
    markup.add(KeyboardButton(t["elobod"]))
    markup.row(KeyboardButton(b["back"]))

    return markup
# ------------------------------------ END OF Terra locations ------------------------------------


# ------------------------------------ Caramel vacancies ------------------------------------

caramel_vacancies_buttons = {
    "uz": {
        "afitsant": "Afitsant",
        "barista": "Barista",
        "farrosh": "Farrosh",
        "sotuvchi": "Sotuvchi",
        "kassir": "Kassir",
    },
    "ru": {
        "afitsant": "Официант",
        "barista": "Бариста",
        "farrosh": "Уборщик",
        "sotuvchi": "Продавец",
        "kassir": "Кассир",
    }
}

def get_caramel_vacancies_menu(lang):
    t = caramel_vacancies_buttons[lang]
    b = back_text[lang]
    markup = ReplyKeyboardMarkup(resize_keyboard=True)

    markup.add(KeyboardButton(t["afitsant"]), KeyboardButton(t["barista"]))
    markup.add(KeyboardButton(t["farrosh"]), KeyboardButton(t["sotuvchi"]))
    markup.add(KeyboardButton(t["kassir"]))
    markup.row(KeyboardButton(b["back"]))

    return markup

# ------------------------------------ END OF Caramel vacancies ------------------------------------

# ------------------------------------ Office vacancies ------------------------------------

office_vacancies_buttons = {
    "uz": {
        "smm": "Instagram SMM",
        "buxgalteriya": "Buxgalteriya",
        "hr": "HR manager",
        "farrosh": "Farrosh",
    },
    "ru": {
        "smm": "Instagram SMM",
        "buxgalteriya": "Бухгалтерия",
        "hr": "HR менеджер",
        "farrosh": "Уборщик",
    }
}

def get_office_vacancies_buttons(lang):
    t = office_vacancies_buttons[lang]
    b = back_text[lang]
    markup = ReplyKeyboardMarkup(resize_keyboard=True)

    markup.add(KeyboardButton(t["smm"]), KeyboardButton(t["buxgalteriya"]))
    markup.add(KeyboardButton(t["hr"]), KeyboardButton(t["farrosh"]))
    markup.row(KeyboardButton(b["back"]))

    return markup

# ------------------------------------ END OF office vacancies ------------------------------------

# ------------------------------------ Production vacancies ------------------------------------
production_vacancies_buttons = {
    "uz": {
        "qandolatchi": "Qandolatchi",
        "marozilshik": "Marozilshik",
        "haydovchi": "Haydovchi",
        "farrosh": "Farrosh",
        "yukchi": "Yuk tashuvchi",
    },
    "ru": {
        "qandolatchi": "Кондитер",
        "marozilshik": "Морозильщик",
        "haydovchi": "Водитель",
        "farrosh": "Уборщик",
        "yukchi": "Грузчик",
    }
}

def get_production_vacancies_menu(lang):
    t = production_vacancies_buttons[lang]
    b = back_text[lang]
    markup = ReplyKeyboardMarkup(resize_keyboard=True)

    markup.add(KeyboardButton(t["qandolatchi"]), KeyboardButton(t["marozilshik"]))
    markup.add(KeyboardButton(t["haydovchi"]), KeyboardButton(t["farrosh"]))
    markup.add(KeyboardButton(t["yukchi"]))
    markup.row(KeyboardButton(b["back"]))

    return markup
# ------------------------------------ END OF Production vacancies ------------------------------------

# ------------------------------------ Terra vacancies ------------------------------------

terra_vacancies_buttons = {
    "uz": {
        "barista": "Barista",
        "farrosh": "Farrosh",
    },
    "ru": {
        "barista": "Бариста",
        "farrosh": "Уборщик",
    }
}

def get_terra_vacancies_menu(lang):
    t = terra_vacancies_buttons[lang]
    b = back_text[lang]
    markup = ReplyKeyboardMarkup(resize_keyboard=True)

    markup.add(KeyboardButton(t["barista"]), KeyboardButton(t["farrosh"]))
    markup.row(KeyboardButton(b["back"]))

    return markup

# ------------------------------------ END OF Terra vacancies ------------------------------------

# ------------------------------------ Working time ----------------------------------------------

work_time = {
    "uz": {
        "kunduzgi": "8:00 - 16:00 (1-smena)",
        "kechki": "16:00 - 23:00 (2-smena)",
        "toliq": "Toliq ish kuni",
        "harqanday": "Har qanday grafik",
    },
    "ru": {
        "kunduzgi": "8:00 - 16:00 (1-смена)",
        "kechki": "16:00 - 23:00 (2-смена)",
        "toliq": "Полный рабочий день",
        "harqanday": "Любой график",
    }
}

def get_work_time_menu(lang):
    t = work_time[lang]
    b = back_text[lang]
    markup = ReplyKeyboardMarkup(resize_keyboard=True)

    markup.add(KeyboardButton(t["kunduzgi"]), KeyboardButton(t["kechki"]))
    markup.add(KeyboardButton(t["toliq"]), KeyboardButton(t["harqanday"]))
    markup.row(KeyboardButton(b["main"]), KeyboardButton(b["back"]))

    return markup


# ------------------------------------ END OF Working time ----------------------------------------------


# ------------------------------------ Back button ----------------------------------------------

def get_back_button(lang):
    t = back_text[lang]
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(KeyboardButton(t["back"]))
    return markup

# ------------------------------------ END OF Back button ----------------------------------------------

# ------------------------------------ Ask gender ----------------------------------------------

gender_text = {
    "uz": {
        "male": "Erkak",
        "female": "Ayol",
    },
    "ru": {
        "male": "Мужчина",
        "female": "Женщина",
    }
}

def get_gender(lang):
    t = gender_text[lang]
    b = back_text[lang]
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(KeyboardButton(t["male"]), KeyboardButton(t["female"]))
    markup.add(KeyboardButton(b["back"]))
    return markup

# --------------------------------

def get_confirm_keyboard(lang):
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=answers[lang]["confirm"], callback_data="confirm")],
        [InlineKeyboardButton(text=answers[lang]["cancel"], callback_data="cancel")]
    ])