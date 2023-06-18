import time
from multiprocessing import Pool

def square(x):
    square = x * x
    print("start process")
    time.sleep(1)
    return square


if __name__ == "__main__":
    pool = Pool()
    result = pool.map_async(square, range(0, 5))
    print("main script")
    print(result.get())
    print("end main script")