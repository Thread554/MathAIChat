from aiogram import types
from project_math import calculate


async def solve_task(message: types.Message):
    expression = message.text
    try:
        string, answer = calculate(expression)
        if type(answer) == int:
            if int(answer) < 0:
                await message.answer(f'❌ Ошибка: мы пока не можем решить данную задачу.')
        await message.answer(f'📝 Уравнение: \n{string}')
        await message.answer(f'🔍 Ответ: {answer}')
    except Exception as e:
        await message.answer(f'❌ Ошибка: мы пока не можем решить данную задачу.')
        print(e)
