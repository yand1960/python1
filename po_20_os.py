# Скопировать в папку folder3 все файлы,
# которые есть в папке folder1,
# но которых нет в папке folder2
# Скриптовый подход к инкапсуляция

import os
import shutil

# ----------------- ввести пути к пакам -----------------
FOLDER1 = "data/folder1"
FOLDER2 = "data/folder2"
FOLDER3 = "data/folder3"
# ---------------------------------------------------------------

# commands = ["dir", "notepad"]
os.system("CHCP 65001")

# for command in commands:
#     os.system(command)

files1 = os.listdir(FOLDER1)
files2 = os.listdir(FOLDER2)
unique_files = list(set(files1).difference(set(files2)))
# print(unique_files)
for file in unique_files:
    print(file)
    # shutil.copy(f"data/folder1/{file}", f"data/folder3/{file}")
    folder1 = FOLDER1.replace("/", "\\")
    folder3 = FOLDER3.replace("/", "\\")
    command = f'COPY "{folder1}\\{file}"  "{folder3}\\{file}" '
    # print(command)
    os.system(command)


