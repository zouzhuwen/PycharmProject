import  multiprocessing



def download_data(q):
    """下载数据"""
    data = [11,22,33,44]
    for temp in data:
        q.put(temp)
    print("---数据下载完毕---")


def analysis(q):
    """处理数据"""
    result_data = list()
    while True:
        if not q.empty():
            result_data.append(q.get())
        else:
            break
    print(result_data)



def main():
    q = multiprocessing.Queue()
    p1 = multiprocessing.Process(target=download_data,args=(q,))
    p2 = multiprocessing.Process(target=analysis,args=(q,))
    p1.start()
    p2.start()


if __name__ == '__main__':
    main()