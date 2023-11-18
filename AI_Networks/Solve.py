import requests
from LxmlSoup import LxmlSoup
from aiogram import types


def run_solve(eq):
    response = requests.get(f'https://mathsolver.microsoft.com/ru/solve-problem/{eq}').text
    soup = LxmlSoup(response)
    answers = soup.find('div', class_='Answer_resultsAnswer__alKN5').text()
    return answers


async def solve_command(message: types.Message):
    eq = message.text.replace("/solve ", "")
    try:
        await message.answer(f"🔍 Ответ: \n\n {run_solve(eq)}")
    except Exception as e:
        await message.answer(f'❌ Ошибка: {e}')