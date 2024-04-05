#Напишите программу, которая асинхронно ищет файлы определенного типа в указанном каталоге. Обработайте результаты поиска.
import asyncio 
import os

async def find_files(directory, extension):
    txt_files = []

    for file in os.listdir(directory):
        if file.endswith(extension):
            txt_files.append(file)

    return txt_files


async def main():
    directory = input("Введите путь к каталогу: ")
    if os.path.isdir(directory) == False:
        print('Такого адреса не существует')
    extension = input("Введите расширение файлов: ")
    files_found = await find_files(directory, extension)
    
    if files_found:        
        for file_path in files_found:
            print(file_path)
    else:
        print(f"Файлы не найдены.")

if __name__ == '__main__':
    asyncio.run(main())