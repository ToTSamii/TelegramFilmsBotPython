from aiogram import types
from aiogram.filters import Command
from aiogram import filters

from .bot import dp
from .keyBoard import keyBoard_Start, keyBoard_Info, keyBoard_Catalog, keyBoard_Kion, keyBoard_Ivi, keyBoard_Premier

from parsers.parsing_kion import Kion_Parsing
from parsers.parsing_ivi import Ivi_Parsing
from parsers.parsing_premier import Premier_Parsing
from config import user, kion_links, ivi_links, premier_links


#_____________________________main_________________________________


@dp.message(filters.CommandStart())
async def start_handler(message: types.Message) -> None:
    await message.answer(f"Приветствую тебя, {message.from_user.first_name}! Выбери команды из списка и наслаждайся этим шедевром:)\n/info\n/catalog", reply_markup = keyBoard_Start)


@dp.message(Command("info"))
async def handler_info(message: types.Message) -> None:
    await message.answer("Данный бот выдаёт список фильмов по жанрам с трёх популярных сайтов: Kion, Ivi, Premier.", reply_markup = keyBoard_Info)


@dp.message(Command("catalog"))
async def handler_catalog(message: types.Message) -> None:
    await message.answer("Выберите кинотеатр с которого хотите получить данные.", reply_markup = keyBoard_Catalog)


#__________________________________________________________________
#_______________________________kion_______________________________


@dp.message(Command("kion"))
async def handler_kion(message: types.Message) -> None:
    await message.answer("Онлайн-кинотеатр с бесплатными фильмами, сериалами, ТВ каналами и мультфильмами. Смотрите видео в хорошем качестве в любое время на KION.", reply_markup = keyBoard_Kion)


@dp.message(Command("popular_now_kion"))
async def handler_kion_popular_now(message: types.Message) -> None:
    k = Kion_Parsing(user, kion_links["popular_now"])
    info = k.parsing()

    for i in range(0, 10):
        await message.answer("Название: " + info[i]["name"] + "\n" +
                            "Ссылка: " + info[i]["link"] + "\n" +
                            "Оценка: " + info[i]["grade"] + "\n" +
                            "Статус: " + info[i]["status"] + "\n" +
                            "Картинка: " + info[i]["img_link"])

@dp.message(Command("new_kion"))
async def handler_kion_new(message: types.Message) -> None:
    k = Kion_Parsing(user, kion_links["new"])
    info = k.parsing()

    for i in range(0, 10):
        await message.answer("Название: " + info[i]["name"] + "\n" +
                            "Ссылка: " + info[i]["link"] + "\n" +
                            "Оценка: " + info[i]["grade"] + "\n" +
                            "Статус: " + info[i]["status"] + "\n" +
                            "Картинка: " + info[i]["img_link"])


@dp.message(Command("fantastic_kion"))
async def handler_kion_fantastic(message: types.Message) -> None:
    k = Kion_Parsing(user, kion_links["fantastic"])
    info = k.parsing()

    for i in range(0, 10):
        await message.answer("Название: " + info[i]["name"] + "\n" +
                            "Ссылка: " + info[i]["link"] + "\n" +
                            "Оценка: " + info[i]["grade"] + "\n" +
                            "Статус: " + info[i]["status"] + "\n" +
                            "Картинка: " + info[i]["img_link"])


@dp.message(Command("comedy_kion"))
async def handler_kion_comedy(message: types.Message) -> None:
    k = Kion_Parsing(user, kion_links["comedy"])
    info = k.parsing()

    for i in range(0, 10):
        await message.answer("Название: " + info[i]["name"] + "\n" +
                            "Ссылка: " + info[i]["link"] + "\n" +
                            "Оценка: " + info[i]["grade"] + "\n" +
                            "Статус: " + info[i]["status"] + "\n" +
                            "Картинка: " + info[i]["img_link"])


@dp.message(Command("action_kion"))
async def handler_kion_action(message: types.Message) -> None:
    k = Kion_Parsing(user, kion_links["action"])
    info = k.parsing()

    for i in range(0, 10):
        await message.answer("Название: " + info[i]["name"] + "\n" +
                            "Ссылка: " + info[i]["link"] + "\n" +
                            "Оценка: " + info[i]["grade"] + "\n" +
                            "Статус: " + info[i]["status"] + "\n" +
                            "Картинка: " + info[i]["img_link"])


#___________________________________________________________________
#_____________________________ivi___________________________________


@dp.message(Command("ivi"))
async def handler_ivi(message: types.Message) -> None:
    await message.answer("«И́ви» — российский онлайн-кинотеатр. Основан в 2010 году Олегом Тумановым и Дмитрием Алимовым. Один из первых легальных видеосервисов в России. Сервис предоставляет подписку, продажу отдельных фильмов и сериалов, а также монетизирует свой контент за счёт показа рекламы. С 2020 года компания производит оригинальные сериалы", reply_markup = keyBoard_Ivi)


@dp.message(Command("best_ivi"))
async def handler_ivi_best(message: types.Message) -> None:
    k = Ivi_Parsing(user, ivi_links["best"])
    info = k.parsing()

    for i in range(0, 10):
        await message.answer("Название: " + info[i]["name"] + "\n" +
                             "Ссылка: " + info[i]["link"] + "\n" +
                             "Время: " + info[i]["time"] + "\n" +
                             "Оценка: " + info[i]["grade"] + "\n" +
                             "Дата - страна: " + info[i]["date-country"])
        

@dp.message(Command("comedy_ivi"))
async def handler_ivi_comedy(message: types.Message) -> None:
    k = Ivi_Parsing(user, ivi_links["comedy"])
    info = k.parsing()

    for i in range(0, 10):
        await message.answer("Название: " + info[i]["name"] + "\n" +
                             "Ссылка: " + info[i]["link"] + "\n" +
                             "Время: " + info[i]["time"] + "\n" +
                             "Оценка: " + info[i]["grade"] + "\n" +
                             "Дата - страна: " + info[i]["date-country"])
        

@dp.message(Command("fantastic_ivi"))
async def handler_ivi_fantastic(message: types.Message) -> None:
    k = Ivi_Parsing(user, ivi_links["fantastic"])
    info = k.parsing()

    for i in range(0, 10):
        await message.answer("Название: " + info[i]["name"] + "\n" +
                             "Ссылка: " + info[i]["link"] + "\n" +
                             "Время: " + info[i]["time"] + "\n" +
                             "Оценка: " + info[i]["grade"] + "\n" +
                             "Дата - страна: " + info[i]["date-country"])
        

@dp.message(Command("adventures_ivi"))
async def handler_ivi_adventures(message: types.Message) -> None:
    k = Ivi_Parsing(user, ivi_links["adventures"])
    info = k.parsing()

    for i in range(0, 10):
        await message.answer("Название: " + info[i]["name"] + "\n" +
                             "Ссылка: " + info[i]["link"] + "\n" +
                             "Время: " + info[i]["time"] + "\n" +
                             "Оценка: " + info[i]["grade"] + "\n" +
                             "Дата - страна: " + info[i]["date-country"])
        

@dp.message(Command("action_ivi"))
async def handler_ivi_action(message: types.Message) -> None:
    k = Ivi_Parsing(user, ivi_links["action"])
    info = k.parsing()

    for i in range(0, 10):
        await message.answer("Название: " + info[i]["name"] + "\n" +
                             "Ссылка: " + info[i]["link"] + "\n" +
                             "Время: " + info[i]["time"] + "\n" +
                             "Оценка: " + info[i]["grade"] + "\n" +
                             "Дата - страна: " + info[i]["date-country"])


#___________________________________________________________________
#___________________________premier_________________________________


@dp.message(Command("premier"))
async def handler_premier(message: types.Message) -> None:
    await message.answer("Кем бы вы ни были, и что бы ни любили — в онлайн-кинотеатре PREMIER вы найдете фильмы, сериалы, мультфильмы и шоу на свой вкус.", reply_markup = keyBoard_Premier)


@dp.message(Command("comedy_premier"))
async def handler_premier_comedy(message: types.Message) -> None:
    k = Premier_Parsing(user, premier_links["comedy"])
    info = k.parsing()

    for i in range(0, 10):
        await message.answer("Название: " + info[i]["name"] + "\n" +
                             "Описание: " + info[i]["description"] + "\n" +
                             "Ссылка на картинку: " + info[i]["img_link"] + "\n" +
                             "Оценка: " + info[i]["grade"] + "\n" +
                             "Ссылка на трейлер: " + info[i]["trailer_url"])
        

@dp.message(Command("drama_premier"))
async def handler_premier_drama(message: types.Message) -> None:
    k = Premier_Parsing(user, premier_links["drama"])
    info = k.parsing()

    for i in range(0, 10):
        await message.answer("Название: " + info[i]["name"] + "\n" +
                             "Описание: " + info[i]["description"] + "\n" +
                             "Ссылка на картинку: " + info[i]["img_link"] + "\n" +
                             "Оценка: " + info[i]["grade"] + "\n" +
                             "Ссылка на трейлер: " + info[i]["trailer_url"])
        

@dp.message(Command("fantastic_premier"))
async def handler_premier_fantastic(message: types.Message) -> None:
    k = Premier_Parsing(user, premier_links["fantastic"])
    info = k.parsing()

    for i in range(0, 10):
        await message.answer("Название: " + info[i]["name"] + "\n" +
                             "Описание: " + info[i]["description"] + "\n" +
                             "Ссылка на картинку: " + info[i]["img_link"] + "\n" +
                             "Оценка: " + info[i]["grade"] + "\n" +
                             "Ссылка на трейлер: " + info[i]["trailer_url"])
        

@dp.message(Command("adventures_premier"))
async def handler_premier_adventures(message: types.Message) -> None:
    k = Premier_Parsing(user, premier_links["adventures"])
    info = k.parsing()

    for i in range(0, 10):
        await message.answer("Название: " + info[i]["name"] + "\n" +
                             "Описание: " + info[i]["description"] + "\n" +
                             "Ссылка на картинку: " + info[i]["img_link"] + "\n" +
                             "Оценка: " + info[i]["grade"] + "\n" +
                             "Ссылка на трейлер: " + info[i]["trailer_url"])
        

@dp.message(Command("detektiv_premier"))
async def handler_premier_detektiv(message: types.Message) -> None:
    k = Premier_Parsing(user, premier_links["detektiv"])
    info = k.parsing()

    for i in range(0, 10):
        await message.answer("Название: " + info[i]["name"] + "\n" +
                             "Описание: " + info[i]["description"] + "\n" +
                             "Ссылка на картинку: " + info[i]["img_link"] + "\n" +
                             "Оценка: " + info[i]["grade"] + "\n" +
                             "Ссылка на трейлер: " + info[i]["trailer_url"])


#___________________________________________________________________