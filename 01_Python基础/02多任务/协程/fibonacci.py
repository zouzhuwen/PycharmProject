



def create_num(all_num):
    a = 0
    b = 1
    currnet = 0
    while True:
        if currnet <= all_num:
            yield  a
            a ,b = b ,a+b
            currnet += 1

if __name__ == '__main__':
    obj = create_num(10)
    for i in  obj:
        print(i)