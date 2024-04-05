#Напишите программу, в которой несколько асинхронных задач выполняются параллельно. 
#Включите обработку возможных ошибок в каждой задаче.
import asyncio
import random

async def task(n):
    print(f'Выполняю {n} задачу.')
    await asyncio.sleep(3)
    mes  = input('Введите слово: ')
    print('Слово наоборот: ', mes[::-1])
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