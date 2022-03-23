import threading
import time

pos_int = int(input('Enter a positive integer: '))


def print_foo(n):
    for _ in range(n):
        print('foo', end='')
        time.sleep(1)


def print_bar(n):
    for _ in range(n):
        print('bar', end='')
        time.sleep(1)


thread1 = threading.Thread(target=print_foo, args=(pos_int, ))
thread2 = threading.Thread(target=print_bar, args=(pos_int, ))

thread1.start()
thread2.start()
