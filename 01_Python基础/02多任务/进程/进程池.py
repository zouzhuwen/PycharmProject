from multiprocessing import Pool
import time,os,random


def work(num):
    start_time = time.time()
    print("开始执行进程号为{}".format(os.getpid()))
    time.sleep(random.random()*2)
    stop_time = time.time()
    print(num,"执行完毕,耗时{}".format(round(stop_time-start_time,2)))




if __name__ == '__main__':
    # print(time.time())
    # print(os.getpid())
    p = Pool(3)
    for i in range(10):
        p.apply_async(work,(i,))

    print("---start---")
    p.close()#  关闭进程池，关闭后po不再接手新的请求
    p.join() #  等待po中所有子进程执行完成，必须放到close语句之后
    print("---end---")


