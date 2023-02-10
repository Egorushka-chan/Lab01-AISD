"""
Натуральные числа, не превышающие 1 000 000, у которых пятая справа цифра равна 7.
Выводит на экран четные цифры стоящие в числе справа от этой 7 (прописью).
"""
numbers_dictionary = {
    '0': 'ноль',
    '1': 'один',
    '2': 'два',
    '3': 'три',
    '4': 'четыре',
    '5': 'пять',
    '6': 'шесть',
    '7': 'семь',
    '8': 'восемь',
    '9': 'девять'
}

with open("numbers.txt", 'r') as file:
    line = file.readline()
    if line != '':
        while line != '':
            numbers = line.split(' ')

            for number in numbers:

                test_passed = True
                for value in number: #проверка что значение содержит только числа
                    if value not in numbers_dictionary:
                        test_passed = False

                if test_passed: #проверка что число не превышает 1 000 000
                    if int(number) > 1000000:
                        test_passed = False

                if test_passed: #проверка что 5-ое число справа 7
                    length = len(number)
                    if length >= 5:
                        fifth_value = number[-5]
                        if fifth_value != '7':
                            test_passed = False

                if test_passed: #вывод четных чисел
                    selected_values = number[-4:]
                    result_values = []
                    for value in selected_values:
                        if int(value) % 2 == 0:
                            result_values.append(value)

                    result_string = ''
                    for result_value in result_values:
                        result_string += numbers_dictionary[result_value] + " "
                    if result_string != '':
                        print(f"{number}: {result_string}")
            line = file.readline()
    else:
        print('файл пустой')
