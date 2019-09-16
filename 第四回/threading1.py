from threading import Thread
import time

boolean = False
x = 1

def Double():
    global boolean
    global x
    while True:
        time.sleep(0.5)
        if boolean:
            break
        x = 2*x
        

class Test(Thread):
    def __init__(self):
        t1=Thread(target=Double)
        t2=Thread(target=self.run)
        t1.start()
        time.sleep(0.25)
        t2.start()

    def run(self):
        global boolean
        while True:
            if x>100:
                boolean=True
                break
            time.sleep(0.5)
        print(x)

loop = Test()
loop.start()
Double()
print(x)