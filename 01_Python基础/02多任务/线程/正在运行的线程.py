import threading
from time import sleep

def dance():
    for i in range(5):
        sleep(1)
        print("dance...%d次"%i)


def sing():
    for i in range(5):
        sleep(1)
        print("sing...%d次"%i)


def main():
    t1 = threading.Thread(target=dance)
    t2 = threading.Thread(target=sing)

    t1.start()
    t2.start()

    t = threading.enumerate()
    for i in t:
        print(i)


if __name__ == '__main__':
    main()
