import sched
import time

s = sched.scheduler(time.time, time.sleep)


def sum(a,b):
    print (a+b)

def print_in_time():
    s.enter(3,1,sum,argument=(7,2))
    s.run()


print_in_time()