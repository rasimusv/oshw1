#!/usr/bin/python3

# Гарипов Расим Ильнурович 11-901

import os
import random
import sys

N = int(sys.argv[1])

my_pid = os.getpid()

for _ in range(N):
    if my_pid == os.getpid():
        os.fork()
    if my_pid != os.getpid():
        os.execv('child.py', ['[]', str(random.randint(1, 10))])
        break

if my_pid == os.getpid():
    for _ in range(N):
        res = os.wait()
        print(f'Дочерний процесс с PID {res[0]} завершился. Статус завершения {os.WEXITSTATUS(res[1])}')
