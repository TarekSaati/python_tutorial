import time
from multiprocessing import Pool

def square(x):
    square = x * x
    print("working..")
    time.sleep(1)
    return square

if __name__ == "__main__":
    pool = Pool(processes=8)
    result = pool.map_async(square, range(0, 5))
    print("using map async to pass multiple tasks")
    print(result.get())
    print("end map async")

    futs=[]
    print("using apply async to pass tasks one-by-one")
    for x in range(5):
        f = pool.apply_async(square, args=(x,))
        futs.append(f)
        time.sleep(0.1)
        
    for f in futs:
        print(f.get())
    pool.close()
    pool.join()
    print("end main script")
