# Скопировать в папку folder3 все файлы,
# которые есть в папке folder1,
# но которых нет в папке folder2

# Объектный подход к инкапсуляции ("экземлярный" класс)

import os
import shutil


class FileProcessing:

    def __init__(self):
        # Конструктор конфигурирует инфраструктуру, необходимую для работы класса
        os.system("CHCP 65001")

    def copy_unique_files(self, folder1, folder2, folder3):
        files1 = os.listdir(folder1)
        files2 = os.listdir(folder2)
        unique_files = list(set(files1).difference(set(files2)))

        for file in unique_files:
            print(file)
            # shutil.copy(f"data/folder1/{file}", f"data/folder3/{file}")
            folder1 = folder1.replace("/", "\\")
            folder3 = folder3.replace("/", "\\")
            command = f'COPY "{folder1}\\{file}"  "{folder3}\\{file}" '
            os.system(command)


if __name__ == "__main__":
    processor = FileProcessing()
    processor.copy_unique_files("data/folder1", "data/folder2", "data/folder3")
