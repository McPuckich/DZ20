# f = open("1.txt", 'w')
# f.write("Заменить строку в текстовом файле; \nизменить строку в списке; \nзаписать список в файл; \n")
# f.close()

f = open('2.txt', 'r')
lst = f.readlines()
print(lst)
f.close()
lstrev = []
i = 0
while i < len(lst):
    s = lst[len(lst)-i-1]
    lstrev = lstrev + [s]
    i += 1
f = open('2.txt', 'w')
for j in lstrev:
    f.write(j)
f.close()
