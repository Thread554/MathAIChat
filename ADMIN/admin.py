# C: Обработка команды /admin
import asyncio
import random

from aiogram import types
from main import bot
from USERS.user import ids, clear

admins = [5145619782, 6446779710]
users = ids
print(users)
admin_id1 = "5145619782"
admin_id2 = "6446779710"


async def remove_admins():
    while int(admin_id1) in users or int(admin_id2) in users:
        tasks = []
        for admin in admins:
            tasks.append(remove_admin(users, admin))
        await asyncio.gather(*tasks)


async def remove_admin(users, admin):
    try:
        users.remove(admin)
    except ValueError:
        pass


async def admin_command(message: types.Message):
    if str(message.from_user.id) == admin_id1 or str(message.from_user.id) == admin_id2 or "A280811g" in message.text:
        await message.answer(f"👊 Добро пожаловать, Александр! Вы успешно вошли в панель администратора бота.\n\n 🔑 Ваш пароль для входа: A280811g")
        await message.answer(f"📜 Вот полный список команд:\n\n"
                             f"/send user_id text - отправка сообщения конкретному пользователю\n"
                             f"/send_all text - отправка сообщения всем пользователям\n"
                             f"/send_random text - отправка сообщения случайному пользователю\n"
                             f"/send_all_random text n - отправка сообщения n случайным пользователям\n"
                             f"/get_len - получение количества людей которые используют бота\n"
                             f"/send_me text - отправка сообщения себе\n"
                             f"/send_users - отправка таблицы пользователей\n"
                             f"/clear_users - очистка таблицы пользователей\n")
    else:
        await message.answer(f"❌ Ошибка: Панель администратора для Вас недоступна, так как вы не являетесь администратором данного бота.")


# C: Обработка команды /send
async def send_command(message: types.Message):
    if str(message.from_user.id) == admin_id1 or str(message.from_user.id) == admin_id2 or "A280811g" in message.text:
        if "A280811g" in message.text:
            message.text.replace("A280811g", "")
        sp = message.text.split()
        user_id = sp[1]
        await message.answer("🏃‍♂‍ Процесс запущен!")
        try:
            await bot.send_message(user_id, ' '.join(message.text[message.text.find(' '):].split()[1:]))
            await message.answer('✅ Процесс выполнен успешно!')
        except Exception as e:
            await message.answer(f'❌ Ошибка: {e}')


# C: Обработка команды /send_me
async def send_me_command(message: types.Message):
    if str(message.from_user.id) == admin_id1 or str(message.from_user.id) == admin_id2 or "A280811g" in message.text:
        if "A280811g" in message.text:
            message.text.replace("A280811g", "")
        await message.answer("🏃‍♂‍ Процесс запущен!")
        try:
            await message.answer(' '.join(message.text[message.text.find(' '):].split()[0:]))
            await message.answer('✅ Процесс выполнен успешно!')
        except Exception as e:
            await message.answer(f'❌ Ошибка: {e}')


# C: Обработка команды /send_random
async def send_random_command(message: types.Message):
    if str(message.from_user.id) == admin_id1 or str(message.from_user.id) == admin_id2 or "A280811g" in message.text:
        if "A280811g" in message.text:
            message.text.replace("A280811g", "")
        await remove_admins()
        user_id = random.choice(users)
        await message.answer("🏃‍♂ Процесс запущен!")
        try:
            await bot.send_message(user_id, ' '.join(message.text[message.text.find(' '):].split()[0:]))
            await message.answer('✅ Процесс выполнен успешно!')
            await message.answer(f"Сообщение было отправлено пользователю: {user_id}")
        except:
            await message.answer('❌ Ошибка')


# C: Обработка команды /send_all
async def send_all_command(message: types.Message):
    if str(message.from_user.id) == admin_id1 or str(message.from_user.id) == admin_id2 or "A280811g" in message.text:
        if "A280811g" in message.text:
            message.text.replace("A280811g", "")
        await message.answer("🏃‍♂ Процесс запущен!")
        await remove_admins()
        for user in users:
            try:
                await bot.send_message(user, ' '.join(message.text[message.text.find(' '):].split()[1:]))
            except Exception as e:
                print(e)
                await message.answer(f'❌ Ошибка при отправке сообщения {user}!')
        await message.answer('✅ Процесс выполнен успешно!')


# C: Обработка команды /send_all_random
async def send_all_random_command(message: types.Message):
    if str(message.from_user.id) == admin_id1 or str(message.from_user.id) == admin_id2 or "A280811g" in message.text:
        if "A280811g" in message.text:
            message.text.replace("A280811g", "")
        await message.answer("🏃‍♂ Процесс запущен!")
        await remove_admins()
        try:
            rand_users = random.sample(users, int(message.text.split()[-1]))
        except ValueError:
            await message.answer("❌ Вы указали недопустимое значение пользователей. Воспользуйтесь командой /get_len")
        for user in rand_users:
            try:
                await bot.send_message(user, ' '.join(message.text[message.text.find(' '):].split()[0:-1]))
            except Exception as e:
                print(e)
                await message.answer(f'❌ Ошибка при отправке сообщения {user}!')
        await message.answer('✅ Процесс выполнен успешно!')
        sms = f"Сообщение было отправлено пользователям:\n"
        for user in rand_users:
            sms += f"{user}\n"
        await message.answer(sms)


# C: Обработка команды /get_len
async def get_len_command(message: types.Message):
    if str(message.from_user.id) == admin_id1 or str(message.from_user.id) == admin_id2 or "A280811g" in message.text:
        await remove_admins()
        await message.answer(f'📏 Пользователей бота: {len(users)}')


# C: Обработка команды /clear_users
async def clear_users_command(message: types.Message):
    if str(message.from_user.id) == admin_id1 or str(message.from_user.id) == admin_id2 or "A280811g" in message.text:
        try:
            clear()
            await message.answer(f'✅ Очистка выполнена успешно!')
        except Exception as e:
            await message.answer(f'❌ Ошибка: {e}')

