from sys import argv
from datetime import datetime, time
from pyautogui import moveTo, FailSafeException
from random import randint

time_args = [17]
if (len(argv) > 1):
    time_args = [int(x) for x in argv[1:]]

STOP_AT = time(*time_args)
print(
    f"Process will automatically stop at {STOP_AT.strftime('%I:%M:%S %p')}")

try:
    while datetime.now().time() < STOP_AT:
        moveTo(randint(50, 1000), randint(50, 1000), duration=1)
except KeyboardInterrupt:
    print('I am back because of Keyboard Interrupt!')
except FailSafeException:
    print('I am back because of FailSafe!')
