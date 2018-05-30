import threading


class CmeMess(threading.Thread):
    def run(self):
        for _ in range(10):  # when you wanna loop, but don t care about a variable
            print(threading.currentThread().getName())


x = CmeMess(name="sendMsg")
y = CmeMess(name="ReceiveMsg")
x.start()  # goes to class and search for run function => kicks off the thread
y.start()
