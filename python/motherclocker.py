import time;
from threading import Thread
# MULTI THREAD CLOCK SIGNAL GENERATOR
"""
This file enables a multi thread clock signal generator
good for raspberry pi clock simulation

many threads with 1 pin control for oscillating it, good idea
for circuit test
"""
def clock1():
    while(True):
        print("ping 1 sec")
        time.sleep(1)

def clock2():
    while(True):
        print("pong 1/8 sec")
        time.sleep(.125)

"""

The thread configuration feature: daemon, has the function to keep the thread execution in the background and not to overlap with the
main executing thread.

as a result, the main thread has to have a circle feature (while(true) lanes in the main execution part of the program) with a sleep time
to avoid consumption of the cpu bandwidth, this will allow you to break execution with keyboard interruption (tipically ctrl-c)


"""

def main():
    # string.format helps y,ou to place variables in the message
    t1 = Thread(target=clock1, args="")
    t1.daemon = True
    t1.start()
    
    t2 = Thread(target=clock2, args="")
    t2.daemon = True
    t2.start()

    while(True):
        time.sleep(60)



if __name__=="__main__":
    main()