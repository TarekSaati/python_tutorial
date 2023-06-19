from multiprocessing import Pool, Queue
import time
import cv2

# intialize global variables for the pool processes:
def init_pool(d_b):
    global detection_buffer
    detection_buffer = d_b


def detect_object(frame):
    if not detection_buffer.full():
        detection_buffer.put(frame)
        
def show(): 
    while True:          
        if not detection_buffer.empty():
            print('show')
            frame = detection_buffer.get()
            quit = cv2.waitKey(1) & 0xFF == ord('q')
            if (frame is None) or quit:
                cv2.destroyAllWindows()
                break
            cv2.imshow("Video", frame)
    

if __name__ == '__main__':
    detection_buffer = Queue()
    pool = Pool(4, initializer=init_pool, initargs=(detection_buffer,))
    
    cap = cv2.VideoCapture(0)
    # wait for the cap object to be ready
    while not cap.read():
        pass
        
    futures, count = [], 0
    show_future = pool.apply_async(show)

    while count < 200:
        ret, frame = cap.read()
        if ret:
            f = pool.apply_async(detect_object, args=(frame,))
            futures.append(f)
            count+=1
        else:
            break
        

    for f in futures:
        f.get()

    detection_buffer.put(None)
    show_future.get()
    pool.close()
    pool.join()
    print('Program Ended')