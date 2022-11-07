import sched
import time

s = sched.scheduler(time.time, time.sleep)

def print_time_no_args():
    print("Time: ", time.time())

def print_name_with_delay(name, delay=0):
    s.enter(delay, 1, print, argument=(name,))
    s.enter(delay, 2, print_time_no_args)
    s.run()

def division_with_delay(a, b, delay=0):
    try:
        s.enter(delay, 1, print, argument=(a / b,))
    except ZeroDivisionError:
        s.enter(delay, 1, print, argument=("Can't divide by zero",))
    s.run()

print_name_with_delay("Martin", 5)
division_with_delay(10, 0, 5)