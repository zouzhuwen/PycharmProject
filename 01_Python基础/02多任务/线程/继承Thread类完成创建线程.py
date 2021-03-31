import  threading


class ThreadClass(threading.Thread):
    def run(self):
        print("run...")
        self.dance()
        self.singe()

    def dance(self):
        print("dance...")

    def singe(self):
        print("singe...")

if __name__ == '__main__':
    t = ThreadClass()
    t.start()
