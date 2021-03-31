import  threading
import hashlib
def fun(num):
    """打印乘法计算表"""
    for i in range(1,num):
        for j in range(1,num):
            if i>=j:
                print("{}*{}={}\t".format(j,i,i*j),end='')
        print()

def ran():
    for i in range(1,5):
        print(i)


def enume():
    names = ["aa","bb","cc"]
    for name in threading.enumerate():
        print(name)


if __name__ == '__main__':
    str = "戴假发IDahgnadigjdg"
    print(str.encode("utf-8"))
    print(str.hexdigest())
