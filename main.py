# C: -*- coding: utf-8 -*-
__author__ = 'Alexander Gladkih'
# __version__ = '0.0.1'
__date__ = '16.07.2023'
__maintainer__ = "Alexander Gladkih"

# C: Главный файл с телеграм ботом


import logging
import asyncio

from AI_Networks.solve_tasks import solve_task
from USERS.user import save_user, ids
from ADMIN.admin import *
from AI_Networks.Convert import convert_command
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from AI_Networks.Solve import solve_command
from AI_Networks.code_generator import code_command
from AI_Networks.chatgpt import generate_response
from mixtures_and_alloys.generator import texts_ as t1
from collaboration.generator import texts_ as t2

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# C: Инициализация бота
bot = Bot(token='6380733806:AAGcuPItVu-QNrEv-IqAMbePxaNUI89mAXY')
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
CHANNEL_ID = "@XOR57"


def check_sub_channel(chat_member):
    print(chat_member['status'])
    if chat_member['status'] != 'left':
        return True
    else:
        return False


@dp.callback_query_handler(lambda query: query.data == "check_subscription")
async def check_subscription_callback(query: types.CallbackQuery):
    chat_member = await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=query.from_user.id)
    if check_sub_channel(chat_member):
        await query.answer("Поздравляем! Воспользуйтесь командой /start")
    else:
        await query.answer("Вы не подписаны на канал.")


# C: Обработка команды /start
@dp.message_handler(Command('start'))
async def start_command(message: types.Message):
    chat_member = await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)
    if check_sub_channel(chat_member):
        await message.answer(
            f'👋 Здравствуй, {message.from_user.first_name}! Этот бот поможет тебе решить задачи из ОГЭ на темы "Сплавы и Растворы" и "Совместная работа" . \n\n✏️ Напиши задачу, которую нужно решить или воспользуйся одной из команд 📜:\n\n'
            f'/solve уравнение - решение уравнения\n'
            f'/convert число текущая_система_счисления нужная_система_счисления - перевод систем счислений\n'
            f'/example - случайная текстовая задача\n')

        if message.from_user.id not in ids and message.from_user.id not in admins:
            ids.append(message.from_user.id)
            save_user(message)
    else:
        subscribe_button = types.InlineKeyboardButton(text="Подписаться", url=f"https://t.me/{CHANNEL_ID[1:]}")
        check_subscription_button = types.InlineKeyboardButton(text="Проверить подписку",
                                                               callback_data="check_subscription")

        markup = types.InlineKeyboardMarkup().add(subscribe_button).add(check_subscription_button)

        await message.answer("Для доступа к функционалу бота, пожалуйста, подпишитесь на канал.", reply_markup=markup)


# C: Обработка команды /clear_users
@dp.message_handler(Command('clear_users'))
async def example(message: types.Message):
    if message.from_user.id not in ids and message.from_user.id not in admins:
        ids.append(message.from_user.id)
        save_user(message)
    await clear_users_command(message)



# C: Обработка команды /example
@dp.message_handler(Command('example'))
async def example(message: types.Message):
    if message.from_user.id not in ids and message.from_user.id not in admins:
        ids.append(message.from_user.id)
        save_user(message)
    task_type = random.randint(0, 1)
    if task_type == 0:
        await message.answer(random.choice(t1))
    else:
        await message.answer(random.choice(t2))


# C: Обработка команды /convert
@dp.message_handler(Command('convert'))
async def convert(message: types.Message):
    if message.from_user.id not in ids and message.from_user.id not in admins:
        ids.append(message.from_user.id)
        save_user(message)
    await convert_command(message)


# C: Обработка команды /solve
@dp.message_handler(Command('solve'))
async def solve(message: types.Message):
    if message.from_user.id not in ids and message.from_user.id not in admins:
        ids.append(message.from_user.id)
        save_user(message)
    await solve_command(message)


# C: Обработка команды /admin
@dp.message_handler(Command('admin'))
async def admin(message: types.Message):
    if message.from_user.id not in ids and message.from_user.id not in admins:
        ids.append(message.from_user.id)
        save_user(message)
    await admin_command(message)


# C: Обработка команды /send_users
@dp.message_handler(Command('send_users'))
async def send_users(message: types.Message):
    if str(message.from_user.id) == admin_id1 or str(message.from_user.id) == admin_id2 or "A280811g" in message.text:
        with open('USERS/users.xlsx', 'rb') as document:
            await message.reply_document(document)


# C: Обработка команды /send
@dp.message_handler(Command('send'))
async def send(message: types.Message):
    if message.from_user.id not in ids and message.from_user.id not in admins:
        ids.append(message.from_user.id)
        save_user(message)
    await send_command(message)


# C: Обработка команды /send_me
@dp.message_handler(Command('send_me'), content_types=types.ContentType.ANY)
async def send_me(message: types.Message):
    if message.from_user.id not in ids and message.from_user.id not in admins:
        ids.append(message.from_user.id)
        save_user(message)
    await send_me_command(message)


# C: Обработка команды /send_random
@dp.message_handler(Command('send_random'))
async def send_random(message: types.Message):
    if message.from_user.id not in ids and message.from_user.id not in admins:
        ids.append(message.from_user.id)
        save_user(message)
    await send_random_command(message)


# C: Обработка команды /send_all
@dp.message_handler(Command('send_all'))
async def send_all(message: types.Message):
    if message.from_user.id not in ids and message.from_user.id not in admins:
        ids.append(message.from_user.id)
        save_user(message)
    await send_all_command(message)


# C: Обработка команды /send_all_random
@dp.message_handler(Command('send_all_random'))
async def send_all_random(message: types.Message):
    if message.from_user.id not in ids and message.from_user.id not in admins:
        ids.append(message.from_user.id)
        save_user(message)
    await send_all_random_command(message)


# C: Обработка команды /get_len
@dp.message_handler(Command('get_len'))
async def get_len(message: types.Message):
    if message.from_user.id not in ids and message.from_user.id not in admins:
        ids.append(message.from_user.id)
        save_user(message)
    await get_len_command(message)


# C: Обработка, решение и отправка решения задачи
@dp.message_handler()
async def process_expression(message: types.Message, state: FSMContext):
    if message.from_user.id not in ids and message.from_user.id not in admins:
        ids.append(message.from_user.id)
        save_user(message)

    await solve_task(message)


# C: Главная функция main для вызова остальных функций
async def main():
    # Start the bot
    await dp.start_polling()
    logger.info('🤖 Бот запущен')

    # C: Запуск бота и его остановка если нажать Ctrl+C
    await dp.wait_closed()


if __name__ == '__main__':
    # C: Асинхронный запуск функции main
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
