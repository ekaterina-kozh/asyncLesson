#Напишите программу с использованием asyncio, которая в течение определенного времени 
#выводит сообщение каждую секунду. Используйте asyncio.sleep для создания таймера.
import asyncio

async def async_timer(message):
    for i in range(10):
        print(message)
        await asyncio.sleep(1)


# Используйте event loop для запуска асинхронной функции
loop = asyncio.new_event_loop()
loop.run_until_complete(async_timer('Hi'))