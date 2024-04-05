#Создайте простой асинхронный кэш, который позволяет асинхронно добавлять 
#и получать значения по ключу. Проверьте его работу в параллельных задачах.
import asyncio 

class Cache:
    def __init__(self):
        self.cache = {}

    async def getCash(self, key):
        await asyncio.sleep(1) 
        return 'Значение: ' + self.cache.get(key)
    
    async def setCash(self, key, val):
        await asyncio.sleep(1) 
        self.cache[key] = val
        print('Ключ и значение добавлены')


async def main():
    cache = Cache()
    await cache.setCash(1, 'One')
    await cache.setCash(2, 'Two')
    await cache.setCash(3, 'Tree')

    await cache.getCash(2)

if __name__ == '__main__':
    asyncio.run(main())