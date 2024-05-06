#!/usr/bin/python3
import random

number = random.randint(-10, 10)

if number > 0:
    sign = "is positive"
elif number < 0:
    sign = "is negative"
elif number == 0:
    sign = "is zero"
else:
    sign = "is somehow neither positive, negative, nor zero"

print("%i %s" % (number, sign))
