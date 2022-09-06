# Скопировать в папку folder3 все файлы,
# которые есть в папке folder1,
# но которых нет в папке folder2

# Процедурный подход к инкапсуляцми

import os
import shutil


def copy_unigue_files(folder1, folder2, folder3):

    os.system("CHCP 65001")

    # for command in commands:
    #     os.system(command)

    files1 = os.listdir(folder1)
    files2 = os.listdir(folder2)
    unique_files = list(set(files1).difference(set(files2)))
    # print(unique_files)
    for file in unique_files:
        print(file)
        # shutil.copy(f"data/folder1/{file}", f"data/folder3/{file}")
        folder1 = folder1.replace("/", "\\")
        folder3 = folder3.replace("/", "\\")
        command = f'COPY "{folder1}\\{file}"  "{folder3}\\{file}" '
        # print(command)
        os.system(command)


if __name__ == "__main__":
    copy_unigue_files("data/folder1", "data/folder2", "data/folder3")
