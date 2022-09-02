# Скопировать в папку folder3 все файлы,
# которые есть в папке folder1,
# но которых нет в папке folder2

import os
commands = ["dir", "notepad"]

os.system("CHCP 65001")

# for command in commands:
#     os.system(command)

files1 = os.listdir("data/folder1")
files2 = os.listdir("data/folder2")
unique_files = list(set(files1).difference(set(files2)))
# print(unique_files)
for file in unique_files:
    print(file)
