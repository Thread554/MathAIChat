# C: Файл для подстановки данных из задачи под нужную формулу

from mixtures_and_alloys.classifier import get_answer
from sympy import symbols, Eq, solve
import re
from fractions import Fraction

# C: Функция для решения задач
# C: string - уравнение для решения задачи
def math_pr(task, task_type):
    if task_type == 0:
        result = re.findall(r'\d+', task)
        string = f"\n{int(result[0]) / 100}x + {int(result[1]) / 100}y = {int(result[2]) / 100}(x + y)\n\n"
        x, y = symbols('x y')
        result = Eq(int(result[0])/100*x + int(result[1])/100*y, int(result[2])/100*(x + y))
        result = solve(result, x)
        result = result[0] / y
        result = str(Fraction(str(result)).limit_denominator())
        if '/' not in result:
            result += '/1'

        result1, result2 = int(result.split('/')[0]), int(result.split('/')[1])
        string += f" x      {'%.2f' % round(result1, 2)}\n"
        string += "--- = ---------\n"
        string += f" y      {'%.2f' % round(result2, 2)}"
        return string, '%.2f' % round(result1, 2) + " : " + "%.2f" % round(result2, 2)

    elif task_type == 1 or task_type == 10:
        result = re.findall(r'\d+', task)
        string = f"\n{int(result[0]) / 100}x + {int(result[1]) / 100}x"
        l = round(len(string) * 1.7)
        result = (int(result[0]) + int(result[1])) / 200
        string += '\n' + l * '-' + f' = {result}\n'
        string += '' + (l - 5) // 2 * ' ' + 'x + x' + (l - 5) // 2 * ' '
        return string, str("%.1f" % round(result * 100, 1)) + '%'

    elif task_type == 2:
        result = re.findall(r'\d+', task)
        string = f'\n{int(result[0]) / 100}x + {int(result[1]) / 100}(x + {int(result[2])}) = {int(result[3]) / 100}(2x + {int(result[2])})'
        x = symbols('x')
        k = int(result[2])
        result = Eq(int(result[0]) / 100 * x + int(result[1]) / 100 * (x + int(result[2])), (int(result[3]) / 100) * (2*x + int(result[2])))
        result2 = solve(result, x)[0]
        return string, str("%.2f" % round(result2 * 2 + k, 2)) + 'кг'

    elif task_type == 3 or task_type == 11:
        result = re.findall(r'\d+', task)
        string = '❗ Уравнения соединены между собой знаком системы ❗\n\n'
        string += '{' + f'{result[0]}x + {result[1]}y = ({result[0]} + {result[1]}) * {int(result[2]) / 100}'
        string += '\n{' + f'x + y = 2 * {int(result[3]) / 100}\n\n'
        first = result[0]
        second = result[1]
        x, y = symbols('x y')
        equation1 = Eq(int(result[0])*x + int(result[1])*y, (int(result[0]) + int(result[1])) * (int(result[2]) / 100))
        equation2 = Eq(x + y, 2 * (int(result[3]) / 100))
        solution = solve((equation1, equation2), (x, y))
        X = solution[x]
        Y = solution[y]
        string += '{' + f'x = {"%.2f" % round(X, 2)}\n'
        string += '{' + f'y = {"%.2f" % round(Y, 2)}\n\n'
        if 'кило' in task.split('.')[-1]:
            if 'первом' in task.split('.')[-1]:
                string += f'{first} * x = ?'
                answer = int(first) * X
                return string, str("%.2f" % round(answer, 2)) + 'кг'
            else:
                string += f'{second} * y = ?'
                answer = int(second) * Y
                return string, str("%.2f" % round(answer, 2)) + 'кг'
        elif 'процен' in task.split('.')[-1]:
            if 'первом' in task.split('.')[-1]:
                string += f'{round(X, 2)} * 100 = ? %'
                answer = round(X, 2) * 100
                return string, str("%.2f" % round(answer, 2)) + '%'
            else:
                string += f'{round(Y, 2)} * 100 = ? %'
                answer = round(Y, 2) * 100
                return string, str("%.2f" % round(answer, 2)) + "%"

    elif task_type == 4 or task_type == 7:
        result = re.findall(r'\d+', task)
        F = 100 - int(result[0])
        S = 100 - int(result[1])
        R = "%.2f" % round((S / F) * int(result[2]))
        string = f"\n{S}\n"
        string += f"{'-' * int(len(str(F)) + 2 * 1.7)}  * {result[2]} = {R}кг\n"
        string += f"{F}"
        return string, str(R) + 'кг'



    elif task_type == 5:
        result = re.findall(r'\d+', task)
        F = 100 - int(result[0])
        S = 100 - int(result[1])
        K = (F / 100) * int(result[2])
        string = f"\n100% - {result[0]}% = {F}%\n"
        string += f"100% - {result[0]}% = {S}%\n\n"
        string += f"{F / 100} * {result[2]} = {K}кг\n\n"
        if len(str(S)) > len(str(K)):
            l = int(len(str(S)) * 1.7)
        else:
            l = int(len(str(K)) * 1.7)

        R = K / (S / 100)
        string += f"{K}\n"
        string += f"{'-' * l + 1} = {R}кг\n"
        string += f"{S / 100}"

        answer = str(R) + 'кг'
        return string, answer

    elif task_type == 6:
        result = re.findall(r'\d+', task)
        string = '❗ Уравнения соединены между собой знаком системы ❗\n\n'
        string += '{' + f'{int(result[0]) / 100}x + {int(result[1]) / 100}y = {int(result[3]) / 100}(x + y + {result[2]})'
        string += '\n{' + f'{int(result[0]) / 100}x + {int(result[1]) / 100}y + {int(result[6]) / 100} * {result[5]} = {int(result[7]) / 100}(x + y + {result[2]})\n\n'
        first = result[0]
        second = result[1]
        x, y = symbols('x y')
        equation1 = Eq(int(result[0]) * x + int(result[1]) * y,
                       int(result[3]) * (x + y + int(result[2])))
        equation2 = Eq(int(result[0]) * x + int(result[1]) * y + int(result[6]) * int(result[5]),
                       int(result[7]) * (x + y + int(result[2])))
        solution = solve((equation1, equation2), (x, y))
        X = solution[x]
        Y = solution[y]
        string += '{' + f'x = {"%.2f" % round(X, 2)}\n'
        string += '{' + f'y = {"%.2f" % round(Y, 2)}\n\n'

        if first in task.split('.')[-1]:
            answer = f'{X}кг'
        else:
            answer = f"{Y}кг"

        return string, answer

    elif task_type == 8:
        result = re.findall(r'\d+', task)
        R1 = (int(result[0]) / 100) * int(result[1])
        R2 = int(result[0]) + int(result[2])
        R = R1 / R2 * 100
        string = f"\n({result[0]} / 100) * {result[1]} = {R1}кг\n"
        string += f"{result[0]} + {result[2]} = {R2}\n"
        string += f"({R1} / {R2}) * 100 = {R}%"
        return string, str("%.2f" % round(R, 2)) + '%'

    elif task_type == 9:
        result = re.findall(r'\d+', task)
        string = f"\n{int(result[2])/100}({result[0]} + x) = {int(result[1])/100} * {int(result[0])}"
        x = symbols('x')
        result = Eq((int(result[2])/100)*(int(result[0]) + x), int(result[1])/100 * int(result[0]))
        result2 = solve(result, x)[0] / 1000
        return string, str("%.2f" % round(result2, 2)) + 'кг'

    elif task_type == 12:
        result = list(map(int, re.findall(r'\d+', task)))
        res = result[2]
        string = f'\n{result[0] / 100}x + {result[1] / 100}({result[2]} - x) = {result[3] / 100} * {result[2]}\n'
        x = symbols('x')
        result = Eq((result[0] / 100)*x + (result[1] / 100)*(result[2] - x), result[3] / 100 * result[2])
        result2 = float("%.2f" % round(solve(result, x)[0], 2))
        result2 = res - result2 * 2
        string += f'x = {result2}'

        return string, str(result2) + 'кг'

    elif task_type == 13:
        result = list(map(int, re.findall(r'\d+', task)))
        res = result[2]
        string = f'\n{result[0] / 100}x + {result[1] / 100}({result[2]} - x) = {result[3] / 100} * {result[2]}\n'
        x = symbols('x')
        result = Eq((result[0] / 100) * x + (result[1] / 100) * (result[2] - x), result[3] / 100 * result[2])
        result1 = float("%.2f" % round(solve(result, x)[0], 2))
        result2 = res - result1
        string += f'x = {result1}'

        return string, f'{result1}кг и {result2}кг'


# C: Функция для подготовки данных. Объединяет в себе
# C: Чистку, классификацию и решение задачи
def calculate(task):
    try:
        task = ''.join(task.split('­'))
    except:
        pass
    task_type = get_answer(task)
    print(task_type)
    return math_pr(task, task_type)


