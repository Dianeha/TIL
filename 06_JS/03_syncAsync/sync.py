# Python: Blocking
from time import sleep

def sleep_3s():
    sleep(3)
    print('Wake up!')

print('시작')
sleep_3s()
print('끝')