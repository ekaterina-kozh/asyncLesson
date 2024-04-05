#Реализуйте асинхронный генератор, который асинхронно возвращает случайные числа. 
#Запустите несколько задач для генерации чисел параллельно.
import asyncio
import random

async def task(n):
    print(f'Выполняю {n} задачу.')
    await asyncio.sleep(3)
    print('Случайное число: ', random.randint(1,27))
    print(f'Окнончание работы {n} задачи')
    return task

async def main():
    first_delay = asyncio.create_task(task(1))
    second_delay = asyncio.create_task(task(2))
    third_delay = asyncio.create_task(task(3))

    try:
        await first_delay
        await second_delay
        await third_delay
    except Exception as e:
        print('Ошибка: ', e)

# Запускаем цикл событий
asyncio.run(main())