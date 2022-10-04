import time
from threading import Thread, Lock

lock = Lock()
results = []

def measure(n):
    time.sleep(3)
    result = 10 * n # Симуляция измерения
    return n, result


def measure_wrapper(n):
    result = measure(n)
    # Этот код гарантирует, что в данный блок кода не зайдет одновременно более 1 потока
    lock.acquire()
    # print(n, result[1])
    results.append(result)
    lock.release()


# Синхронный код хорош, пока задержка невелика
# for n in range (1, 10):
#     result = measure(n)
#     print(result)

pool = []
for n in range(1, 10):
    # thread = Thread(target=measure, args=(n,))
    thread = Thread(target=measure_wrapper, args=(n,))
    pool.append(thread)
    thread.start()

# time.sleep(3.5)
# counter = 0
# while counter < 9:
#     lock.acquire()
#     counter = len(results)
#     lock.release()
#     time.sleep(0.1)

for thread in pool:
    thread.join(timeout=10)
    if thread.is_alive():
        raise TimeoutError

results.sort()
print(results)

