#!/usr/bin/python3

import os
import time
import random
import sys

s = int(sys.argv[1])
print(f'Запущена программа Child в процессе с PID {os.getpid()} с аргументом {s}')
time.sleep(s)
print(f'Завершился процесс с PID {os.getpid()}')
sys.exit(random.randint(0, 1))
