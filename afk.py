from sys import argv
from datetime import datetime, time
from random import randint, uniform
from time import sleep

import pyautogui

time_args = [17]
if (len(argv) > 1):
    time_args = [int(x) for x in argv[1:]]

STOP_AT = time(*time_args)
print(
    f"Process will automatically stop at {STOP_AT.strftime('%I:%M:%S %p')}")

def human_move():
    width, height = pyautogui.size()
    margin_x = max(10, min(200, width // 6))
    margin_y = max(10, min(200, height // 6))

    min_x = margin_x
    max_x = width - margin_x - 1
    if max_x <= min_x:
        min_x, max_x = 0, width - 1

    min_y = margin_y
    max_y = height - margin_y - 1
    if max_y <= min_y:
        min_y, max_y = 0, height - 1

    target_x = randint(min_x, max_x)
    target_y = randint(min_y, max_y)
    current_x, current_y = pyautogui.position()

    distance = ((target_x - current_x) ** 2 + (target_y - current_y) ** 2) ** 0.5
    base_steps = int(distance / 150) + 2
    steps = max(3, min(8, base_steps + randint(0, 2)))
    jitter_radius = int(min(120, max(15, distance / max(steps, 1))))

    points = []
    for step in range(steps - 1):
        ratio = (step + 1) / steps
        intermediate_x = int(
            current_x
            + (target_x - current_x) * ratio
            + uniform(-jitter_radius, jitter_radius)
        )
        intermediate_y = int(
            current_y
            + (target_y - current_y) * ratio
            + uniform(-jitter_radius, jitter_radius)
        )
        intermediate_x = max(0, min(width - 1, intermediate_x))
        intermediate_y = max(0, min(height - 1, intermediate_y))
        points.append((intermediate_x, intermediate_y))

    points.append((target_x, target_y))

    sleep(uniform(0.1, 0.6))

    for x, y in points:
        duration = uniform(0.15, 0.8)
        pyautogui.moveTo(x, y, duration=duration, tween=pyautogui.easeInOutQuad)
        sleep(uniform(0.05, 0.4))

    if uniform(0, 1) < 0.35:
        micro_x = int(uniform(-8, 8))
        micro_y = int(uniform(-8, 8))
        pyautogui.moveRel(micro_x, micro_y, duration=uniform(0.05, 0.2))
        sleep(uniform(0.05, 0.3))

    sleep(uniform(0.5, 1.8))


try:
    while datetime.now().time() < STOP_AT:
        human_move()
except KeyboardInterrupt:
    print('I am back because of Keyboard Interrupt!')
except pyautogui.FailSafeException:
    print('I am back because of FailSafe!')
