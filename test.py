import sched
import time

s = sched.scheduler(time.time, time.sleep)
def print_time():
    print(time.time())

def print_some_time():
    s.enter(5,1,print_time)
    s.run()

print_some_time()