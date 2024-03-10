import os

files = ['1.txt', '2.txt', '3.txt']

def get_lines_count(filename):
    with open(filename, 'r', encoding = 'utf-8') as file:
        return sum(1 for line in file)

files = sorted(files, key=lambda x: get_lines_count(x))

with open('result.txt', 'w', encoding = 'utf-8') as result_file:
    for file_name in files:
        lines_count = get_lines_count(file_name)
        result_file.write(f'{file_name}\n{lines_count}\n')
        with open(file_name, 'r', encoding = 'utf-8') as file:
            result_file.write(file.read())
        result_file.write('\n')

print("Файл успешно создан: result.txt")