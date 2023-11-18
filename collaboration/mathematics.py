# C: Файл для подстановки данных из задачи под нужную формулу

from collaboration.classifier import get_answer
from sympy import symbols, Eq, solve
import re
from fractions import Fraction

# C: Функция для решения задач
# C: string - уравнение для решения задачи
def math_pr(task, task_type):
    if task_type == 0:
        result = re.findall(r'\d+', task)
        string = '❗ Уравнения соединены между собой знаком системы ❗\n\n'
        string += '{' + f'1 / x + 1 / y = 1 / {result[0]}\n'
        string += '{' + f'{result[1]} / x + {result[2]} / y = {" / ".join(str(Fraction(int(result[3])/100).limit_denominator()).split("/"))}\n\n'
        x, y = symbols('x y')
        equation1 = Eq(1/x + 1/y, 1/int(result[0]))
        equation2 = Eq(int(result[1])/x + int(result[2])/y, int(result[3])/100)
        solution = solve((equation1, equation2), (x, y))[0]
        X = solution[0]
        Y = solution[1]
        string += '{' + f'x = {"%.2f" % round(X, 2)}\n'
        string += '{' + f'y = {"%.2f" % round(Y, 2)}\n\n'

        return string, f"первый оператор за {'%.2f' % round(X, 2)}ч, второй оператор за {'%.2f' % round(Y, 2)}ч."

    elif task_type == 1 or task_type == 2:
        result = list(map(int, re.findall(r'\d+', task)))
        l1 = 9 - int(len(str(result[0])) * 1.7) + 1
        l2 = 10 - int(len(str(result[2])) * 1.7) + 1
        string = "\n" + f"{' ' * (l1//2)}{result[0]}{' ' * (l1//2)}   {' ' * ((l2 - 4)//2)}{result[2]}{' ' * ((l2)//2)}\n"
        string += f"{'-' * 9} - {'-' * 9} = {result[1]}\n"
        string += f"{' ' * (8//2)}x{' ' * (8//2)}   {' ' * (3//2)}x + {result[3]}{' ' * (3//2)}\n\n"
        string += f"ОДЗ:\nx != 0\nx != {result[3]}\n\n"
        x = symbols('x')
        result = Eq(result[0] / x - result[2]/(x+result[3]), result[1])
        result2 = sorted(solve(result, x))
        string += f"x1 = {eval(str(result2[0]))}\n"
        string += f"x2 = {eval(str(result2[1]))}\n\n"
        string += f"x = {result2[-1]}"

        if "литров" in task:
            return string, str("%.2f" % round(result2[-1], 2)) + ' л.'
        else:
            return string, str("%.2f" % round(result2[-1], 2)) + ' д.'

    elif task_type == 3:
        result = list(map(int, re.findall(r'\d+', task)))
        l1 = 9 - int(len(str(result[0])) * 1.7) + 1
        l2 = 10 - int(len(str(result[1])) * 1.7) + 1
        res = result[2] / 60
        string = "\n" + f"{' ' * (8 // 2)}x{' ' * (8 // 2)}   {' ' * (8 // 2)}x{' ' * (8 // 2)}\n"
        string += f"{'-' * 9} - {'-' * 9} = {res}\n"
        string += f"{' ' * (l1 // 2)}{result[0]}{' ' * (l1 // 2)}   {' ' * ((l2 - 4) // 2)}{result[1]}{' ' * (l2 // 2)}\n\n"
        x = symbols('x')
        result = Eq(x/result[0] - x/result[1], res)
        result2 = solve(result, x)[0]
        string += f"x = {'%.2f' % round(result2, 2)}"
        return string, f"Тест содержит {'%.2f' % round(result2, 2)} вопр."

    elif task_type == 4:
        result = list(map(int, re.findall(r'\d+', task)))
        l1 = 9 - int(len(str(result[-1])) * 1.7) + 1
        l2 = 10 - int(len(str(result[-3])) * 1.7) + 1
        string = f"\n{' ' * (l1 // 2)}{result[-1]}{' ' * (l1 // 2)}   {' ' * ((l2 - 4) // 2)}{result[-3]}{' ' * (l2 // 2)}\n"
        string += f"{'-' * 9} - {'-' * 9} = {result[-2]}\n"
        string += f"{' ' * (3 // 2)}x - {result[0]}{' ' * (3 // 2)}   {' ' * (6 // 2)}x{' ' * (8 // 2)}\n\n"
        string += f"ОДЗ:\nx != 0\nx != {result[0]}\n\n"
        x = symbols('x')
        result = Eq(result[-1]/(x-result[0]) - result[-3]/x, result[-2])
        result2 = sorted(solve(result, x))
        string += f"x1 = {'%.2f' % round(result2[0], 2)}\n"
        string += f"x2 = {'%.2f' % round(result2[1], 2)}"
        return string, f"{'%.2f' % round(result2[1], 2)} л."

    elif task_type == 5:
        result = list(map(int, re.findall(r'\d+', task)))
        if len(result) == 3:
            f = result[-3] * 60 + result[-2]
            s = result[-1] * 60
            th = int(1 / eval(f"(1/{f}) - (1/{s})"))
            string = f"\n1/{f} - 1/{s} = 1/{th}"
            res = th / 60
            return string, res
        else:
            f = result[-2]
            s = result[-1] * 60
            th = int(1 / eval(f"(1/{f}) - (1/{s})"))
            string = f"\n1/{f} - 1/{s} = 1/{th}"
            res = th / 60
            return string, res

    elif task_type == 6:
        pass

    elif task_type == 7:
        result = list(map(int, re.findall(r"\d+", task)))
        string = f"\n1/{result[0]} + 1/{result[1]} + 1/{result[2]} = {Fraction(eval('(1/18) + (1/20) + (1/30)')).limit_denominator()}"
        sp = list(map(int, str(Fraction(eval("(1/18) + (1/20) + (1/30)")).limit_denominator()).split('/')))
        res = (sp[1]/sp[0]) * 120
        return string, res

    elif task_type == 8:
        result = list(map(int, re.findall(r"\d+", task)))
        string = f"\nx + x/{result[1]} + x + {result[2]} = {result[0]}\n"
        x = symbols('x')
        result2 = Eq(x + x/result[1] + x + result[2], result[0])
        result2 = solve(result2, x)[0]
        string += f"x = {result2}\n\n"
        result3 = result2 / result[1]
        string += f"{result2} / {result[1]} = {result3}\n"
        result4 = result[0] - result3 - result2
        string += f"{result[0]} - {result3} - {result2} = {result4}\n"
        res = result4 - result3
        string += f"{result4} - {result3} = {res}"
        return string, res

    elif task_type == 9:
        result = list(map(int, re.findall(r'\d+', task)))
        l1 = 9 - int(len(str(result[-2])) * 1.7) + 1
        l2 = 10 - int(len(str(result[-2])) * 1.7) + 1
        string = f"\n{' ' * (l1 // 2)}{result[-2]}{' ' * (l1 // 2)}   {' ' * ((l2-4) // 2)}{result[-2]}{' ' * (l2 // 2)}\n"
        string += f"{'-' * 9} - {'-' * 9} = {result[-1]}\n"
        string += f"{' ' * (8 // 2)}x{' ' * (8 // 2)}   {' ' * (4 // 2)}x - {result[0]}{' ' * (3 // 2)}\n\n"
        string += f"ОДЗ:\nx != 0\nx != {result[0]}\n\n"
        x = symbols('x')
        result = Eq(result[-2]/x - result[-2]/(x+result[0]), result[-1])
        result2 = sorted(solve(result, x))
        string += f"x1 = {'%.2f' % round(result2[0], 2)}\n"
        string += f"x2 = {'%.2f' % round(result2[1], 2)}"
        return string, f"{'%.2f' % round(result2[1], 2)} л."






# C: Функция для подготовки данных. Объединяет в себе
# C: Чистку, классификацию и решение задачи
def calculate(task):
    task_type = get_answer(task)
    print(task_type)
    return math_pr(task, task_type)



