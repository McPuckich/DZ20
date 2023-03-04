# f = open("1.txt", 'w')
# f.write("Заменить строку в текстовом файле; \nизменить строку в списке; \nзаписать список в файл;")
# f.close()

pos1 = int(input("Введите номер первой строки для замены: ")) - 1
pos2 = int(input("Введите номер второй строки для замены: ")) - 1
if pos1 != pos2:
    f = open('1.txt', 'r')
    lst = f.readlines()
    print(lst)
    f.close()
    lst[pos1], lst[pos2] = lst[pos2], lst[pos1]
    f = open('1.txt', 'w')
    for i in lst:
        f.write(i)
    f.close()
else:
    print("Введите отличные друг от друга строки")