import threading
import multiprocessing
import queue

def producer(q):
    for i in range(1, 6):
        q.put(i)
        print("Produced:", i)

def consumer(q):
    for i in range(5):
        print("Consumed:", q.get())

if __name__ == "__main__":

    # Threading
    q = queue.Queue()
    lock = threading.Lock()

    t1 = threading.Thread(target=producer, args=(q,))
    t2 = threading.Thread(target=consumer, args=(q,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Threading completed")

    # Multiprocessing
    q = multiprocessing.Queue()

    p1 = multiprocessing.Process(target=producer, args=(q,))
    p2 = multiprocessing.Process(target=consumer, args=(q,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Multiprocessing completed")