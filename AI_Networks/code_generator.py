import requests
from aiogram import types


def filter_and_print(data):
    sp = []
    lines = data.split("zzznewlinezzz")
    for line in lines:
        try:
            if line.startswith("data:"):
                continue
            elif line.startswith("zzzmessageidzzz:"):
                continue
            elif line.startswith("zzz_completed_zzz"):
                continue
            else:
                line = line.strip("zzz").strip("#").strip("`").strip()
                sp.append(line)
        except:
            continue

    return "\n".join(sp)


def generate(prompt, lang):
    cookies = {
        '_ga_KVXDJ93SHK': 'GS1.1.1692288363.1.1.1692288376.0.0.0',
        '_ga': 'GA1.1.297906271.1692288363',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/116.0',
        'Accept': '*/*',
        'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'Referer': 'https://zzzcode.ai/code-generator',
        'Content-Type': 'application/json',
        'Origin': 'https://zzzcode.ai',
        'Alt-Used': 'zzzcode.ai',
        'Connection': 'keep-alive',
        # 'Cookie': '_ga_KVXDJ93SHK=GS1.1.1692288363.1.1.1692288376.0.0.0; _ga=GA1.1.297906271.1692288363',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
    }

    json_data = {
        'p1': f"{lang}",
        'p2': f"{prompt}",
        'p3': 'none',
        'p4': 'none',
        'p5': 'none',
        'option1': '2 - Generate code',
        'option2': 'Professional',
        'option3': 'Russian',
    }

    response = requests.post('https://zzzcode.ai/api/my/code-generator', cookies=cookies, headers=headers,
                             json=json_data).text.encode().decode('unicode-escape')
    result = filter_and_print(response).replace('data: "zzz_completed_zzz"', "")
    print(result)
    return result



async def code_command(message: types.Message):
    msg = await message.answer("🧑‍💻 Начинаем генерацию кода...")
    sp = message.text.replace("/code ", "").split()
    await msg.edit_text(f"🧑‍💻 Ваш код успешно сгенерирован:\n\n{generate(' '.join(sp[1:]), sp[0])}")
