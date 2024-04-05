#Напишите программу, где одна асинхронная задача запускает другие 
#асинхронные задачи и ожидает их завершения. Проверьте, что задачи выполняются параллельно.
import asyncio
import random

async def getChar(n):
    print('Генерация символа:')
    await asyncio.sleep(0.5)
    print('Окночание генерации символа')
    return chr(n)

async def genPas():
    print('Сгенерируем 8 значный пароль')
    tasks = []
    for _ in range(8):
        task = asyncio.create_task(getChar(random.randint(64,122)))
        tasks.append(task)
    results = await asyncio.gather(*tasks)
    print('Окончание генерации')
    return results

async def main():
    results = await genPas()
    print(f"Результат: {''.join(results)}")

asyncio.run(main())