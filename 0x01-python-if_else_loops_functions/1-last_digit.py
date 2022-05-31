#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lstdgt = int(repr(number)[-1])
state = ""
if (lstdgt > 5 and number > 0):
    state = "and is greater than 5"
elif (lstdgt == 0 and number >= 0):
    state = "and is 0"
elif (lstdgt < 6 and number > 0):
    state = "and is less than 6 and not 0"
else:
    lstdgt = -lstdgt
    state = "and is less than 6 and not 0"
print("Last digit of {} is {} {}".format(number, lstdgt, state))
