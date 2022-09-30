import time
from threading import Thread

def measure(n):
    time.sleep(3)
    result = 10 * n # Симуляция измерения
    print(n, result)
    return n, result

# Синхронный код хорош, пока задержка невелика
# for n in range (1, 10):
#     result = measure(n)
#     print(result)

for n in range(1, 10):
    thread = Thread(target=measure, args=(n,))
    thread.start()

