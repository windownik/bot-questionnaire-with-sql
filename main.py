from aiogram import executor
from modules.dispatcher import dp
import time
import threading


def sleeper():
    while True:
        with open('modules/database.db', 'rb') as file:
            pass
        file.close()
        time.sleep(1200)


if __name__ == '__main__':
    t = threading.Thread(target=sleeper, name="Thread")
    t.start()

    executor.start_polling(dp)
