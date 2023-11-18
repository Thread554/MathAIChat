from aiogram import types


async def convert_command(message: types.Message):
    sp = message.text.replace("/convert ", "").split()
    number = sp[0]
    current_base = int(sp[1])
    target_base = int(sp[2])

    # Переводим число в десятичную систему счисления
    decimal_number = int(str(number), current_base)

    # Конвертируем десятичное число в целевую систему счисления
    converted_number = ""
    while decimal_number > 0:
        remainder = decimal_number % target_base
        converted_number = str(remainder) + converted_number
        decimal_number = decimal_number // target_base

    await message.answer(f"🔍 Ответ: {converted_number}")