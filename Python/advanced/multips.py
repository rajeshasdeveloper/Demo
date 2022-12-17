import time


def intensive_func(arr=[1, 2, 3, 4, 5]):
    for i in arr:
        time.sleep(10)
        print(i)


import threading

t1 = threading.Thread(target=intensive_func)
t2 = threading.Thread(target=intensive_func)

start = time.perf_counter()

t1.start()
t2.start()

t1.join()
t2.join()
# intensive_func()
# intensive_func()

print("time taken", round(time.perf_counter() - start, 3))
