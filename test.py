import sched
import time

s = sched.scheduler(time.time, time.sleep)
def print_time():
    print(time.time())

def print_some_time():
    s.enter(5,1,print_time)
    s.run()

print_some_time()

<<<<<<< HEAD

def sum(a,b):
    print (a+b)

def print_in_time():
    s.enter(2,1,sum,argument=(7,2))
    s.enter(2,0,sum,argument=(2,2))
    s.run()


print_in_time()
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
=======
def print_mult(n1, n2):
    print(n1 * n2)

def print_fin():
    print("Fin")

def print_sched():
    s.enter(2, 1, print_mult, argument=(3,1,))
    s.enter(4, 2, print_mult, argument=(4,2,))
    s.enter(7, 3, print_fin)
    s.run()


print_sched()

>>>>>>> fabrizio
