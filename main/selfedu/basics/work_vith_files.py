# --- чтение ---

# f = open('file.txt', 'r', encoding='utf-8')
# text = f.read(2)
# print(f.encoding)  # cp1251
# text2 = f.read(8)
# text = f.read()

# f.close()

# print(text)  # РЎ
# print(text)  # Ст
# print(text2)
# рока 1
# С
# print(text)
# Строка 1
# Строка 2
# Строка 3
#

# --- дозаписать в файл ('a' - append) ---

# f = open('file.txt', 'a', encoding='utf-8')
# f.write('Новая строка\n')
# f.close()

# lines = ['Новая строка 1', 'Новая строка 2']
# f = open('file.txt', 'a', encoding='utf-8')
# for i in lines:
#     f.write(i + '\n')
# f.writelines(lines)
# f.writelines(f'{i}\n' for i in lines)
# f.close()

# --- ещё про чтение файлов ---

f = open('file.txt', 'r', encoding='utf-8')
for line in f:
    # print(line.replace('\n', ''))  # с помощью replace убрали лишние переносы строк
    # или убираем с помощью опции end=''
    print(line, end='')
f.close()










