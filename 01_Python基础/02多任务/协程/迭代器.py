

class Fibonacci():
    def __init__(self):
        self.list =  list()
        self.list.append(1)
        self.list.append(2)
        self.list.append(3)
        self.current = 0


    def __iter__(self):
        return  self

    def __next__(self):
        if self.current < len(self.list):
            result = self.list[self.current]
            self.current += 1
            return result
        else:
            raise StopIteration

def main():
    f = Fibonacci()
    for l in f:
        print(l)

if __name__ == '__main__':
    main()