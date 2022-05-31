#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lstdgt = int(repr(number)[-1])
if number < 0:
   lstdgt = -lstdgt
print("Last digit of {} is {} and is ".format(number, lstdgt), end="")
if lstdgt > 5:
    print("greater than 5")
elif lstdgt == 0:
    print("0")
else:
    print("less than 6 and not 0")
