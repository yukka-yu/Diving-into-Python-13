'''Вспоминаем задачу 3 из прошлого семинара. Мы сформировали текстовый файл с псевдо именами и произведением чисел.
Напишите функцию, которая создаёт из созданного ранее файла новый с данными в формате JSON.
Имена пишите с большой буквы.
Каждую пару сохраняйте с новой строки.'''


import json


def text_to_json(file_text: str, file_json: str) -> None:
    try:
        with (
            open(file_text, 'r', encoding = 'utf-8') as ft,
            open(file_json, 'w', encoding = 'utf-8') as fj
                
        ):
            fj.write(ft.read()) 
    except FileNotFoundError as e:
        print('Файл не найден!')
        

if __name__ == '__main__':
    text_to_json('text3.txt', 'text3.json')