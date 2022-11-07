import sched
import time

s = sched.scheduler(time.time, time.sleep)

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

