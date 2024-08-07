from config import TOKEN
from telegram_bot.bot import Tg_Bot


def main():
    Tg_Bot(TOKEN)


if __name__ == "__main__" :
    try:
        main()
    except:
        print("Ошибка MAIN")