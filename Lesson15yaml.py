#
#
#  из джейсона в пайтон обьект в два шага import yaml


import time
import threading

count = 10
count2 = 10


def third_th(th):
    print('before')
    time.sleep(5)
    th.join()
    print('after')

def second_th():
    global count2
    while count2:
        count2 -= 1
        print(f'--- count2: {count2}')
        time.sleep(0.5)
    return 100

th2 = threading.Thread(target=second_th, name='second_tread', daemon=False)
th3 = threading.Thread(target=third_th, args=(th2,), name='third_tread', daemon=False)



th2.start()
th3.start()
# th2.join()

while count:
    count -= 1
    print(f'count: {count}')
    time.sleep(0.3)


print(f"Done: {count2}")
