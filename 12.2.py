#Создайте программу, где пользователь может вводить асинхронные математические операции (например, сложение, умножение)
# в интерактивном режиме. Реализуйте асинхронную обработку ввода.
import asyncio

def calculate(num1, num2, op):
    num1, num2 = float(num1), float(num2)
    match op:
        case '+':
            return num1 + num2
        case '-':
            return num1 - num2
        case '*':
            return num1 * num2
        case '/':
            try:
                return num1 / num2
            except ZeroDivisionError:
                return "Нельзя делить на 0"
        case _:
            return "Выберите операцию [+-*/]."

async def main():
    while True:
        val1 = await asyncio.to_thread(input, "Введите первое число: ")
        val2 = await asyncio.to_thread(input, "Введите второе число: ")
        val3 = await asyncio.to_thread(input, "Введите оператор [+-*/]: ")
        if val1 == '' or val2 == '' or val3 == '':
            print("Программа завершена.")
            break
        result = calculate(val1, val2, val3)
        print(f"Результат: {result}")

if __name__ == '__main__':
    asyncio.run(main())