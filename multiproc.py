from multiprocessing import Pool, Queue
import time
import cv2

# intialize global variables for the pool processes:
def init_pool(d_b):
    global detection_buffer
    detection_buffer = d_b


def detect_object(frame):
    
    time.sleep(0.1)
    if not detection_buffer.full():
        detection_buffer.put(frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        return True
    return False


def show():
    
    while True:
        print('show')
        frame = detection_buffer.get()
        if frame is None:
            break
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        cv2.imshow("Video", frame)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    detection_buffer = Queue(maxsize=10)
    pool = Pool(6, initializer=init_pool, initargs=(detection_buffer,))
    show_future = pool.apply_async(show)
    cap = cv2.VideoCapture(0)
    futures = []
    count = 0
    while count < 100:
        ret, frame = cap.read()
        if ret:
            f = pool.apply_async(detect_object, args=(frame,))
            futures.append(f)
            time.sleep(0.05)
        count+=1

    for f in futures:
        f.get()

    detection_buffer.put(None)
    show_future.get()
    pool.close()
    pool.join()
    cv2.destroyAllWindows()
    print('Program Ended')