import freeGPT
import googletrans
from aiogram import types


async def generate_response(message: types.Message):
    msg = await message.answer("🤖 Обрабатываю Ваш запрос...")
    sp = message.text.replace("/gpt ", "").split()
    await msg.edit_text(await run(" ".join(sp[1:])))


async def run(prompt):
    try:
        translator = googletrans.Translator(service_urls=['translate.googleapis.com'])
        resp = await getattr(freeGPT, "gpt3").Completion().create(prompt)
        translated_text = translator.translate(resp, src='en', dest='ru').text
        return f"🤖 {translated_text}"
    except Exception as e:
        return f"🤖 {e}"