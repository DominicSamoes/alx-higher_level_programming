#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
st = int(repr(number)[-1])
state = ""
if (st > 5):
    state = "and is greater than 5"
elif (st == 0):
    state = "and is 0"
elif (st < 6):
    state = "and is less than 6 and not 0"
print("Last digit of", number, "is", st, state)
