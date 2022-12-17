import threading
import concurrent.futures
from time import sleep, perf_counter


def intensive_function(n=1):
    print("I am sleeping ...")
    sleep(n)
    # print("Done")
    return "Done"


# t1 = threading.Thread(target=intensive_function, args=(5,))
# t2 = threading.Thread(target=intensive_function, args=(5,))


start = perf_counter()
# t1.start()
# t2.start()

# t1.join()
# t2.join()
# *****************************************************************************************
# threaded_tasks = []

# for _ in range(5):
#     t = threading.Thread(target=intensive_function, args=(5,))

#     t.start()
#     threaded_tasks.append(t)

# for thread in threaded_tasks:
#     thread.join()

with concurrent.futures.ThreadPoolExecutor() as executor:
    # threads = []
    # for _ in range(5):
    #     threads.append(executor.submit(intensive_function, _ + 1))
    # for r in concurrent.futures.as_completed(threads):
    #     print(r.result())
    r = executor.map(intensive_function, [1]*5)
    print(list(r))


print(f"Total time taken \u0394:", round(perf_counter() - start, 3))
