#Создайте асинхронный счетчик, который можно
# увеличивать и уменьшать из разных задач параллельно. Обеспечьте синхронный доступ к счетчику.
import asyncio

class AsyncCounter:
    def __init__(self):
        self.n = 0

    async def increment(self, val):
            await asyncio.sleep(0.1)  
            self.n += int(val)

    async def decrement(self, val):
            await asyncio.sleep(0.1) 
            self.n -= int(val)

    async def get_value(self):
        return self.n


async def main():
    counter = AsyncCounter()

    await asyncio.gather(
        counter.increment(input('Введите число для прибавления:')),
        counter.decrement(input('Введите число для вычитания:'))
        )

    # Выводим итоговое значение счетчика
    print(f"Итоговое значение: {await counter.get_value()}")

# Запускаем асинхронный цикл
asyncio.run(main())