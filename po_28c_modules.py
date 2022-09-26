# Импорт по абсолютному пути

# 1. Задать переменную окружения PYTHONPATH на уровне OC - не делаем

# 2. Задать переменную окружения PYTHONPATH программно
# Весьма неудобно для разработчика (среда ругается, подсказка не высплывает и т.д.)
# import sys
# sys.path.append("C:\\tmp")
#
# from module01.module013  import foo123

# 2. Задать переменную окружения PYTHONPATH в среде разработки
# на уровне проекта:
# File -> Settings -> Python Interpreter -> cog -> Show All -> Пятая кнопка -> +
from module01.module013  import foo123

print(foo123)
