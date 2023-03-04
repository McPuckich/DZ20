# f = open("1.txt", 'w')
# f.write()
# f.close()

import os
import os.path


read_file1 = '1.txt'
read_file2 = '2.txt'
write_file = '3.txt'

with open(read_file1, 'r') as fr, open(read_file2, 'r') as fw, open(write_file, 'w') as f:
    l1 = fr.readlines()
    l2 = fw.readlines()
    print(l1)
    print(l2)
    l3 = l1 + l2
##    for i in l3:
##        f.write(i)
    f.writelines(l1 + l2)


# r_text = ''.join(my_file.readlines()).split('\n')