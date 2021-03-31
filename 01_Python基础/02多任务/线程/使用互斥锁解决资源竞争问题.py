import time
import threading

g_num = 0
mutex = threading.Lock() #创建互斥锁
def test1(num):
    global g_num
    # 上锁，如果之前没有被上锁，那么上锁成功
    # 如果上锁之前，已经被上锁，那么此时会堵塞，直到这个锁被解开为止
    for i in range(num):
        mutex.acquire()
        g_num += 1
        # 解锁
        mutex.release()
    print("...in test1 g_num=%d..." %g_num)


def test2(num):
    global g_num
    for i in range(num):
        mutex.acquire()
        g_num += 1
        mutex.release()
    print("...in test2 g_num=%d..." % g_num)


def main():
    t1 = threading.Thread(target=test1,args=(1000000,))
    t2 = threading.Thread(target=test2,args=(1000000,))
    t1.start()
    t2.start()

    time.sleep(2)
    print(print("...in main g_num=%d..." %g_num))

if __name__ == '__main__':
    main()