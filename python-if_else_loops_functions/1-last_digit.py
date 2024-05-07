#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)

if number < 0:
    last = number % 10 - 10
else:
    last = number % 10

if last == 0:
    size = "and is 0"
elif last > 5:
    size = "and is greater than 5"
elif last < 6:
    size = "and is less than 6 and not 0"
else:
    size = "and break the logic of this code"

print("Last digit of %i is %i %s" % (number, last, size))
